from core.ai_service import _validate_result, AIServiceError

def test_valid_contract():
    payload={"roast":["r1","r2","r3"],"boost":[
        {"title":"t1","why":"w1","action":"a1"},
        {"title":"t2","why":"w2","action":"a2"},
        {"title":"t3","why":"w3","action":"a3"}]}
    assert _validate_result(payload)==payload

def test_invalid_roast_count():
    payload={"roast":["r1","r2"],"boost":[
        {"title":"t1","why":"w1","action":"a1"},
        {"title":"t2","why":"w2","action":"a2"},
        {"title":"t3","why":"w3","action":"a3"}]}
    try:_validate_result(payload)
    except AIServiceError:return
    raise AssertionError("Expected AIServiceError")
