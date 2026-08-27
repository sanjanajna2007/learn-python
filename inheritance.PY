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


child = ("halemani", "sanju")
print(f"{child.name} {child.surname}")

grandchild = ("halemani", "deepak","deepu")

print(f"{grandchild.name} |{grandchild.surname}, {grandchild.cutename}")