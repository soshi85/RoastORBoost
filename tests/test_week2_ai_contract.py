import pytest
from pydantic import ValidationError
from core.contracts import AIResult, normalize_validate_ai_result

def valid_payload():
    return {"roast":["  roast one  ","roast two","roast three"],"boost":[{"title":"  title one ","why":"why one","action":"action one"},{"title":"title two","why":"why two","action":"action two"},{"title":"title three","why":"why three","action":"action three"}]}

def test_valid_schema_and_normalization():
    r=normalize_validate_ai_result(valid_payload()); assert r["roast"][0]=="roast one"; assert r["boost"][0]["title"]=="title one"
def test_two_roasts_rejected():
    p=valid_payload(); p["roast"]=p["roast"][:2]
    with pytest.raises(ValidationError): AIResult.model_validate(p)
def test_four_boosts_rejected():
    p=valid_payload(); p["boost"].append({"title":"t4","why":"w4","action":"a4"})
    with pytest.raises(ValidationError): AIResult.model_validate(p)
def test_extra_key_rejected():
    p=valid_payload(); p["extra"]="x"
    with pytest.raises(ValidationError): AIResult.model_validate(p)
def test_old_schema_rejected():
    with pytest.raises(ValidationError): AIResult.model_validate({"roast_text":"old","boost_tips":["a","b","c"]})
def test_duplicate_roast_rejected():
    p=valid_payload(); p["roast"]=["same","same","different"]
    with pytest.raises(ValidationError): AIResult.model_validate(p)
