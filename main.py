from __future__ import annotations

import uuid
from datetime import datetime, timezone
from pathlib import Path

import pymupdf
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from core.ai_service import AIServiceError, get_roast_and_boost
from core.pdf_extractor import extract_text_from_pdf

MAX_FILE_SIZE = 5 * 1024 * 1024
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI(title="Roast & Boost MVP")
app.mount("/static", StaticFiles(directory="static"), name="static")

def error_response(request_id: str, code: str, message: str, status_code: int):
    return JSONResponse(
        status_code=status_code,
        content={"ok": False, "requestId": request_id, "error": {"code": code, "message": message}}
    )

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.post("/api/v1/upload")
async def upload_resume(file: UploadFile = File(...)):
    request_id = f"req_{uuid.uuid4().hex[:12]}"
    filename = file.filename or "resume.pdf"

    if not filename.lower().endswith(".pdf"):
        return error_response(request_id, "INVALID_FILE_TYPE", "فقط فایل PDF مجاز است.", 400)

    file_bytes = await file.read(MAX_FILE_SIZE + 1)

    if len(file_bytes) > MAX_FILE_SIZE:
        return error_response(request_id, "FILE_TOO_LARGE", "حجم فایل باید حداکثر ۵ مگابایت باشد.", 400)

    if not file_bytes.startswith(b"%PDF-"):
        return error_response(request_id, "INVALID_PDF", "فایل ارسال‌شده PDF معتبر نیست.", 400)

    stored_path = UPLOAD_DIR / f"{request_id}.pdf"

    try:
        stored_path.write_bytes(file_bytes)
        try:
            clean_text = extract_text_from_pdf(str(stored_path))
        except (pymupdf.FileDataError, RuntimeError, ValueError):
            return error_response(request_id, "INVALID_PDF", "خواندن فایل PDF ممکن نبود.", 422)

        if not clean_text.strip():
            return error_response(request_id, "EMPTY_RESUME_TEXT", "متنی از این PDF استخراج نشد.", 422)

        ai_result = await get_roast_and_boost(clean_text)

        return {
            "ok": True,
            "requestId": request_id,
            "data": {
                "roast": ai_result["roast"],
                "boost": ai_result["boost"],
                "meta": {
                    "fileName": filename,
                    "processedAt": datetime.now(timezone.utc).isoformat()
                }
            }
        }

    except AIServiceError as exc:
        status_map = {
            "AI_TIMEOUT": 504,
            "AI_RATE_LIMIT": 503,
            "AI_CONNECTION_ERROR": 502,
            "AI_PROVIDER_ERROR": 502,
            "AI_NOT_CONFIGURED": 500,
            "AI_INVALID_RESPONSE": 502,
            "EMPTY_RESUME_TEXT": 422
        }
        return error_response(request_id, exc.code, exc.message, status_map.get(exc.code, 500))
    except Exception:
        return error_response(request_id, "INTERNAL_ERROR", "خطای داخلی در پردازش رزومه رخ داد.", 500)
    finally:
        if stored_path.exists():
            stored_path.unlink()
