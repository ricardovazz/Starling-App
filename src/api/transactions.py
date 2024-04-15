from src.utils.starlingHttpClient import get_request

def get_recent_transactions(account_id):
    endpoint = f"/api/v2/accounts/{account_id}/transactions"
    return get_request(endpoint)