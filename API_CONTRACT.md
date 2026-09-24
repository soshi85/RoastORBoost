# API Contract (Roast & Boost MVP)

## Base URL
`/api/v1`

---

## 1. Upload API (دریافت رزومه و پردازش)

- **Endpoint:** `POST /upload`
- **Description:** دریافت فایل PDF، استخراج متن، ارسال به AI و برگرداندن نتیجه Roast/Boost.
- **Request Type:** `multipart/form-data`
- **Key:** `file` (فرمت PDF، حداکثر ۵ مگابایت)

### Success Response (200 OK)

> **نکته:** کلیدهای `status` و `message` توسط **Backend** تولید می‌شوند. هوش مصنوعی فقط `roast_text` و `boost_tips` را برمی‌گرداند.

```json
{
  "status": "success",
  "message": "Resume processed successfully",
  "data": {
    "roast_text": "این رزومه بین «Backend Developer جونیور» و «فهرست چیزهایی که یک‌بار از کنارشان رد شده‌ام» گیر کرده؛ Python و Django و JWT مسیر خوبی ساخته‌اند، ولی Microsoft Office، Docker و Linux بدون سطح یا خروجی مشخص فقط صندلی‌های اضافه مهمانی مهارت‌ها هستند.",
    "boost_tips": [
      "خلاصه حرفه‌ای را از متن عمومی کوتاه‌تر و هدفمندتر کن: نقش هدف، Python/Django و یک نمونه کار واقعی را در همان ۲–۳ خط اول برجسته کن.",
      "در تجربه کارآموزی، اثر کار را روشن‌تر کن؛ مثلاً اگر عدد واقعی داری تعداد APIها یا Bugهای رفع‌شده را اضافه کن.",
      "بخش مهارت‌ها را اولویت‌بندی کن: Python، Django، Django REST و PostgreSQL را به‌عنوان Core Backend جدا کن."
    ]
  }
}