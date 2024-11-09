class Transaction:
    def __init__(self, ttype, value, description):
        self.__type = ttype
        self.__value = value
        self.__description = description


    def save(self, db):
        db.save_transaction(self.__type, self.__value, self.__description)


    def view(self):
        print(f'Operation: {self.__type} - Value: {self.__value} - Description: {self.__description}')