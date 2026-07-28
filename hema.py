marks1 = int(input("enter a marks 1 "))
marks2 = int(input("enter a marks 2 "))
marks3 = int(input("enter a marks 3 "))

total_percentage = (marks1+ marks2 + marks3)/300*100
print(total_percentage)

if(total_percentage>=40):
    print("you are pass")

else:
    print("you are failed")