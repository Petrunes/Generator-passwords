from random import randint as r
from os import system as s

chars = ("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM")

numbers = int(input("Введите количество символов в пароле"))

password = ""
for i in range(numbers):
    password = f"{password}{chars[r(1,len(chars)-1)]}"
print("Получите Ваш пароль:" + " " + password)

file = open("password.txt", "a")
file.write("\n" + password)
file.close()