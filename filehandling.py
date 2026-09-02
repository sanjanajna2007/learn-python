# file = open("notes.txt", "w")
# file.write("sanjana")
# content = file.readlines()
# print(content)
# file.close()

file = open("notes.txt", "w")
try:
    file.write("sanjana")
    file.write("weekend")
    file.write("heyyy")

except Exception as e:
    print(f"error: {e}")
  
finally:
    print("file closed")

