def test_get_blocks_returns_categories(client):
    response = client.get("/api/templates/blocks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Each item should have category and blocks
    for cat in data:
        assert "category" in cat
        assert "blocks" in cat
        assert isinstance(cat["blocks"], list)


def test_get_blocks_has_buy_sell_category(client):
    response = client.get("/api/templates/blocks")
    data = response.json()
    categories = [c["category"] for c in data]
    assert "buy_sell" in categories


def test_get_blocks_buy_sell_has_blocks(client):
    response = client.get("/api/templates/blocks")
    data = response.json()
    buy_sell = next(c for c in data if c["category"] == "buy_sell")
    block_names = [b["name"] for b in buy_sell["blocks"]]
    assert "buy_sell" in block_names


def test_block_has_required_fields(client):
    response = client.get("/api/templates/blocks")
    data = response.json()
    first_block = data[0]["blocks"][0]
    assert "name" in first_block
    assert "display_name" in first_block
    assert "category" in first_block
    assert "default_params" in first_block


def test_get_indicators_returns_list(client):
    response = client.get("/api/templates/indicators")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_indicators_has_rsi(client):
    response = client.get("/api/templates/indicators")
    data = response.json()
    names = [i["name"] for i in data]
    assert "rsi" in names


def test_get_indicators_has_ma(client):
    response = client.get("/api/templates/indicators")
    data = response.json()
    names = [i["name"] for i in data]
    assert "ma" in names


def test_indicator_has_required_fields(client):
    response = client.get("/api/templates/indicators")
    data = response.json()
    first = data[0]
    assert "name" in first
    assert "display_name" in first
    assert "default_params" in first
