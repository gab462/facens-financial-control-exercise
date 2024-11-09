class Database:
    def __init__(self):
        self.__transactions = []


    def show_menu(self):
        print(32 * '-')
        print('| Welcome to Financial Control |')
        print('| 1 - Transact                 |')
        print('| 2 - View transactions        |')
        print('| 3 - Exit                     |')
        print(32 * '-')


    def get_option(self):
        option = input('Choose one of the options: ')

        if option not in ['1', '2', '3']:
            print('Invalid Option.')

        return option


    def transact(self):
        operation = input('Choose type of operation: ')
        value = input('Choose the value: ')
        description = input('Add a description: ')

        self.__transactions.append((operation, value, description))


    def view(self):
        for op, v, desc in self.__transactions:
            print(f'Operation: {op} - Value: {v} - Description: {desc}')


    def exit(self):
        print('Thank you for your service.')


def main():
    db = Database()

    option = ''

    while option != '3':
        db.show_menu()

        option = db.get_option()

        if option == '1':
            db.transact()
        elif option == '2':
            db.view()
        elif option == '3':
            db.exit()


if __name__ == '__main__':
    main()