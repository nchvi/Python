from random import *
from time import sleep
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как вас зовут?:   ')
print('Привет,', name)


def choice():
    n = randint(0, len(answers)-1)
    return answers[n]


def game():
    while True:
        question = input('Введите вопрос, на который можно ответить "Да" или "Нет":   ')
        sleep(2)
        print(choice())
        sleep(1)
        new_try = input('Хотите сыграть еще раз? Введите "Да" или "Нет":   ').lower()
        while True:
            if new_try == 'да' or new_try == 'нет':
                break
            else:
                new_try = input('Введите "Да" или "Нет":   ')
                continue

        if new_try == 'да':
            continue
        else:
            print('Возвращайся если возникнут вопросы!')
            break

game()

