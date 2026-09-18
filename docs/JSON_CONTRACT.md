
---

## 📄 فایل ۲: `JSON_CONTRACT.md` 

```markdown
# JSON Contract (Internal AI Communication)

این سند قرارداد بین **Backend** و **AI** است.  
نکته مهم: `requestId` و `meta` جزو خروجی AI نیستند و فقط توسط Backend اضافه می‌شوند.

---

## 1. Request to AI (از طرف Backend به AI)

```json
{
  "resumeText": "متن پاک‌سازی شده رزومه",
  "language": "fa",
  "roastCount": 3,
  "boostCount": 3
}