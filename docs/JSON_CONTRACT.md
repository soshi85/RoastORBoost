# JSON Contract — Backend ↔ AI

Backend runtime call:

```python
await get_roast_and_boost(clean_resume_text)
```

AI must return exactly:

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

No extra keys.

`requestId`, `fileName`, and `processedAt` are Backend responsibilities.
