from __future__ import annotations

import json
import logging
import os
from pathlib import Path

import openai
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
logger = logging.getLogger(__name__)

PROMPT_PATH = Path(__file__).resolve().parents[1] / "prompts" / "roast_boost_prompt_v2.txt"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "roast": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
            "minItems": 3,
            "maxItems": 3
        },
        "boost": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "minLength": 1},
                    "why": {"type": "string", "minLength": 1},
                    "action": {"type": "string", "minLength": 1}
                },
                "required": ["title", "why", "action"],
                "additionalProperties": False
            },
            "minItems": 3,
            "maxItems": 3
        }
    },
    "required": ["roast", "boost"],
    "additionalProperties": False
}

class AIServiceError(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message

def _timeout_seconds() -> float:
    try:
        return float(os.getenv("OPENAI_TIMEOUT_SECONDS", "45"))
    except ValueError:
        return 45.0

def _validate_result(result: dict) -> dict:
    if set(result.keys()) != {"roast", "boost"}:
        raise AIServiceError("AI_INVALID_RESPONSE", "ساختار پاسخ هوش مصنوعی معتبر نیست.")
    if not isinstance(result["roast"], list) or len(result["roast"]) != 3:
        raise AIServiceError("AI_INVALID_RESPONSE", "خروجی باید دقیقاً ۳ Roast داشته باشد.")
    if not all(isinstance(x, str) and x.strip() for x in result["roast"]):
        raise AIServiceError("AI_INVALID_RESPONSE", "هر Roast باید متن معتبر باشد.")
    if not isinstance(result["boost"], list) or len(result["boost"]) != 3:
        raise AIServiceError("AI_INVALID_RESPONSE", "خروجی باید دقیقاً ۳ Boost داشته باشد.")
    for item in result["boost"]:
        if not isinstance(item, dict) or set(item.keys()) != {"title", "why", "action"}:
            raise AIServiceError("AI_INVALID_RESPONSE", "ساختار Boost معتبر نیست.")
        if not all(isinstance(item[k], str) and item[k].strip() for k in ("title", "why", "action")):
            raise AIServiceError("AI_INVALID_RESPONSE", "فیلدهای Boost نباید خالی باشند.")
    return result

async def get_roast_and_boost(resume_text: str) -> dict:
    if not isinstance(resume_text, str) or not resume_text.strip():
        raise AIServiceError("EMPTY_RESUME_TEXT", "متن رزومه خالی است.")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise AIServiceError("AI_NOT_CONFIGURED", "کلید API هوش مصنوعی تنظیم نشده است.")

    client = AsyncOpenAI(
        api_key=api_key,
        timeout=_timeout_seconds(),
        max_retries=2,
    )
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")

    try:
        response = await client.responses.create(
            model=model,
            instructions=SYSTEM_PROMPT,
            input=f"<resume>\n{resume_text.strip()}\n</resume>",
            text={"format": {
                "type": "json_schema",
                "name": "roast_boost_response",
                "description": "Exactly 3 Roast strings and 3 Boost objects.",
                "schema": RESPONSE_SCHEMA,
                "strict": True
            }},
            store=False,
        )
        return _validate_result(json.loads(response.output_text))
    except openai.APITimeoutError as exc:
        raise AIServiceError("AI_TIMEOUT", "پردازش هوش مصنوعی بیش از حد طول کشید.") from exc
    except openai.RateLimitError as exc:
        raise AIServiceError("AI_RATE_LIMIT", "سرویس هوش مصنوعی موقتاً شلوغ است.") from exc
    except openai.APIConnectionError as exc:
        raise AIServiceError("AI_CONNECTION_ERROR", "ارتباط با سرویس هوش مصنوعی برقرار نشد.") from exc
    except openai.AuthenticationError as exc:
        raise AIServiceError("AI_NOT_CONFIGURED", "کلید API هوش مصنوعی معتبر نیست.") from exc
    except openai.APIStatusError as exc:
        raise AIServiceError("AI_PROVIDER_ERROR", "سرویس هوش مصنوعی در پردازش درخواست خطا داد.") from exc
    except json.JSONDecodeError as exc:
        raise AIServiceError("AI_INVALID_RESPONSE", "پاسخ هوش مصنوعی JSON معتبر نبود.") from exc
