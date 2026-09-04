# import math

# math.sqrt(25)

# import wikipedia
# print(wikipedia.summary("sanjana"))

# from currency_converter import CurrencyConverter

# c = CurrencyConverter()
# amt = float(input("enter a amount"))
# new_amt = c.convert(1, "USD", "INR", date=(2013,3,21))
# print(f"amount in INR:{new_amt} ")


import qrcode
image = qrcode.make("https://www.linkedin.com/in/sanjana-j-halemani-86394833")

image.save("eik_qr.png")

print("qr code generated successfully")
