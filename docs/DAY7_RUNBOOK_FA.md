# Day 7 Runbook

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
# .env را باز کن و API Key واقعی را وارد کن
python -m pytest tests/test_ai_contract.py tests/test_pdf_extractor.py
python tests/live_ai_smoke_test.py
uvicorn main:app --reload
```

بعد مرورگر:
`http://127.0.0.1:8000`

تست نهایی:
1. PDF ساده → Result
2. PDF چندصفحه‌ای → Result
3. JPG → Error
4. هر Success = دقیقاً 3 Roast + 3 Boost

اگر حداقل یک PDF واقعی از UI تا Result بدون دخالت دستی اجرا نشود، Week 1 هنوز Done نیست.
