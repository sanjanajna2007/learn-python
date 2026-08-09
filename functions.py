        #  functionsss
         
def func1(name, ending="thank youuuu"):
    print(f"hello,{ name}")
    print(ending)
func1("sanjana")

            #   recurssion

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(f"factorial of {n} is", fact)
fact(5)