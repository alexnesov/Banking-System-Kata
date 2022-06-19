from app.adapter.inmemory_account_repository import InMemoryAccountRepository
from app.domain.account import Account
from app.domain.banking_system import BankingSystem

def main():
    """
    """

    account_repository = InMemoryAccountRepository()
    BankingSystem(account_repository).screen()

    print(account_repository.list_accounts())



if __name__ == '__main__':
    main()