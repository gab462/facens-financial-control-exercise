from config.vars import Vars
from utils.db import Database
from models.transaction import Transaction


def show_menu():
    print(32 * '-')
    print('| Welcome to Financial Control |')
    print('| 1 - Transact                 |')
    print('| 2 - View transactions        |')
    print('| 3 - Exit                     |')
    print(32 * '-')


def get_option():
    option = input('Choose one of the options: ')

    if option not in ['1', '2', '3']:
        print('Invalid Option.')

    return option


def finish():
    print('Thank you for your service.')


class App:
    def __init__(self, db):
        self.__db = db


    def transact(self):
        operation = input('Choose type of operation: ')
        value = input('Choose the value: ')
        description = input('Add a description: ')

        Transaction(operation, value, description).save(self.__db)


    def view(self):
        for line in self.__db.get_all_transactions():
            print(line)


def main():
    app = App(Database(Vars().output_file))

    option = ''

    while option != '3':
        show_menu()

        option = get_option()

        if option == '1':
            app.transact()
        elif option == '2':
            app.view()
        elif option == '3':
            finish()


if __name__ == '__main__':
    main()