a = 10
b = 0
print(a/b)

a = int(input("a "))
b = int(input("b "))

print(a/b)

try:
    print(a/b)
except Exception as e :
    print(f"error: {e}")
    b = int(input("b: "))
    print(a/b)

else:
    print("no error")
finally:
    print("i dont care")
    print("programm is ended")

try:
    num = int(input("enter a numbrer"))
    result = 10/num

except ZeroDivisionError:
    print("it is cannot divide by zero")
except ValueError:
    print("please enter a valid number")

try:
    boy = input("who do you want to love")
    if boy.lower() != "chandan":
        raise Exception("you can love only him not others")

except Exception as e:
    print(f"error: {e}")