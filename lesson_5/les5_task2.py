"""lesson5 task2"""
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("text2.txt", "r+", encoding="utf-8") as f_obj:
    text = "Неудачи есть всегда. Если у вас нет неудач, значит вы недостаточно инновационны.\n" \
           "Терпение — это добродетель, и я учусь быть терпеливым. Но это трудные уроки.\n" \
           "Я хочу быть частью того, что меняет мир.\n" \
           "Ошибки совершать не страшно. Главное каждый раз ошибаться в чем-то новом.\n" \
           "Главное — задать правильный вопрос. Все дело в вопросах."
    print(text, file=f_obj)
    f_obj.seek(0)
    content = [line.strip().split() for line in f_obj]
new_content = []
for stroke in range(len(content)):
    new_stroke = [el for el in content[stroke] if len(el) > 1 or el.isalpha()]
    new_content.append(new_stroke)
for stroke, el in enumerate(new_content):
    print(f"{stroke + 1} строка кол-во слов: {len(el)}")
