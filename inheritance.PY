# class user:
#     def __init__(self,username):
#         self.username = username

#         def __login(self):
#             print(f"{self.username} is logged in")

# class admin(user):
#     def delete_user(self):
#         print("admin deleted he user")

# a = user("aaa")

# print(a.username)
# a.delete_user()

    #  types oof inheritance


class family:
    def __init__(self, surname):
        self.surname = surname

class child(family):
    def __init__(self, surname, name):
        super().__init__(surname)
        self.name = name

class grandchild(child):
    def __init__(self, surname, name, cutename):
        super().__init__(surname, name)
        self.cutename = cutename


child1 = child("halemani", "sanju")
print(f"{child1.name} {child1.surname}")

gc1 = grandchild("halemani", "deepak","deepu")

print(f"{gc1.name} |{gc1.surname}, {gc1.cutename}")

class calculate :
    def __init__(self, n):
        self.n = n

    def __add__(self,other):
        return self.n + other.n

calci1 = calculate(2)
calci2 = calculate(4)
print(calci1 + calci2)


class animal:
    def make_sound(self):
        print("anima is making sound")

class dog(animal):
    def make_sound(self):
        print("bark")

class cat(animal):
    def make_sound(self):
        print("meow")

animals = [dog(), cat()]
for animal in animals:
    animal.make_sound()