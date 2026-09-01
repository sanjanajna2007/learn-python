class account:
    def __init__(self, id, holder_name):
            self.id = id
            self.holder_name = holder_name
            self._balance = 0

    def check_balance(self):
        print(f"balance is {self._balance}")

    def deposite(self, amount):
        self._balance += amount
        print(f"deposit successfully and updated balance is: {self._balance}")

    def withdraw(self, amount):
         if self._balance >= amount:
              self._balance-= amount
              print(f"deposited successfully. updated balance is {self._balance}")


         else:
              print("alance cant be less than zero")


class savingaccount(account):

      def calculate_interest(self):
           INTEREST_RATE = 0.04
           interest = self._balance * INTEREST_RATE
           print(F"INTEREST : {interest}")
    

class currentaccount(account):
    def withdraw(self, amount):
         OVERDRAFT_LIMIT = 1000
         if self._balance + OVERDRAFT_LIMIT >= amount:
              self._balance -= amount
              print(f"withdraww successfully. updated balance is {self._balance}")
         else:
              print("balance is less than ask")

class bank:
     def __init__(self, name, city):
          self.name = name
          self.city = city
          self.__account = {}

     def create_account(self, id, holder_name, type):
          if type=="saving":
               new_account = savingaccount(id,holder_name)

          elif type=="current" :
               new_account = currentaccount(id,holder_name)

          else:
               print("invalid account typre")
               return None    
          self.__account[id] = new_account
          print("account creation successfully")
          return new_account

     def get_account(self, id):
          if id not in self.__account:
               print("account is not found")
               return None
          else:
               account = self.__account_[id]
               print(f"\n ID: {account.id}\n holder_name(account.holder_name)")
               return account

bankii = bank("karnataka grameena bank ingalahalli", "ingalahalli" )

s1 = bankii.create_account("11", "sanjana", "saving")
s2 = bankii.create_account("12", "chandan", "current")

s1.deposite(1000)
s2.deposite(10)

s1.withdraw(200)
s2.withdraw(500)

s1.check_balance()
s2.check_balance()
                                            
           
          
     