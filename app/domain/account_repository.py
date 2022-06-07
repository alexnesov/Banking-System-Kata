import abc
from typing import List

from app.domain.account import Account

class AccountRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, vote: Account) -> Account:
        raise NotImplementedError
    
    @abc.abstractmethod
    def list_accounts(self) -> List[Account]:
        raise NotImplementedError
