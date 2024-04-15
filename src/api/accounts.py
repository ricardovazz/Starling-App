from src.utils.starlingHttpClient import get_request

def get_account_balance(account_id):
    endpoint = f"/api/v2/accounts/{account_id}/balance"
    return get_request(endpoint)

