"""lesson_4 task_3"""
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
num_1, num_2 = 20, 240
print([el for el in range(num_1, num_2 + 1) if el % 20 == 0 or el % 21 == 0])
