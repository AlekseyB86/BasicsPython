"""lesson_2 task_5"""
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
rating = [10, 8, 8, 7, 6, 6, 6, 5, 3, 3, 3, 3, 2, 1, 1, 1]
while True:
    user_Num = input("Введите новый элемент рейтинга (натуральное число): ")
    if user_Num.isdecimal():
        user_Num = int(user_Num)
        break
if user_Num > max(rating):
    rating.insert(0, user_Num)
elif user_Num < min(rating):
    rating.append(user_Num)
elif user_Num in rating:
    """v1"""
    rating.reverse()
    rating.insert(rating.index(user_Num), user_Num)
    rating.reverse()
    print(rating)
    """v2"""
    # new_list = []
    # rating_1 = rating[:rating.index(user_Num)]
    # print(rating_1)
    # rating_2 = rating[rating.index(user_Num):]
    # print(rating_2)
    # while user_Num in rating_2:
    #     new_list.append(rating_2.pop(rating_2.index(user_Num)))
    # new_list.append(user_Num)
    # print(new_list)
    # rating = rating_1 + new_list + rating_2
else:
    for i in range(len(rating)):
        if user_Num > rating[i]:
            rating.insert(i, user_Num)
            break
print(rating)
