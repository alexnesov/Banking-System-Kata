import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.account_repository import AccountRepository

@dataclass
class Account:
    account_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def save(self, account_repository: 'AccountRepository'):
        return account_repository.add(self)
    
    def __hash__(self):
        return hash(self.account_id)


        