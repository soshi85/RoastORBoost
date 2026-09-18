# API Contract (Roast & Boost MVP)

## Base URL
`/api/v1`

---

## 1. Upload API (دریافت رزومه و پردازش)

- **Endpoint:** `POST /api/v1/upload`
- **Description:** دریافت فایل PDF، استخراج متن، ارسال به AI و برگرداندن نتیجه Roast/Boost.
- **Request Type:** `multipart/form-data`
- **Key:** `file` (فرمت PDF، حداکثر ۵ مگابایت — پس از تأیید تیم Backend)

### Success Response (200 OK)

> **نکته:** کلیدهای `requestId` و `meta` توسط **Backend** تولید می‌شوند، نه AI. هوش مصنوعی فقط `roast` و `boost` را برمی‌گرداند.

```json
{
  "ok": true,
  "requestId": "req_mock_123",
  "data": {
    "roast": [
      "نوشتی مسلط به Word و Excel؟ الان ۲۰۲۶ است نه ۲۰۰۴.",
      "این بخش تجربه‌ها بیشتر شبیه شرح وظایف است تا دستاورد.",
      "ایمیلت حرفه‌ای نیست."
    ],
    "boost": [
      {
        "title": "مهارت‌هایت را به‌روز کن",
        "why": "Word و Excel عمومی شده‌اند و مزیت رقابتی نیستند.",
        "action": "به جای «مسلط به آفیس» بنویس «تحلیل داده با Excel و ساخت داشبورد با Power BI»."
      },
      {
        "title": "دستاورد بنویس، نه وظیفه",
        "why": "استخدام‌کننده نتیجه را می‌خرد، نه مسئولیت را.",
        "action": "هر تجربه را با عدد و نتیجه بنویس."
      },
      {
        "title": "خلاصه رزومه را هدفمند کن",
        "why": "خلاصه فعلی برای هر شغلی استفاده می‌شود.",
        "action": "خلاصه را برای همان موقعیت شغلی بنویس."
      }
    ],
    "meta": {
      "fileName": "resume.pdf",
      "processedAt": "2026-09-16T12:00:00Z"
    }
  }
}