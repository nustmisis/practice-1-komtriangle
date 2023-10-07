# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = input()
height = input()

# Ваш кол

error = ""

if not weight.isnumeric():
    error = "Вес должен быть числом"

if not height.isnumeric():
    error = "Рост должен быть числом"

if error != "":
    print(error)

else:
    weight = int(weight)
    height = int(height)

    if weight <= 0:
        error = "вес должен быть больше нуля"

    if height <= 0:
        error = "рост должен быть больше нуля"

    if error == "":
        print(f"BMI: {weight/height**2}")
    else:
        print(error)
