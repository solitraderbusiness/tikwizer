def test_generate_minimal_strategy(client, minimal_strategy):
    response = client.post("/api/generate", json=minimal_strategy)
    assert response.status_code == 200
    data = response.json()
    assert "code" in data
    assert "filename" in data
    assert data["filename"] == "expert_output.mq4"
    assert len(data["code"]) > 1000  # Should be substantial


def test_generate_contains_mql4_structure(client, minimal_strategy):
    response = client.post("/api/generate", json=minimal_strategy)
    code = response.json()["code"]
    assert "OnTick" in code
    assert "OnInit" in code
    assert "OnDeinit" in code


def test_generate_contains_copyright(client, minimal_strategy):
    response = client.post("/api/generate", json=minimal_strategy)
    code = response.json()["code"]
    assert "tikwizer" in code.lower()


def test_generate_condition_with_buy(client, condition_with_buy_strategy):
    response = client.post("/api/generate", json=condition_with_buy_strategy)
    assert response.status_code == 200
    code = response.json()["code"]
    assert "OnTick" in code
    assert len(code) > 1000


def test_generate_empty_strategy(client, empty_strategy):
    response = client.post("/api/generate", json=empty_strategy)
    assert response.status_code == 200
    code = response.json()["code"]
    assert "OnTick" in code


def test_generate_preview(client, minimal_strategy):
    response = client.post("/api/generate/preview", json=minimal_strategy)
    assert response.status_code == 200
    data = response.json()
    assert "code" in data


def test_generate_invalid_json_returns_500(client):
    response = client.post("/api/generate", json={"bad": "data"})
    assert response.status_code == 500
