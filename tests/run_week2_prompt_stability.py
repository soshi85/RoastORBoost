import asyncio,json
from datetime import datetime, timezone
from pathlib import Path
from core.ai_service import get_roast_and_boost
FIXTURES=Path("tests/fixtures/week2_prompt_cases.json"); ARTIFACT=Path("tests/artifacts/week2_prompt_stability_report.json")
def wc(t): return len([x for x in t.split() if x.strip()])
def checks(r):
    rc=[wc(x) for x in r["roast"]]; tc=[wc(x["title"]) for x in r["boost"]]; yw=[wc(x["why"]) for x in r["boost"]]; ac=[wc(x["action"]) for x in r["boost"]]
    return {"exactly_3_roast":len(r["roast"])==3,"exactly_3_boost":len(r["boost"])==3,"roast_distinct":len(set(x.casefold() for x in r["roast"]))==3,"boost_titles_distinct":len(set(x["title"].casefold() for x in r["boost"]))==3,"roast_word_range_12_35":all(12<=n<=35 for n in rc),"boost_title_word_range_2_8":all(2<=n<=8 for n in tc),"boost_why_word_range_10_30":all(10<=n<=30 for n in yw),"boost_action_word_range_10_40":all(10<=n<=40 for n in ac),"word_counts":{"roast":rc,"boost_title":tc,"boost_why":yw,"boost_action":ac}}
async def main():
    cases=json.loads(FIXTURES.read_text(encoding="utf-8")); report={"testedAt":datetime.now(timezone.utc).isoformat(),"caseCount":len(cases),"cases":[]}
    for i,c in enumerate(cases,1):
        print(f"[{i}/{len(cases)}] {c['id']}"); result=await get_roast_and_boost(c["resume_text"]); report["cases"].append({"id":c["id"],"source":c["source"],"response":result,"automatedChecks":checks(result),"manualReview":{"relevance":"TODO","no_hallucination":"TODO","tone":"TODO","actionability":"TODO","notes":""}})
    report["allStructuralChecksPassed"]=all(x["automatedChecks"]["exactly_3_roast"] and x["automatedChecks"]["exactly_3_boost"] and x["automatedChecks"]["roast_distinct"] and x["automatedChecks"]["boost_titles_distinct"] for x in report["cases"])
    ARTIFACT.parent.mkdir(parents=True,exist_ok=True); ARTIFACT.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8"); print("Saved:",ARTIFACT); print("Structural checks:","PASS" if report["allStructuralChecksPassed"] else "FAIL")
if __name__=="__main__": asyncio.run(main())
