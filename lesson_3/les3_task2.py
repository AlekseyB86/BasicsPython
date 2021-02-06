"""lesson_3 task_2"""


# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def personal_date(**kwargs):
    result = []
    for arg in kwargs.values():
        result.append(str(arg))
    return " ".join(result)


print(personal_date(name="Сидр", surname="Сидоров", year_birth=1958,
                    city="Гуляй-Борисовка", email="tutu@mail.ru", tel=89168887766))
