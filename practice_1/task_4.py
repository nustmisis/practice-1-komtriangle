# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четыхрехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""

number = int(input())

if number < 1000 or number > 9999:
    print("Число должно быть четырехзначным")
else:
    sum = sum([(number//10**(i)) % 10 for i in range(4)])
    print(sum)
