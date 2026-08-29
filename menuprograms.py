# def add(a, b):
#     return a+b

# def sub(a, b):
#     return a-b

# def mul(a, b):
#     return a * b

# # a = int(input("enter a number"))
# # b = int(input("enter second number"))
# def display_menu():
#     print("simple calculator")
#     print("1. add")
#     print("2. subtract")
#     print("3. multiply")
#     print("4. quite")

# while(True):
#     display_menu()
#     choice = int(input("enter your choice: "))
#     print("you entered ", choice)

#     if choice == 1:
#         a = int(input("enter a number"))
#         b = int(input("enter second number"))
#         print("result: ", add(a , b))

#     elif choice == 2:
#         a = int(input("enter a number"))
#         b = int(input("enter second number"))
#         print("result: ", sub(a,b))

#     elif choice == 3:
#         a = int(input("enter a number"))
#         b = int(input("enter second number"))
#         print("result: ", mul(a , b))

#     elif choice == 4 :
#         print("exit from the calculator")
#         break

# else:
#     print("invalid choice ....tru next time")

def menu():
    print("banking system")
    print("1. check balance")
    print("2. deposite")
    print("3. withdraw")
    print("4. quite")

balance = 0

while True:
    menu()
    choice = int(input("enter your choice"))
    if choice == 1:
        print("blance", balance)

    elif choice == 2:
        amount = int(input("enter amount to deposite"))
        balance += amount

    elif choice == 3:
        amount = int(input("enter amount to withdrae"))
        balance -= amount

    elif choice == 4:
        print("thank you for using our banking system")

    else:
        print("quitting")

      

        

