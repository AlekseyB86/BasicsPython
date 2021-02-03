"""Lesson 1 task 4"""

userNumber = int(input('Введите целое число: '))
maxNumeral = 0
while userNumber != 0:
    # maxNumeral = userNumber % 10 if maxNumeral < userNumber % 10 else maxNumeral
    if maxNumeral < userNumber % 10:
        maxNumeral = userNumber % 10
    userNumber = userNumber // 10
print(maxNumeral)
