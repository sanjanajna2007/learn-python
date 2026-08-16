# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("enter a number"))
# print(f"{f_to_c} *c")

# def pattern(n):
#     if (n==0 or n==1):
#         return 
#     print("*" * n)
#     pattern(n-1)

# pattern (6)

# def inch_to_cm(i):
#     return i * 2.54

# n = int(input("enter a value"))
# print(f"the converted value in cms {inch_to_cm(n)}")

def rem(l, word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["harry", "sanju", "an" ,"shuban"]
print(rem(l, "sa"))












