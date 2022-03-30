import random

chars = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

number = int(input("Количество паролей?:"))
length = int(input("Длина пароля?:"))

for x in range(number):
    password = " "

    for i in range(length):
        password += random.choice(chars)
    print(password)

    file = open("password1.txt", "a")
    file.write("\n" + password)
    file.close()