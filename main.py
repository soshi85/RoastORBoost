import os
from fastapi import FastAPI, File, UploadFile, HTTPException

# ایمپورت کردن توابعی که الان ساختیم
from core.pdf_extractor import extract_text_from_pdf
from core.ai_service import get_roast_and_boost


app = FastAPI()
os.makedirs("uploads", exist_ok=True)

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    
    # ۱. اعتبارسنجی فایل
    if not file.filename.endswith(".pdf") and file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Error: Only PDF files are allowed!")
    
    file_location = f"uploads/{file.filename}"
    
    # ۲. ذخیره فایل
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())
    
    # ۳. استخراج متن (صدا زدن تابع مهیار)
    extracted_text = extract_text_from_pdf(file_location)
    
    # ۴. ارسال به هوش مصنوعی (صدا زدن تابع نیما)
    ai_result = get_roast_and_boost(extracted_text)
    
    # ۵. برگرداندن جواب نهایی به فرانت‌اند (دقیقاً طبق JSON Contract)
    return {
        "status": "success",
        "message": "Resume processed successfully",
        "data": ai_result
    }