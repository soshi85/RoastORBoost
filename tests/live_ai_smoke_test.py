import asyncio, json, os
from core.ai_service import get_roast_and_boost

SAMPLE_TEXT="""توسعه‌دهنده Backend جونیور
مهارت‌ها: Python, Django, PostgreSQL, Git
تجربه: همکاری در توسعه API داخلی و رفع باگ‌های گزارش‌شده.
پروژه شخصی: سیستم مدیریت هزینه با JWT و CRUD."""

async def main():
    if not os.getenv("OPENAI_API_KEY"): raise SystemExit("OPENAI_API_KEY تنظیم نشده است.")
    result=await get_roast_and_boost(SAMPLE_TEXT)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    assert len(result["roast"])==3 and len(result["boost"])==3
    print("LIVE AI TEST PASSED")

if __name__=="__main__": asyncio.run(main())
