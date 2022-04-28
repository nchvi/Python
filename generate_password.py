
from random import *

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
bad_symbols = 'il1Lo0O'

chars = ''

def check_letters(n):
    while True:
        if n == 'да' or n == 'нет':
            return n
        else:
            n = input('Введите "Да" или "Нет":  ')
            continue
def check_digits(n):
    while True:
        if n.isdigit() and int(n) > 0:
            return n
        else:
            n = input('Введите число больше нуля:  ')
            continue

numbers = input('Сколько паролей будет нужно сгенерировать?:  ').strip()
numbers = check_digits(numbers)
lenth = input('Введите длину пароля. Чем длиннее пароль, тем более безопасно:  ').strip()
lenth = check_digits(lenth)
with_dig = input('Включать ли цифры?. Введите "Да" или "Нет":  ').lower().strip()
with_dig = check_letters(with_dig)
with_low_case = input('Включать ли строчные буквы?. Введите "Да" или "Нет":  ').lower().strip()
with_low_case = check_letters(with_low_case)
with_big_case = input('Включать ли прописные буквы?. Введите "Да" или "Нет":  ').lower().strip()
with_big_case = check_letters(with_big_case)
with_symbols = input('Включать ли символы?. Введите "Да" или "Нет":  ').lower().strip()
with_symbols = check_letters(with_symbols)
with_bad_symbols = input('Включать ли неоднозначные символы? Их можно легко перепутать. Введите "Да" или "Нет":  ').lower().strip()
with_bad_symbols = check_letters(with_bad_symbols)

if  lenth == 0 or(with_dig == 'нет' and with_low_case == 'нет' and with_big_case == 'нет' and with_symbols == 'нет' and with_bad_symbols == 'нет'):
    print('К сожалению, нельзя подобрать пароль по введенным требованиям. Пожалуйста, повторите попытку с измененными параметрами')
else:
    if with_dig == 'да':
        chars += digits
    if with_low_case == 'да':
        chars += lowercase_letters
    if with_big_case == 'да':
        chars += uppercase_letters
    if with_symbols == 'да':
        chars += punctuation
    if with_bad_symbols == 'да':
        chars += bad_symbols

def generate_passwors(lenth, chars, numbers):
    for i in range(int(numbers)):
        for j in range(int(lenth)):
            print(choice(chars), end='')
        print()

generate_passwors(lenth,chars,numbers)
