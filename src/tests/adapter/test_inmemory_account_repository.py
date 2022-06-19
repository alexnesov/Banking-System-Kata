from app.adapter.inmemory_account_repository import InMemoryAccountRepository
from app.domain.account import Account


def test_account_save():
    account = Account("alex", "nesov")
    account_repository = InMemoryAccountRepository()

    assert account.add_account(account_repository).account_id == account.account_id


def test_account_repository_all():
    account_repository = InMemoryAccountRepository()
    account1 = Account("alex", "nesov").add_account(account_repository)

    assert set(account_repository.list_accounts()) == {account1}
