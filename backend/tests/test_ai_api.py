import os


def test_ai_endpoint_without_api_key(client):
    """Without OPENROUTER_API_KEY, should return 503."""
    # Ensure the key is not set
    original = os.environ.pop("OPENROUTER_API_KEY", None)
    try:
        response = client.post("/api/ai/generate-strategy", json={"prompt": "buy when RSI > 70"})
        assert response.status_code == 503
        assert "not configured" in response.json()["detail"].lower()
    finally:
        if original:
            os.environ["OPENROUTER_API_KEY"] = original


def test_ai_endpoint_validates_input(client):
    """Should reject request without prompt field."""
    response = client.post("/api/ai/generate-strategy", json={})
    assert response.status_code == 422  # Pydantic validation error
