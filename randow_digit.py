
from random import *
n = randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def check(s):
    while True:
        if s.isdigit() and 1 <= int(s) <= 100:
            s = int(s)
            break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            s = input('Введите число от 1 до 100:  ')
    return s


s = check(input('Введите число от 1 до 100:  '))
counter = 1
while s != n:
    if s < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        s = check(input())
        counter += 1
        continue
    elif s > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        s = check(input())
        counter += 1
        continue
counter = 1
print('Вы угадали, поздравляем!, вам потребовалось', counter, 'попыток, чтобы угадать число!')

next_try = input('Хотите сыграть еще раз? Введите "Да" или "Нет":   ').lower()
while True:
    if next_try != 'Да' or next_try != 'Нет':
        next_try = input('Введите "Да" или "Нет":   ').lower()
    else:
        break

if next_try == 'Да':
    ### вызов функции еще раз


print('Спасибо, что играли в числовую угадайку. Еще увидимся...')