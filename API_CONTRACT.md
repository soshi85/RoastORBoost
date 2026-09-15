# Visionet Roast & Boost - API Contract

این سند ساختار ارتباطی بین فرانت‌اند (پرهام)، بک‌اند (سوشیانت/کسری) و هوش مصنوعی (نیما) را مشخص می‌کند. تمام دیتاها با این فرمت رد و بدل خواهند شد.

## 1. Upload API (دریافت رزومه و پردازش)

*   **Endpoint:** `POST /upload`
*   **Description:** دریافت فایل PDF از کاربر، ارسال به هوش مصنوعی و برگرداندن نتیجه نهایی.
*   **Request Type:** `multipart/form-data`
*   **Key:** `file` (فایل رزومه کاربر با فرمت PDF)

### ✅ Success Response (وضعیت 200 OK)
**نکته مهم برای فرانت‌اند:** مقادیر `roast_text` و `boost_tips` در خروجی نهایی ثابت نیستند و توسط هوش مصنوعی به صورت داینامیک (Dynamic) برای هر کاربر تولید می‌شوند. پرهام جان، فعلاً از این ساختار به عنوان Mock Data برای طراحی UI استفاده کن.

```json
{
  "status": "success",
  "message": "Resume processed successfully",
  "data": {
    "roast_text": "متن طنز و نقد بی‌رحمانه رزومه (تولید توسط هوش مصنوعی - نوع داده: String)",
    "boost_tips": [
      "پیشنهاد جدی اول برای بهبود رزومه (تولید توسط هوش مصنوعی - نوع داده: String)",
      "پیشنهاد جدی دوم...",
      "پیشنهاد جدی سوم..."
    ]
  }
}

{
  "status": "error",
  "message": "Error: Only PDF files are allowed! (نوع خطا به صورت متنی برگردانده می‌شود)"
}
