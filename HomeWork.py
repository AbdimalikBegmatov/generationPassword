'''
Напишите функцию, которая будет генерировать случайный пароль. В пароле должно быть от 7 до 10 символов, при этом каждый символ должен
быть случайным образом выбран из диапазона от 33 до 126 в таблице
ASCII. Ваша функция не должна принимать на вход параметры, а возвращать будет сгенерированный пароль. В основной программе вы должны
просто вывести созданный случайным образом пароль. Программа должна запускаться только в том случае, если она не импортирована в виде
модуля в другой файл.



Добавте файлы ДЗ в github репозиторий, и отправьте мне ссылку
'''

import random

countOfSymbols=int(input("Сколько символов хотите сгенерировать:"))

def generatePassword():
    res=""
    for i in range(countOfSymbols):
        r=random.randrange(33,126)
        res+=chr(r)
    return res

password = generatePassword()

print(f"Generated password= {password}")
