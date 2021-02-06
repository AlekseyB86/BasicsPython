"""lesson_3 task_2"""


# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def personal_date(name, surname, year_birth, city, email, tel):
    try:
        int(year_birth)
        int(tel)
    except ValueError:
        return print("Ввели некорректные данные!\n"
                     "'год рождения' и 'телефон' - только цифры!")
    try:
        email.index('.') > email.index('@')
    except ValueError:
        return print(f"Ввели некорректную эл.почту: {email}")
    print(f'{surname} {name} {year_birth} г.р. '
          f'г.{city} email:{email} tel:{tel}')


personal_date(
    name="Сидр",
    surname="Сидоров",
    year_birth="1958",
    city="Гуляй-Борисовка",
    email="tutu@mail.ru",
    tel=89168887766,
)
