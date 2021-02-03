"""Lesson 1 task 5"""
# Запросить у пользователя значения выручки и издержек фирмы.
# Определить, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Вывод соответствующего сообщения.
# Если фирма отработала с прибылью, вычислить рентабельность выручки (соотношение прибыли к выручке).
# Далее запросить численность сотрудников фирмы и определить прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input('Введите значение выручки фирмы: '))
costs = float(input('Введите значение издержек фирмы: '))
numEmployees = int(input('Введите кол-во сотрудников в фирме: '))
profit = proceeds - costs
if profit > 0:
    print(f'Фирма отработала в прибыль: + {profit:.2f}')
    print(f'Рентабельность выручки составляет {profit/proceeds:.2f}')
    while numEmployees <= 0:
        print('Необходимо число больше 0, попробуйте ещё раз!')
        numEmployees = int(input('Кол-во сотрудников в фирме: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit/numEmployees:.2f}')
elif profit < 0:
    print(f'Фирма отработала в убыток: {proceeds - costs}')
else:
    print('Фирма сработала в 0')
