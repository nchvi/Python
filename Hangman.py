
from random import *
from time import sleep

word_list = []
with open(r'C:\Users\nchvikhovskiy\Desktop\word_rus.txt', encoding='utf8') as file:
    for line in file:
        word_list.append(line.strip())

def get_word():
    result = choice(word_list).upper()
    lenth = len(result)
    return result
def check_letters(n, used):
    while True:
        if not n.isalpha():
            n = input('Введите букву:  ')
            continue
        elif len(n) > 1:
            print('Нельзя вводить больше 1 символа')
            n = input('Введите одну букву:  ')
            continue
        elif n in used:
            print('Вы уже называли эту букву, введите другую')
            n = input('Введите другую букву:  ')
            continue
        elif n not in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяёЁ':
            print('Сейчас игра поддерживает только русский язык')
            n = input('Введите другую букву:  ')
            continue
        elif n == 'ё':
            print('В наших словах нет буквы Ё, вместо нее введите Е')
            n = input('Введите букву Е:  ')
            continue
        else:
            return n
def check_answers(n):
    while True:
        if n == 'да' or n == 'нет':
            return n
        else:
            n = input('Введите "Да" или "Нет":  ')
            continue


stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/   --- отпевание состоится в четверг в 10 утра ---
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -    --- все, последняя попытка, больше нет времени шутить!! ---
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -     --- уже все тело и обе руки... мне очень страшно ---
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -     --- я верю в тебя! наверное.. ---
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -     --- появилось тело... ты же победишь? ---
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     --- ну.. пока только голова, так что все нормально ---
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     --- пока все хорошо, тут никого нет ---
                   -
                '''
    ]


print('Давай сыграем в Висельницу! Всего есть 6 попыток угадать слово')
print()
sleep(1)

def game():
    while True:
        sleep(1)
        a = get_word()
        secret = list()
        for _ in range(len(a)):
            secret.append('―')
        print(*secret)
        tries = 6
        used = ''
        while True:
            guess = input('Введите букву:  ').upper()
            guess = check_letters(guess, used)
            used += guess
            counter = 0
            for i in range(len(a)):
                if a[i] == guess:
                    secret.pop(i)
                    secret.insert(i, guess)
                    counter += 1
            if counter == 0:
                tries -= 1
                print('Такой буквы нет, еще осталось:', tries, 'попыток')
                print(stages[tries])
                print(*secret)
            else:
                print('Такая буква есть, еще осталось:', tries, 'попыток')
                print(stages[tries])
                print(*secret)
            if '―' in secret and tries > 0:
                continue
            else:
                break
        if '―' in secret:
            print('К сожалению, вы проиграли:(\nЗагаданное слово было ―', a)
        else:
            print('Ура! Вы выиграли!')
        new_game = input('Хотите еще раз?:  ').lower()
        new_game = check_answers(new_game)
        used = ''
        if new_game == 'да':
            continue
        else:
            print('До новых встреч!')
            break

game()
