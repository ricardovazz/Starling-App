from src.api.accounts import get_accounts
from src.api.accounts import get_account_holder
from src.api.accounts import get_account_balance
import os
from dotenv import load_dotenv

load_dotenv()

def get_uid_for_currency_account(accountsJson, currency):
    accounts_data = accountsJson['accounts']
    for account in accounts_data:
        if account['currency'] == currency:
            return account['accountUid']

def start():

    try:
        uids = get_accounts()
        print(f"JSON RESPONSE: {uids.json()}")
        
        print("=========")

        account_id = get_account_holder().json()
        print(f"JSON RESPONSE  : {account_id}")

        print("=========")

        if gbp_account_uid := get_uid_for_currency_account(uids.json(), "GBP"):
            balance = get_account_balance(gbp_account_uid)
            print(f"GBP Account Balance: {balance.json()}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
