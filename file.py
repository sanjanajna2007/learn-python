# f  = open("file1.txt","r")
# data = f.read()
# print(data)
# f.close

st = "heyyy amazing to meet ypu are u kidding soo sweet of you"
f = open("myfile.txt", "a")
f.write(st)
f.close

f = open("myfile.txt")
print(f.read())
f.close()

with open("myfile.txt") as f:
    print(f.read())

    # no need to close the file

    f = open("myfile.txt")
    content = f.read()
    if("kidding" in content):
        print("yes this is correct file")

    else:
        print("this is not correct file")
    f.close()