@echo off
call .venv\Scripts\activate.bat
python -m pytest tests/test_ai_contract.py tests/test_pdf_extractor.py
python tests/live_ai_smoke_test.py
pause
