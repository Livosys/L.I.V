from routers.contracts import ReactPayload

def test_react_payload_contract():
    p = ReactPayload(ticket_id=1, goal="test")
    assert p.ticket_id == 1
