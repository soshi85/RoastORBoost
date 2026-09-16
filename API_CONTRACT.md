# API Contract (Roast & Boost)

## Base URL
`/api/v1`

## 1. Upload API (دریافت رزومه و پردازش)
- **Endpoint:** `POST /api/v1/upload`
- **Description:** دریافت فایل PDF، استخراج متن، ارسال به AI و برگرداندن نتیجه Roast/Boost.
- **Request Type:** `multipart/form-data`
- **Key:** `file` (فرمت PDF، حداکثر ۵ مگابایت)

### Success Response (200 OK)
```json
{
  "ok": true,
  "requestId": "req_123456",
  "data": {
    "roast": [
      "نقد اول",
      "نقد دوم",
      "نقد سوم"
    ],
    "boost": [
      {
        "title": "عنوان پیشنهاد",
        "why": "دلیل اهمیت",
        "action": "اقدام مشخص"
      }
    ],
    "meta": {
      "fileName": "resume.pdf",
      "processedAt": "2026-09-16T12:00:00Z"
    }
  }
}