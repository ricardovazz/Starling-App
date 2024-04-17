from src.utils.starlingHttpClient import get_headers
import pytest
import os


def test_get_headers_with_token(monkeypatch):
    # Given
    expected_token = "test_token_123"
    monkeypatch.setenv("STARLING_ACCESS_TOKEN", expected_token)

    actual_token = os.getenv("STARLING_ACCESS_TOKEN")
    print(f"Token immediately after monkeypatch: {actual_token}")  # Should print 'test_token_123'

    # When
    headers = get_headers()

    # Then
    assert headers["Authorization"] == f"Bearer {expected_token}"
    assert headers["Content-Type"] == "application/json"

def test_get_headers_without_token_throws_error(monkeypatch):
    # Given
    # Environment variable is not set
    monkeypatch.delenv("STARLING_ACCESS_TOKEN", raising=False)

    # When
    with pytest.raises(ValueError) as excinfo:
        get_headers()

    assert "Missing access token" in str(excinfo.value)