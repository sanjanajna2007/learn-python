class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)

cbi = ATM(1000)

print(cbi.check_balance)


    #   creating te database

class database:
    def __init__(self):
        self.storage = {} #public
        self._storage = {} #protected
        self.__storage = {} #private

    def write(self, key, value):
        self.__storage[key] = value

    def read(self, key):
        if key in self.__storage:
           
            return self.__storage[key]

        else:
            print("db is not available")
         

db = database()
db.read( "subscribers")
db.write("subscribers", "10k")
print(db.storage)

db.read("name")

