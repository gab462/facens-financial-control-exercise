class Database:
    def __init__(self, output_file):
        self.__output_file = output_file


    def save_transaction(self, ttype, value, description):
        with open(self.__output_file, 'a+') as file:
            file.write(f'Operation: {ttype} - Value: {value} - Description: {description}\n')


    def get_all_transactions(self):
        with open(self.__output_file, 'r') as file:
            return [line[:-1] for line in file.readlines()]