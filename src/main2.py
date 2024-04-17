from src.api.accounts import get_account_balance
from src.api.transactions import get_recent_transactions
import os
from dotenv import load_dotenv

load_dotenv()

def start():
    account_id = "bc3b61e0-6d7c-420b-a13b-f4be26bb95ee"

    try:
        # Fetch account balance
        balance = get_account_balance(account_id)
        print(f"Account Balance: {balance.text}")


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
