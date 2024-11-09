class Vars:
    def __init__(self):
        self.__output_file = './out/transactions.txt'


    @property
    def output_file(self):
        return self.__output_file