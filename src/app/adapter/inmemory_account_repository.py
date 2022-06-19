from typing import List, Dict

from app.domain.account import Account
from app.domain.account_repository import AccountRepository


class InMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account, account_id: str) -> Account:
        print("Adding account. . .")
        self.accounts[account_id] = account
        return account

    def list_accounts(self) -> Dict[str, Account]:
        return self.accounts