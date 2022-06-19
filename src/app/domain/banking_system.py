
from getpass import getpass
from typing import TYPE_CHECKING

from app.entrypoints.banking_cmd_line import Menu
from app.domain.account import Account
from app.domain.account_repository import AccountRepository


class BankingSystem(Menu):
    """
    
    """
    def __init__(self, account_repository: 'AccountRepository') -> None:
        self.account_repository = account_repository

    def create_account(self):
        firstname   = input('Enter your first name: ')
        lastname    = input('Enter your last name: ')     

        account     = Account.generate(firstname, lastname)
        account.print_infos()
        account.add_account(self.account_repository, account.account_id)

        print("Account created.")

    def log_in(self):
        account_id      = input('Enter your account ID: ')
        account_code    = getpass('Enter your code: ')
        

        print("TEST")
        print(self.account_repository.accounts)
        print(type(self.account_repository.accounts))

        account         = self.account_repository.accounts.get(account_id)

        if account is None or account.account_code != account_code:
            print('Wrong account ID or code')
        else:
            print('You have successfully logged in!')
            account.screen()
    
    def exit(self) -> bool:
        print('Bye!')
        return True

    MENU = (
        ('Exit', exit),
        ('Create an account', create_account),
        ('Log into an account', log_in),
    )