from typing import List

from app.domain.account import Account
from app.domain.account_repository import AccountRepository


class InMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.accounts = []

    def add(self, account: Account) -> Account:
        self.accounts.append(account)
        return account

    def list_accounts(self) -> List[Account]:
        return self.accounts

    def total(self) -> int:
        return len(self.accounts)