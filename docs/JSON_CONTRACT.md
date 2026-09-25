# JSON Contract — Week 2 Frozen Shared Schema

AI + Backend + Frontend shared data object:

```json
{
  "roast": ["string", "string", "string"],
  "boost": [
    {"title":"string","why":"string","action":"string"},
    {"title":"string","why":"string","action":"string"},
    {"title":"string","why":"string","action":"string"}
  ]
}
```

Rules:
- exactly 3 Roast strings
- exactly 3 Boost objects
- no extra keys
- strings non-empty after normalization
- Roast items distinct
- Boost titles distinct

Normalize only whitespace. Old schemas (`roast_text`, `boost_tips`) are invalid and are NOT auto-converted.

Backend adds `requestId` and `meta`; AI does not.
