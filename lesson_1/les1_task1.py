"""Lesson 1 task 1"""
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

myName = 'Aleksey'
print(myName)

userChars = input('Введите число либо текст: ')
print(f'number_1: {userChars} {type(userChars)}')

userNumber = int(input('Введите число: '))
print(f'number_1: {userNumber} {type(userNumber)}')
