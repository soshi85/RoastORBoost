# Day 8 — Review Week 1 + Prioritized Blockers

## P0 — Blocker
1. **Real E2E repeatable** — Owner: Nima + Soshiant + Parham. Done = one real PDF goes UI → Upload → Extract/Clean → AI → JSON → Result without manual editing.
2. **Single runtime contract** — Owner: Kasra + Nima + Soshiant. Done = only `roast[3] + boost[3]{title,why,action}` is used; old `roast_text/boost_tips` is gone from main flow.

## P1 — Critical quality
3. **Prompt stability on 5 resumes** — Owner: Nima. Done = 5 cases, fixed count, manual review PASS.
4. **Shared Normalize/Validate** — Owner: Kasra + Nima + Soshiant. Done = one strict Pydantic schema; wrong count/extra keys rejected; whitespace normalized.
5. **Backend basic error handling** — Owner: Soshiant. Done = invalid PDF/empty text/AI timeout/provider error do not crash.
6. **Frontend consumes real response** — Owner: Parham + Soshiant. Done = real Loading/Error/Success; Mock removed from main flow.

## Later
Shareable polish, UI polish, advanced PDF edge cases, analytics, auth/payment, scoring, multi-language/tone selector.

Decision: no new feature enters main flow before P0 blockers are closed.
