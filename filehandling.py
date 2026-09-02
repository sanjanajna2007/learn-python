with open("notes.txt", "w") as f:

    f.write("sanjana")
    content = f.readlines()
    print(content)


file = open("notes.txt", "w")
try:
    file.write("sanjana")
    file.write("weekend")
    file.write("heyyy")

except Exception as e:
    print(f"error: {e}")
  
finally:
    print("file closed")

