import random

name = input("Привет, как тебя зовут: ")
x = int(input("Введи количество символов в пароле:"))

print("Ну, {0} держи свой пароль".format(name))
print(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(x)])) # В ОДНУ СТРОКУ