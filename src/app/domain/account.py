from dataclasses import dataclass
from typing import TYPE_CHECKING
from random import randrange
from secrets import randbelow

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.account_repository import AccountRepository

from app.entrypoints.banking_cmd_line import Menu

@dataclass
class Account(Menu):
    account_holder_lastname: str 
    account_holder_firstname: str 

    account_id: str         
    account_code: str      
    
    balance: float          = 0

    @classmethod
    def generate(cls, account_holder_firstname, account_holder_lastname) -> 'Account':
        return cls(

            account_holder_firstname = account_holder_firstname,
            account_holder_lastname = account_holder_lastname,

            account_id=f'KATA{randrange(1e10):010}',
            account_code=f'{randbelow(10_000):04}',
        )

    def add_account(self, account_repository: 'AccountRepository', account_id: str):
        return account_repository.add_account(self, account_id)


    def get_balance(self):
        print(f"Current Balance: {self.balance} €")

    def deposit(self):
        is_num = False
        while not is_num:
            try:
                input_amount      = int(input('How much money would like to deposit?'))
                is_num            = True
            except ValueError:
                is_num            = False

        self.balance = self.balance + input_amount
        print(f"Current Balance: {self.balance} €")
    
    def withdraw(self):

        is_num = False
        while not is_num:
            try:
                input_amount      = int(input('How much money would you like to cash out?'))
                is_num            = True
            except ValueError:
                is_num            = False

        temp_balance = self.balance - input_amount

        if temp_balance < 0:
            print("Insufficient funds")
        else:
            self.balance = temp_balance

        print(f"Current Balance: {self.balance} €")

    def print_infos(self):
        print(
            f"\n\nYour account number: {self.account_id}\n"
            f"Your code: {self.account_code}\n"
            f"Note these identifiers down as you will need them to log in again.\n\n"
        )
    
    def __hash__(self):
        return hash(self.account_id)


    def logout(self) -> bool:
        print('You have successfully logged out!')
        return True



    MENU = (
        ('Exit', exit),
        ('Balance', get_balance),
        ('Deposit Money', deposit),
        ('Withdraw', withdraw),
        ('Log out', logout),
    )


