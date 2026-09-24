# Visionet Roast & Boost - API & JSON Contract V1.0

توسعه‌دهندگان بک‌اند: کسری / توسعه‌دهندگان فرانت‌اند: پرهام / هوش مصنوعی: نیما 
این سند به عنوان منبع حقیقت (Single Source of Truth) تدوین شده است. تمامی درخواست‌ها و پاسخ‌ها باید اکیداً از این ساختار پیروی کنند برای ارتباطات کلاینت (Frontend) و سرور (Backend/AI).

## ۱. استانداردهای کلی (Global Standards)
* **Base URL:** `[https://api.visionet.com/api/v1](https://api.visionet.com/api/v1)` (محیط پروداکشن)
* **Content-Type (General):** `application/json`
* **Content-Type (Uploads):** `multipart/form-data`
* **Authentication:** ارسال توکن در هدر `Authorization: Bearer`

## ۲. ساختار پایه پاسخ‌ها (Base Response)
تمامی خروجی‌های API (موفق یا ناموفق) در یک Wrapper استاندارد قرار می‌گیرند تا فرانت‌اند همیشه بداند با چه فرمتی روبه‌رو است.

### ۲.۱. ساختار موفق (Success)
```json
{
  "success": true,
  "status_code": 200,
  "message": "عملیات با موفقیت انجام شد.",
  "meta": {
    "timestamp": "2026-09-18T10:00:00Z",
    "request_id": "req-987654321"
  },
  "data": { } // Payload اصلی در این قسمت قرار می‌گیرد
}
{
  "success": false,
  "status_code": 400,
  "message": "خطای اعتبارسنجی داده‌ها",
  "error": {
    "code": "VAL_001",
    "details": "فرمت فایل ارسال شده پشتیبانی نمی‌شود."
  {
  "success": true,
  "status_code": 200,
  "message": "Resume successfully analyzed by AI.",
  "data": {
    "summary": {
      "overall_score": 68,
      "ai_conclusion": "رزومه شما پتانسیل خوبی دارد اما در بخش پرزنتیشن و توضیح دستاوردها به شدت ضعیف عمل کرده‌اید."
    },
    "scores": {
      "design_and_format": 50,
      "content_quality": 75,
      "impact_and_metrics": 40,
      "grammar_and_spelling": 90
    },
    "roast_section": {
      "title": "AI Roast",
      "text": "راستش رو بخوای رزومه‌ت بیشتر شبیه لیست خرید سوپرمارکته تا یک رزومه حرفه‌ای! اینکه نوشتی 'مسلط به کار تیمی' رو همه می‌نویسن، دقیقاً چیکار کردی؟ فونت‌ها انقدر در همه که هوش مصنوعی من هم سرگیجه گرفت."
    },
    "boost_section": {
      "title": "Boost Tips",
      "tips": [
        {
          "category": "Format",
          "severity": "critical",
          "suggestion": "از یک قالب تک‌ستونه ATS-Friendly استفاده کنید. حاشیه‌های فایل استاندارد نیست."
        },
        {
          "category": "Content",
          "severity": "high",
          "suggestion": "به جای لیست کردن وظایف، از اعداد و دستاوردها استفاده کنید (مثلا: افزایش ۲۰ درصدی فروش)."
        },
        {
          "category": "Skills",
          "severity": "moderate",
          "suggestion": "مهارت‌های نرم (Soft Skills) را با مهارت‌های فنی (Hard Skills) ترکیب نکنید؛ آن‌ها را تفکیک کنید."
        }
      ]
    }
  }
}
  }
}
