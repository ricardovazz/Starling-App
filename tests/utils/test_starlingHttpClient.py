from src.utils.starlingHttpClient import get_headers

def test_get_headers_with_token(monkeypatch):
    # Given
    expected_token = "test_token_123"
    monkeypatch.setenv("STARLING_ACCESS_TOKEN", expected_token)

    # When
    headers = get_headers()

    # Then
    assert headers["Authorization"] == f"Bearer {expected_token}"
    assert headers["Content-Type"] == "application/json"

def test_get_headers_without_token(monkeypatch):
    # Given
    # Environment variable is not set
    monkeypatch.delenv("STARLING_ACCESS_TOKEN", raising=False)

    # When
    headers = get_headers()

    # Then
    assert headers["Authorization"] == "Bearer None" 
    assert headers["Content-Type"] == "application/json"