from src.api.transactions import get_recent_transactions
import os


def test_get_recent_transactions(httpx_mock):
    # Given
    BASE_URL = os.getenv('BASE_URL')
    URL = str(BASE_URL) + "/api/v2/accounts/dummy-account-id/transactions"
    JSON = {'transactions': [{'id': 'tx1'}, {'id': 'tx2'}]}
    httpx_mock.add_response(url=URL, json=JSON)

    # When
    response = get_recent_transactions('dummy-account-id')

    # Then
    assert response.status_code == 200
    assert "tx1" and "tx2" in response.text
