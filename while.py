# n = int(input("enter a number"))
# i=1
# sum=0
# while(i<=n):
#     sum+=1
#     i+=1

# print(sum)

# n = int(input("enter a number"))
# fact = 1
# for i in range(1,n):
#     fact = fact*i

# print(f"the factorial of {n} is {fact}")

n=int(input("enter number of rows"))
for i in range (1, n+1):
    print(" "*(n-i), end="")
    print ("*"*(2*i-1), end=" ")
    print(" ")