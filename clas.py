# class car:
#     def __init__(self,car_id,year,price_per_day, status = "available", rented_days = 2):
#         print("constructor is calling")
#         self.car_id = car_id
#         self.year = year
#         self.price_per_day = price_per_day
#         self.status = status
#         self.rented_days = rented_days

#     def display_details(self):
#         print(f"car_id: {self.car_id}, year: {self.year},price_per_day: {self.price_per_day},status: {self.status} ")

#     def update_status(self, new_status):
#         self.status = new_status
#         print(f"car{self.car_id} status_updated to {self.status}")

#     def calculate_rented_days(self):
#         total_price = self.price_per_day * self.rented_days
#         print(f"total rental price for {total_price}")


# car1 = car(1, 1969, 50) 
# car2 = car(2, 2000, 1200, 3 )

# car1.display_details()
# car2.calculate_rented_days()


# class employee:
#     language = "py"
#     sallary = 12000

# harry = employee()
# print(harry.language,harry.sallary )

class sanjana:
    def __init__(self,work,sallary=-1):
        print("yeah it is loaded")
        self.work = work
        self.sallary = sallary

    def show(self):
        print(f"{self.work} this is her work")
        print(f"{self.sallary} is this much")

s1 = sanjana("softwere developer", 100000)
s2 = sanjana("ml developer")

s1.show()
s2.show()
print(s1.work)

