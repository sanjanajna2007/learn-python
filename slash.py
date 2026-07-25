# name = input("enter your name")
# print(f"good morning {name}")
# print(name)

letter = "dear name, you are selected date"
print(letter.replace("name","sanjana").replace("date", "24 september 2029"))

letter = "dear sanjana\n\ti like the greetings\t\nthanks"
print(letter)

                #  listssssss

friends = ["sanzz", "aaaa", 123, "bol"]
print(friends)
friends[1] = "apple"
print(friends[1])   

friends.reverse()
print(friends)
friends.append("sanju")

print(friends)

l1 = [1,2,25,12,45,46]
# l1.insert(1, 22)
# l1.reverse()
l1.remove(2)
# print(l1.pop(2))
print(l1)

# f1 = input("enter fruits name")
# print(f1)

# marks = list(map(int, input("enter ma rks of subjects").split(",")))
# print(marks)
# marks.sort()
# print(marks)

l = [3,2,45]
total = sum(l)
print(total)

                #    tuplesss...........

a = (1,45,78,45,45,"sanzzz","helol")
# print(type(a))
# print(a)
no = a.count(45)
# print(no)
s = a.index(1)
# print(s)
# print(len(a))

tuple1 = (1,2,3)
tuple = (4,)

result = tuple1 + tuple
# print(result)


                # dictionary

marks = {
    "aa" : 100,
    "bb" : 200,
    "cc" : 24
}
print(marks, type(marks))
print(marks["aa"])
print(marks.keys())
print(marks.values())
marks.pop("aa")
print(marks)