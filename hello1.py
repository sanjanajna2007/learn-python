d = {}
name = input("enter book name ")
lang = input("enter book language ")
d.update({name:lang})

name = input("enter book name ")
lang = input("enter book language ")
d.update({name:lang})
print(d)

            # conditional statements

age = 10

a = int(input("enter a age"))
if (a >=18) :
    print("ready to vote")

elif(a<0):
    print("dont enter negative age ")

elif(a==0):
    print("age cant equal to zero broo")

else:
    print("please come back next time");

print("end of the program")    
 
a1 = int(input("enter a number1"))
a2 = int(input("enter a number2"))
a3 = int(input("enter a number3"))
a4 = int(input("enter a number4"))

if(a1>a2 and a1>a3 and a1>a4 ):
    print("greatest number is a1  ")

elif(a2>a1 and a2>a3 and a2>a4):
     print("greatest number is a2 : ")
     
     
elif(a3>a1 and a3>a2 and a3>a4):
     print("greatest number is a3 : ")     

elif(a4>a1 and a4>a2 and a4>a3):
     print("greatest number is a4 : ") 

else :
     print("greatest number is not there")  
