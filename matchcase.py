# num = int(input("num: "))

# match num:
#     case 1:
#         print("one")

#     case 2:
#         print("two")

#     case 3:
#         print("three")

#     case _:
#         print("some other number")
#         print("exit the program")

day = input("enter name of the day")

match day:
    case "monday":
        print("yeahh its monday")

    case "friday":
        print("its near to weekend")

    case "saturday" | "sunday" :
        print("its jolidayy")

    case _:
        print("its another day of week")