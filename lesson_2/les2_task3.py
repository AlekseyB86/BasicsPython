"""lesson_2 task_3"""
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима,весна,лето,осень)
# Напишите решения через list и через dict.

# seasons = ['весна', 'лето', 'осень', 'зима']      # v list
seasons = {                                         # v dict
    0: 'весна',
    1: 'лето',
    2: 'осень',
    3: 'зима'
}
while True:
    month = input('Введите месяц в виде целого числа: ')
    if month.isdecimal() and (int(month) - 1) in range(12):
        break
if int(month) in range(3, 6):
    print(seasons[0])
elif int(month) in range(6, 9):
    print(seasons[1])
elif int(month) in range(9, 12):
    print(seasons[2])
else:
    print(seasons[3])
