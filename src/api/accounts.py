from src.utils.starlingHttpClient import get_request

def get_account_balance(account_id):
    endpoint = f"/api/v2/accounts/{account_id}/balance"
    return get_request(endpoint)

def get_accounts():
    endpoint = f"/api/v2/accounts"
    return get_request(endpoint)

def get_account_holder():
    endpoint = f"/api/v2/account-holder"
    return get_request(endpoint)
