"""Lesson 1 task 2"""
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

userNumber = int(input('Введите время в секундах: '))
seconds = userNumber % 60
minutes = (userNumber // 60) % 60
hours = (userNumber // 3600) % 24
print(f"{hours}:{minutes}:{seconds}")
