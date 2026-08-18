# import random
# 1 = snake 
# 2 = water 
# 3 = gun 

# computer = random.choice([1,2,3])
computer = 1
youstr = input("enter ur choice ")
dict = {"1":1, "2":2, "3":3}
me = dict[youstr]

# if(computer== 1 and me ==2): -1
#     print("computer won the match")

# elif(computer== 1 and me ==3):-2
#     print("you won the match")

# elif(computer== 2 and me ==1):1
#     print("you won the match")

# elif(computer== 2 and me ==3):-1
#     print("you loos the match")

# elif(computer== 3 and me ==1):-2
#     print("you loose the match")

# elif(computer== 3 and me ==2):1
#     print("you won the match")
# else:
#     print("itss draw")
if(computer==me):
    print("phh itzz draww")

else:
     if(computer - me)== 1 or (computer - me) ==-2:
        
            print("you won")
     else:
            print("you lost")
    