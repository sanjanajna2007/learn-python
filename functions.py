        #  functionsss
         
def func1(name, ending="thank youuuu"):
    print(f"hello,{ name}")
    print(ending)
func1("sanjana")

            #   recurssion

# def fact(n):
#     fact = 1

#     for i in range(1,n+1):
#         fact = fact*i
#     print(f"factorial of {n} is", fact)
# fact(5)

def fact(n):
    if (n==0 or n==1):
        return 1
    return n * fact(n-1)
n = int(input("enter a number"))
print(f"the factorial of this number is: {fact(n)}")

def greatest (a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
            return b
    elif(c>b and c>a):
            return c

    
    a=8
    b=7
    c=9

    print(greatest(a, b, c))