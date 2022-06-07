from app.adapter.inmemory_account_repository import InMemoryAccountRepository
from app.domain.account import Account


def main():

    account_repository = InMemoryAccountRepository()

    Account().save(account_repository)
    Account().save(account_repository)

    print(account_repository.list_accounts())



if __name__ == '__main__':
    main()