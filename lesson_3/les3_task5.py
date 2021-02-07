"""lesson_3 task_5"""


# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.
def is_number(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return 0


summa = 0
char_s = '!'
flag = True
while flag:
    if summa != 0: print(f"Сумма чисел: {summa}")
    numbers = input("Введите ещё числа через пробел: ")
    numbers = numbers.split(" ")
    for i in numbers:
        if char_s not in i:
            i = is_number(i)
            summa += i
        else:
            i = i.split(char_s)
            i = is_number(i[0])
            summa += i
            print(f"Сумма чисел: {summa}")
            print("Программа завершена!")
            flag = False
            break
