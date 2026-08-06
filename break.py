# l = [1,4,7]
# for item in l:
#     print(item)

# else:
#     print("what the fahhh")


# s1 = "sanjana "
# s2 = "halemani"
# s = s1+s2
# print(s)

# for i in range(100):
#     if(i==10):
#         break
#     print(i)

# for i in range(100):
#     if(i==10):
#         continue
#     print(i)

# n = int(input("enter number"))

# for i in range (1,21):
#     print(f"{n} * {i} = {n*i}")

l = ["sanju", "goutam", "sachin"]
for name in l :
    if (name.startswith("s")):
       
        print(f"hello {name}")

    if (name.endswith("m")):
        print(f"hii {name}" )

n = int(input("enter a number "))
for i in range(2, n):
    if(n%i) == 0:
        print("number is not prime")
        break
    else:
        print("entered number is prime")