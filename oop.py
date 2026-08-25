class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)

cbi = ATM(1000)

print(cbi.check_balance)