import uuid

from app.domain.account import Account

def test_account_existing_account_id():
    account_id = str(uuid.uuid4())

    assert Account("alex", "nesov", account_id=account_id).account_id == account_id
