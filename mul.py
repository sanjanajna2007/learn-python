# def multiplication(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} * {i} = {n*i}\n"

#     with open(f"table.txt{n}", "w") as f:
#         f.write(table)

# for i in range(2, 21):

#     multiplication(i)

words = ["donkey", "lorem", "gunga"]

with open("highscore.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))

with open("highscore.txt", "w") as f:
    f.write(content)