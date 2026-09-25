from __future__ import annotations
import json, os
from pathlib import Path
import openai
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pydantic import ValidationError
from core.contracts import AIResult, normalize_validate_ai_result
load_dotenv()
PROMPT_PATH = Path(__file__).resolve().parents[1] / "prompts" / "roast_boost_prompt_v3.txt"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")
RESPONSE_SCHEMA = AIResult.model_json_schema()
class AIServiceError(Exception):
    def __init__(self,code:str,message:str): super().__init__(message); self.code=code; self.message=message

def _timeout_seconds():
    try:return float(os.getenv("OPENAI_TIMEOUT_SECONDS","45"))
    except ValueError:return 45.0

async def get_roast_and_boost(resume_text:str)->dict:
    if not isinstance(resume_text,str) or not resume_text.strip(): raise AIServiceError("EMPTY_RESUME_TEXT","متن رزومه خالی است.")
    api_key=os.getenv("OPENAI_API_KEY")
    if not api_key: raise AIServiceError("AI_NOT_CONFIGURED","کلید API هوش مصنوعی تنظیم نشده است.")
    client=AsyncOpenAI(api_key=api_key,timeout=_timeout_seconds(),max_retries=2)
    model=os.getenv("OPENAI_MODEL","gpt-5.6-luna")
    try:
        response=await client.responses.create(model=model,instructions=SYSTEM_PROMPT,input=f"<resume>\n{resume_text.strip()}\n</resume>",text={"format":{"type":"json_schema","name":"roast_boost_response","description":"Exactly 3 Roast strings and 3 Boost objects.","schema":RESPONSE_SCHEMA,"strict":True}},store=False)
        return normalize_validate_ai_result(json.loads(response.output_text))
    except (ValidationError,json.JSONDecodeError) as exc: raise AIServiceError("AI_INVALID_RESPONSE","پاسخ هوش مصنوعی با Schema مشترک پروژه سازگار نیست.") from exc
    except openai.APITimeoutError as exc: raise AIServiceError("AI_TIMEOUT","پردازش هوش مصنوعی بیش از حد طول کشید.") from exc
    except openai.RateLimitError as exc: raise AIServiceError("AI_RATE_LIMIT","سرویس هوش مصنوعی موقتاً شلوغ است.") from exc
    except openai.APIConnectionError as exc: raise AIServiceError("AI_CONNECTION_ERROR","ارتباط با سرویس هوش مصنوعی برقرار نشد.") from exc
    except openai.AuthenticationError as exc: raise AIServiceError("AI_NOT_CONFIGURED","کلید API هوش مصنوعی معتبر نیست.") from exc
    except openai.APIStatusError as exc: raise AIServiceError("AI_PROVIDER_ERROR","سرویس هوش مصنوعی در پردازش درخواست خطا داد.") from exc
