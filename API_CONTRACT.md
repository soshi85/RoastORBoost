# Roast & Boost — API Contract v1.0 (Week 1 Frozen)

## Endpoint
`POST /api/v1/upload`

Request:
- multipart/form-data
- field: `file`
- PDF only
- max size: 5 MB

## Success
```json
{
  "ok": true,
  "requestId": "req_...",
  "data": {
    "roast": ["string", "string", "string"],
    "boost": [
      {"title":"string","why":"string","action":"string"},
      {"title":"string","why":"string","action":"string"},
      {"title":"string","why":"string","action":"string"}
    ],
    "meta": {"fileName":"resume.pdf","processedAt":"ISO-8601 UTC"}
  }
}
```

## Error
```json
{
  "ok": false,
  "requestId": "req_...",
  "error": {"code":"INVALID_FILE_TYPE","message":"فقط فایل PDF مجاز است."}
}
```

Week-1 error codes:
- INVALID_FILE_TYPE
- FILE_TOO_LARGE
- INVALID_PDF
- EMPTY_RESUME_TEXT
- AI_TIMEOUT
- AI_RATE_LIMIT
- AI_CONNECTION_ERROR
- AI_PROVIDER_ERROR
- AI_NOT_CONFIGURED
- INTERNAL_ERROR

Out of scope for Week 1:
authentication, scoring, payment, user profile, advanced analytics, tone selector, multi-language selector, full resume rewrite.
