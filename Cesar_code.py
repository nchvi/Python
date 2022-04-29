
print('Привет! Эта программа поможет расшифровать шифр Цезаря на русском и английском языке!')

russian_alph ='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
c_russian_alph = int(len(russian_alph) / 2)
english_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
c_english_alph = int(len(english_alph) / 2)

def check_ans(n):
    while True:
        if n == 'шифруем' or n == 'расшифровываем' or n == 'rus' or n == 'eng':
            return n
        else:
            n = input('Введите корректный ответ:  ')
            continue
def check_dig(n):
    while True:
        try: # Проверяем, можно ли введенное значение представить как integer
            n = int(n)
        except ValueError: # Если нельзя, то будет ошибка - обрабатываем
            n = input('Введите число:  ') # Запрашиваем ввод еще раз и повторяем цикл
            continue
        return n

def check_language(txt):
    while True:
        rus_count = 0
        eng_count = 0
        for i in range(len(txt)):
            if txt[i] in russian_alph:
                rus_count += 1
            if txt[i] in english_alph:
                eng_count += 1
        if rus_count > 0 and eng_count > 0:
            print('К сожалению, пока нельзя вводить символы на двух языках сразу. Повторите попытку ввода только на одном языке')
            txt = input('Введите текст:  ')
            continue
        if rus_count == 0 and eng_count == 0:
            print('Введен текст, в котором нет буквенных символов. Введите текст и повторите попытку')
            txt = input('Введите текст:  ')
            continue
        elif rus_count > 0 and eng_count == 0:
            return 'rus'
        elif rus_count == 0 and eng_count > 0:
            return 'eng'

direction = input('Нужно зашифровать текст или расшифровать? Введите "шифруем" или "расшифровываем":  ').lower().strip()
direction = check_ans(direction)
print('Программа работает на двух языках: русский и английский. Просто введите текст, язык распознается автоматически')
txt = input('Введите текст:  ')
language = check_language(txt)
print('language:', language )
step = input('Введите числовое значение шага сдвига:  ')
step = check_dig(step)

res = ''

def prog(res):
    if direction == 'шифруем':
        if language == 'eng':
            for i in range(len(txt)):
                if txt[i].isalpha():
                    if ord('A') <= ord(txt[i]) <= ord('Z'):
                        if (ord(txt[i]) + (step % c_english_alph)) > 90:
                            res = res + chr((ord(txt[i]) + (step % c_english_alph)) - 26)
                        else:
                            res = res + chr((ord(txt[i]) + (step % c_english_alph)))
                    else:
                        if (ord(txt[i]) + (step % c_english_alph)) > 122:
                            res = res + chr((ord(txt[i]) + (step % c_english_alph)) - 26)
                        else:
                            res = res + chr((ord(txt[i]) + (step % c_english_alph)))
                else:
                    res = res + txt[i]
            print(res)
        if language == 'rus':
            for i in range(len(txt)):
                if txt[i].isalpha():
                    if ord('А') <= ord(txt[i]) <= ord('Я'):
                        if (ord(txt[i]) + (step % c_russian_alph)) > 1071:
                            res = res + chr((ord(txt[i]) + (step % c_russian_alph)) - 32)
                        else:
                            res = res + chr((ord(txt[i]) + (step % c_russian_alph)))
                    else:
                        if (ord(txt[i]) + (step % c_russian_alph)) > 1103:
                            res = res + chr((ord(txt[i]) + (step % c_russian_alph)) - 32)
                        else:
                            res = res + chr((ord(txt[i]) + (step % c_russian_alph)))
                else:
                    res = res + txt[i]
            print(res)

    if direction == 'расшифровываем':
        if language == 'eng':
            for i in range(len(txt)):
                if txt[i].isalpha():
                    if ord('A') <= ord(txt[i]) <= ord('Z'):
                        if (ord(txt[i]) - (step % c_english_alph)) < 65:
                            res = res + chr((ord(txt[i]) - (step % c_english_alph)) + 26)
                        else:
                            res = res + chr((ord(txt[i]) - (step % c_english_alph)))
                    else:
                        if (ord(txt[i]) - (step % c_english_alph)) < 97:
                            res = res + chr((ord(txt[i]) - (step % c_english_alph)) + 26)
                        else:
                            res = res + chr((ord(txt[i]) - (step % c_english_alph)))
                else:
                    res = res + txt[i]
            print(res)
        if language == 'rus':
            for i in range(len(txt)):
                if txt[i].isalpha():
                    if ord('А') <= ord(txt[i]) <= ord('Я'):
                        if (ord(txt[i]) - (step % c_russian_alph)) < 1040:
                            res = res + chr((ord(txt[i]) - (step % c_russian_alph)) + 32)
                        else:
                            res = res + chr((ord(txt[i]) - (step % c_russian_alph)))
                    else:
                        if (ord(txt[i]) - (step % c_russian_alph)) < 1072:
                            res = res + chr((ord(txt[i]) - (step % c_russian_alph)) + 32)
                        else:
                            res = res + chr((ord(txt[i]) - (step % c_russian_alph)))
                else:
                    res = res + txt[i]
            print(res)
prog(res)
