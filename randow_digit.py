
### Добавить возможность указания правой границы для случайного выбора числа (от 111 до nnn). - не в цикле


from random import *
from time import sleep

print('Добро пожаловать в числовую угадайку')
sleep(1)
print('Выберете диапазон значений, в котором будете угадывать числа')
sleep(1)
start_range = int(input('Введите начальное значение:   '))
end_range = int(input('Введите конечное значение:   '))
if start_range > end_range:
    start_range, end_range = end_range, start_range

def check(s):
    while True:
        if s.isdigit() and start_range <= int(s) <= end_range:
            s = int(s)
            break
        else:
            print('А может быть все-таки введем целое число от', start_range, 'до',  end_range, '?')
            s = input()
    return s


def game():
    while True:
        n = randint(start_range, end_range)
        print('Введите число от', start_range, 'до',  end_range)
        s = check(input())
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
        print('Вы угадали, поздравляем!, вам потребовалось', counter, 'попыток, чтобы угадать число!')
        counter = 1
        sleep(1)
        new_game = input('Хотите сыграть еще раз? Введите "Да" или "Нет":  ').lower()
        while True:
            if new_game == 'да' or new_game == 'нет':
                break
            else:
                new_game = input('Введите "Да" или "Нет":  ')
                sleep(1)
        if new_game == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        else:
            continue

game()


