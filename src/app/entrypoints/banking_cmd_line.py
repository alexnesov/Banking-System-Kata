from typing import Tuple, Callable, ClassVar



class Menu:
    MENU: ClassVar[Tuple[
        Tuple[
            str, Callable[['Menu'], bool]
        ], ...
    ]]

    def screen(self):
        prompt = '\n'.join(
            f'{i}. {name}'
            for i, (name, fun) in enumerate(self.MENU)
        ) + '\n'

        while True:
            choice = input(prompt)

            try:
                name, fun = self.MENU[int(choice)]
            except ValueError:
                print('Invalid integer entered')
            except IndexError:
                print('Choice out of range')
            else:
                if fun(self):
                    break


class SystemMenuTest(Menu):
    def __init__(self):
        pass

    def test_hello(self):
        print("Hello World")

    MENU = (
        ('Exit', exit),
        ('Print', test_hello)
    )


if __name__ == '__main__':
    """
    Just testing the CMD line Menu
    """
    SystemMenuTest().screen()