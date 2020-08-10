from util import *


@responses.activate
def test_start_verification(verify, dummy_data):
    stub(responses.POST, "https://api.nexmo.com/verify/json")

    params = {"number": "447525856424", "brand": "MyApp"}

    assert isinstance(verify.start_verification(params), dict)
    assert request_user_agent() == dummy_data.user_agent
    assert "number=447525856424" in request_body()
    assert "brand=MyApp" in request_body()


@responses.activate
def test_check_verification(verify, dummy_data):
    stub(responses.POST, "https://api.nexmo.com/verify/check/json")

    assert isinstance(
        verify.check("8g88g88eg8g8gg9g90", code="123445"), dict
    )
    assert request_user_agent() == dummy_data.user_agent
    assert "code=123445" in request_body()
    assert "request_id=8g88g88eg8g8gg9g90" in request_body()


@responses.activate
def test_get_verification(verify, dummy_data):
    stub(responses.GET, "https://api.nexmo.com/verify/search/json")

    assert isinstance(verify.search("xxx"), dict)
    assert request_user_agent() == dummy_data.user_agent
    assert "request_id=xxx" in request_query()


@responses.activate
def test_cancel_verification(verify, dummy_data):
    stub(responses.POST, "https://api.nexmo.com/verify/control/json")

    assert isinstance(verify.cancel("8g88g88eg8g8gg9g90"), dict)
    assert request_user_agent() == dummy_data.user_agent
    assert "cmd=cancel" in request_body()
    assert "request_id=8g88g88eg8g8gg9g90" in request_body()


@responses.activate
def test_trigger_next_verification_event(verify, dummy_data):
    stub(responses.POST, "https://api.nexmo.com/verify/control/json")

    assert isinstance(
        verify.trigger_next_event("8g88g88eg8g8gg9g90"), dict
    )
    assert request_user_agent() == dummy_data.user_agent
    assert "cmd=trigger_next_event" in request_body()
    assert "request_id=8g88g88eg8g8gg9g90" in request_body()

@responses.activate
def test_start_psd2_verification(verify, dummy_data):
    stub(responses.POST, "https://api.nexmo.com/verify/psd2/json")

    params = {"number": "447525856424", "brand": "MyApp"}

    assert isinstance(verify.psd2(params), dict)
    assert request_user_agent() == dummy_data.user_agent
    assert "number=447525856424" in request_body()
    assert "brand=MyApp" in request_body()