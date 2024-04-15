from src.api.accounts import get_account_balance


def test_get_account_balance(httpx_mock):
    # Given
    URL = "https://api-sandbox.starlingbank.com/api/v2/accounts/dummy-account-id/balance"
    JSON = {'effectiveBalance': 123.45}
    httpx_mock.add_response(url=URL, json=JSON)

    # When
    response = get_account_balance('dummy-account-id')

    # Then
    assert response.status_code == 200
    assert "123.45" in response.text