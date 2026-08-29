def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a * b



# a = int(input("enter a number"))
# b = int(input("enter second number"))
def display_menu():
    print("simple calculator")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. quite")


while(True):
    display_menu()
    choice = int(input("enter your choice: "))
    print("you entered ", choice)

    if choice == 1:
        a = int(input("enter a number"))
        b = int(input("enter second number"))
        print("result: ", add(a , b))

    elif choice == 2:
        a = int(input("enter a number"))
        b = int(input("enter second number"))
        print("result: ", sub(a,b))

    elif choice == 3:
        a = int(input("enter a number"))
        b = int(input("enter second number"))
        print("result: ", mul(a , b))

    elif choice == 4 :
        print("exit from the calculator")
        break

else:
    print("invalid choice ....tru next time")
