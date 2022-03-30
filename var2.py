import random

name = input("Привет, как тебя зовут: ")

print("Ну, {0} держи свой пароль".format(name))
print(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(16)])) # В ОДНУ СТРОКУ