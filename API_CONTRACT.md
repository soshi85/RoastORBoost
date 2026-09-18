📄 Visionet Roast & Boost - API & JSON Contract V1.0توسعه‌دهندگان بک‌اند: کسری / سوشیانتمرجع هوش مصنوعی: نیماتوسعه‌دهنده فرانت‌اند: پرهاماین سند به عنوان «منبع حقیقت» (Single Source of Truth) برای ارتباطات کلاینت (Frontend) و سرور (Backend/AI) تدوین شده است. تمامی درخواست‌ها و پاسخ‌ها باید اکیداً از این ساختار پیروی کنند.🏗 ۱. استانداردهای کلی (Global Standards)Base URL: https://api.visionet.com/api/v1 (محیط پروداکشن)Content-Type (General): application/jsonContent-Type (Uploads): multipart/form-dataAuthentication: ارسال توکن در هدر Authorization: Bearer <token> (در فازهای بعدی)📦 ۲. ساختار پایه پاسخ‌ها (Base Response Wrapper)تمامی خروجی‌های API (موفق یا ناموفق) در یک Wrapper استاندارد قرار می‌گیرند تا فرانت‌اند همیشه بداند با چه فرمتی روبه‌رو است.✅ ۲.۱. ساختار موفق (Success Response){
  "success": true,
  "status_code": 200,
  "message": "عملیات با موفقیت انجام شد.",
  "meta": {
    "timestamp": "2026-09-18T10:00:00Z",
    "request_id": "req-987654321"
  },
  "data": { 
    // Payload اصلی در این قسمت قرار می‌گیرد
  }
}
❌ ۲.۲. ساختار ناموفق (Error Response){
  "success": false,
  "status_code": 400,
  "message": "خطای اعتبارسنجی داده‌ها",
  "error": {
    "code": "VAL_001",
    "details": "فرمت فایل ارسال شده پشتیبانی نمی‌شود."
  }
}
🚀 ۳. مستندات Endpoint ها🔹 ۳.۱. سرویس آپلود و تحلیل یکپارچه (Roast & Boost)این سرویس فایل PDF کاربر را دریافت کرده و پس از پردازش متن توسط هوش مصنوعی، نتایج نقد (Roast) و راهکارهای بهبود (Boost) را با جزئیات کامل برمی‌گرداند.Endpoint: POST /resume/analyzeRequest Type: multipart/form-data📥 پارامترهای فرم (Form-Data)ParameterTypeRequiredDescriptionConstraintsfileFileYesفایل رزومه کاربرMax: 5MB, Format: .pdflangStringNoزبان ترجیحی برای خروجیfa (default), entoneStringNoلحن Roastfunny, harsh, professional📤 خروجی موفق - تحلیل کامل (200 OK)💡 پیام برای پرهام: ساختار داده‌ها داینامیک شده است. scores برای نمایش چارت‌ها و boost_tips به صورت آرایه‌ای از آبجکت‌هاست تا بتوانی آیکون/رنگ هر ارور (critical, moderate) را در UI هندل کنی.{
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
      "title": "🔥 AI Roast",
      "text": "راستش رو بخوای، رزومه‌ت بیشتر شبیه لیست خرید سوپرمارکته تا یک رزومه حرفه‌ای! اینکه نوشتی 'مسلط به کار تیمی' رو همه می‌نویسن، دقیقاً چیکار کردی؟ فونت‌ها انقدر درهمه که هوش مصنوعی من هم سرگیجه گرفت!",
      "burn_level": "High"
    },
    "boost_section": {
      "title": "🚀 Boost Tips",
      "tips": [
        {
          "category": "Format",
          "severity": "critical",
          "suggestion": "حاشیه‌های فایل استاندارد نیست. از یک قالب تک‌ستونه ATS-Friendly استفاده کنید."
        },
        {
          "category": "Content",
          "severity": "high",
          "suggestion": "در بخش تجربیات کاری، به جای لیست کردن وظایف، از اعداد و دستاوردها استفاده کنید (مثلا: افزایش ۲۰ درصدی فروش)."
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
⚠️ ۴. دیکشنری کدهای خطا (Error Codes Dictionary)برای هندل کردن دقیق خطاها در فرانت‌اند، از این کدها استفاده می‌شود:Error CodeHTTP StatusDescriptionAction for FrontendFILE_4001400حجم فایل بیشتر از ۵ مگابایت است.نمایش پیام توست (Toast) به کاربرFILE_4002400فرمت فایل نامعتبر است (فقط PDF).مسدود کردن دکمه آپلود / پیام اخطارAI_5001500خطای تایم‌اوت در ارتباط با سرور AI.نمایش دکمه "تلاش مجدد" (Retry)AI_5002422متن داخل PDF قابل استخراج یا خواندن نیست (Scanned PDF).درخواست از کاربر برای آپلود فایل متنی
