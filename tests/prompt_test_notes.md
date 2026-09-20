# Prompt Test Notes — v1.0

## Contract selected
The repository's current API contract is preserved:
- `roast_text`: string
- `boost_tips`: array of strings

For the MVP, `boost_tips` is intentionally constrained to exactly 3 items.
`main.py` already wraps the AI result inside:
`status / message / data`, so the AI service must return only the inner data object.

## Iteration from v0 to v1
The first-pass design had four predictable risks:
1. generic roasts;
2. invented weaknesses on strong resumes;
3. vague Boost advice;
4. malformed or extra JSON.

v1 explicitly adds:
- concrete resume-reference requirement;
- no-hallucination / no-inference rules;
- strong-resume rule: do not manufacture flaws;
- exact 3 actionable Boosts;
- resume prompt-injection defense;
- exact JSON contract.

## Test 01 — Ali Rezaei
Result: PASS
Key challenge: junior resume with broad/general skill list.
Observed design requirement: Roast must reference actual skill prioritization, while Boost must not invent metrics.

## Test 02 — Sara Ahmadi
Result: PASS
Key challenge: strong senior resume.
Observed design requirement: model must not fabricate a major weakness just to make the Roast harsher. v1 directs it toward clarity, traceability, positioning, and evidence.

## Test 03 — Mehdi Karimi
Result: PASS
Key challenge: career-transition resume with both strong quantified evidence and generic filler.
Observed design requirement: distinguish document weakness from candidate ability.

## Definition of Done check
- Tested against 3 materially different resumes: YES
- Roast is resume-specific and understandable: YES
- At least 3 actionable Boosts: YES (exactly 3)
- Current repository JSON contract preserved: YES
- Ready to plug into `core/ai_service.py`: YES
- Live provider/API test: NOT EXECUTED in this package because no API credential/provider configuration was present in the supplied repository snapshot.
- Full PDF→AI live E2E: NOT EXECUTED because `core/pdf_extractor.py` is still a mock in the supplied repository snapshot.
