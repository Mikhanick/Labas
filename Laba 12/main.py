# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 12
# Варианты: Сложение и вычитание, удаление предложения, в котором наиболее количество слов начинается на заданную букву

from text import text
import math


def menu() -> str:  # меню, возвращает номер варианта ответа пользователя
    print('###################################')
    print('1. Выровнять текст по левому краю.')
    print('2. Выровнять текст по правому краю.')
    print('3. Выровнять текст по ширине.')
    print('4. Удаление всех вхождений заданного слова.')
    print('5. Замена одного слова другим во всём тексте.')
    print('6. Вычисление арифметических выражений над целыми числами внутри текста')
    print('7. Найти (вывести на экран) и затем удалить слово или предложение по варианту.')
    print('0. Выход из программы.')
    print('###############################################################################')
    inp = input().strip()
    while not (
            inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6' or
            inp == '7' or inp == '0'):
        print('Некорректный ввод, повторите попытку')
        inp = input()
    return inp


def to_left(text: list[str]) -> list[str]:  # выравнивание текста по левому краю
    for line in range(len(text)):
        text[line] = ' '.join(text[line].split())
    return text


def to_right(text: list[str]) -> list[str]:  # выравнивание текста по правому краю
    ln = [len(i) for i in text]
    linemx = max(ln)
    for line in range(len(text)):
        text[line] = ' ' * (linemx - ln[line]) + text[line]
    return text


def to_wide(text: list[str]) -> list[str]:  # выравнивание текста по ширине
    text = to_left(text)
    ln = max([len(i) for i in text])
    for line in range(len(text)):
        delta = ln - len(text[line].replace(' ', ''))
        k = delta // (max(len(text[line].split()) - 1, 1))
        space = ' ' * max(1, k)
        text[line] = space.join(text[line].split())
        for word in text[line].split():
            if len(text[line]) == ln:
                break
            text[line] = text[line].replace(word, word + ' ', 1)

    return text


def to_mid(text: list[str]) -> list[str]:  # выравнивание текста по центру, в программе не используется
    ln = [len(i) for i in text]
    linemx = max(ln)
    for line in range(len(text)):
        text[line] = ' ' * (math.ceil((linemx - ln[line]) / 2)) + text[line]
    return text


def delete_word(text: list[str]) -> list[str]:  # удаление слова -- в моей программе это вызов замены слова,
    # но как аргумент нового слова -- пустая строка
    word = input('Введите слово, которое следует удалить: ').strip()
    print()
    while len(word) == 0:
        print('Вы не ввели слово')
        word = input('Введите слово, которое следует удалить: ').strip()

    flag = 0
    for line in range(len(text)):
        text[line], cnt = replace_word_by_index(text[line], word, '')
        flag += cnt
    if not flag:
        print(f'Слово "{word}" не было обнаружено')
    else:
        print(f'Удалено {flag} слов')
    return text


def analyze_text(text: list[str]) -> list[str]:  # подпрограмма, убирающая пробелы между словами и
    # небуквенными символами, повторяющиеся небуквенные символы и пустые строки
    letters = ('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю'
               'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёЁ01234567890')

    change = 1
    while change:  # пока есть изменения в тексте повторяем
        change = 0
        for line in range(len(text)):
            if text[line] == '' or set(text[line]) == set(' '):
                text.pop(line)
                change = 1
                break
            # print('найдена пустая строка')

        for line in range(len(text)):
            # print("обработка", line,"строки")
            for sym in range(len(text[line]) - 1):
                a = text[line][sym]
                b = text[line][sym + 1]
                if sym != 0 and sym != (len(text[line]) - 2) and (
                        (text[line][sym - 1] == a == b == '!') != (a == b == text[line][sym + 2] == '!')):
                    # если заметили 3 восклицательных знака то пропускаем их
                    # print(text[line][sym-2:sym+3])
                    continue

                if a == b and a not in letters:
                    text[line] = text[line].replace(a + b, a, 1)
                    change = 1
                    # найдены совпадающие символы
                    break
                if a in '!?' and b not in letters and b not in '!? ':
                    text[line] = text[line][:sym + 1] + text[line][sym + 2:]
                    change = 1  # убираем запятые перед окончанием предложения
                    break
                if a not in letters and not (a == '?' and b == '!') and (b == '.' or b == '!' or b == '?'):
                    text[line] = text[line][:sym] + text[line][sym + 1:]
                    change = 1
                    break
            for sym in range(len(text[line]) - 2):
                a = text[line][sym]
                b = text[line][sym + 1]
                c = text[line][sym + 2]
                if a in letters and b == ' ' and c not in letters and c not in "-+":
                    text[line] = text[line][:sym + 1] + text[line][sym + 2:]
                    change = 1
                    # убираем лишний пробел
                    break
    return text


def count_expression(expression: str) -> str:  # считаем выражение, которое поступает на вход
    # print(expression)
    if '+' in expression:
        return str(sum(map(int, expression.split('+'))))
    else:
        if expression.count('-') == 0 or expression[0] == '-' and expression.count("-") == 1:
            return expression
        elif expression.count('-') == 1:
            num1, num2 = (map(int, expression.split('-')))
            return str(num1 - num2)
        else:
            return str(int(expression[:expression.rfind('-')]) - int(expression[expression.rfind('-') + 1:]))


def search_arithmetic(line: str) -> list[list[str]]:  # поиск арифметических операций
    expression = ''
    flag_to_count = 0
    start = -1
    expressions_to_replace = []
    for index, sym in enumerate(line):
        if sym in '-1234567890' and expression == '':  # ищем начало арифметического выражения
            expression += sym
            start = index
        elif sym == ' ' and (line[max(0, index - 1)] in "1234567890" and line[min(len(line) - 1, index + 1)] in '-+' or
                             line[min(len(line) - 1, index + 1)] in '1234567890' and line[max(0, index - 1)] in '-+' or
                             line[min(len(line) - 1, index + 1)] in '+-' and line[max(0, index - 1)] in '-+'):
            pass  # если один пробел между числом и знаком – то он не влияет
        elif sym in '1234567890':
            expression += sym  # если символ цифра – то добавляем
        elif sym == '-' and expression[-1] == '+':  # если есть +- то все хорошо, добавляем
            expression += sym
        elif sym in '-+' and expression != '' and expression[-1] in '1234567890':  # если новый символ
            # это знак + или - то добавляем, и если знак уже был в выражении то считаем выражение и потом добавляем
            # знак к выражению
            if flag_to_count:
                expression = count_expression(expression)
                expression += sym
            else:
                expression += sym
            flag_to_count = 1
        else:  # если ни один из вышеупомянутых случаев, то считаем непустую последовательность
            # и потом добавляем массив,
            # который идет на замену в строке
            # если последовательность пустая то ничего не делим, если состоит только из знака то удаляем знак
            new_expression = ''
            sym_left = 0
            if expression != '' and (expression[-1] == '-' or expression[-1] == '+'):
                if expression == '-':
                    new_expression += expression[-1]
                expression = expression[:-1]
                sym_left += 1

            if expression != '' and expression[0] == '+':
                expression = expression[1:]
                sym_left += 1
            if expression != '':
                expression = count_expression(expression)
                if line[start:index - sym_left - 1] != expression:
                    expressions_to_replace.append([line[start:index - sym_left].strip(), expression])
                if sym in '-1234567890' and expression == '':
                    expression += sym
                    start = index
                else:
                    expression = new_expression
    sym_left = 0  # по окончании строки то же самое, как когда встречаем неправильный символ
    if expression != '' and (expression[-1] == '-' or expression[-1] == '+'):
        expression = expression[:-1]
        sym_left += 1
    if expression != '' and expression[0] == '+':
        expression = expression[1:]
        sym_left += 1
    if expression != '':
        expression = count_expression(expression)
        if line[start:] != expression:
            expressions_to_replace.append([line[start:len(line) - sym_left], expression])
    return expressions_to_replace


def arithmetical(
        text: list[str]):  # программа подающая по отдельности строки на поиск арифметических операций и заменяющая
    cnt = 0
    for index in range(len(text)):
        for old, new in search_arithmetic(text[index]):
            # print(old,new)
            new_string = text[index].replace(old, new, 1)
            text[index] = new_string
            # print(text[index])
            cnt += 1
    print(f'Произведено {cnt} арифметических операций')
    return text


def replace_word(text: list[str]):  # функция по получению слов которые надо заменить и вызывающая функцию - обработчик
    # замены определенного слова по его индексу
    word = input('Введите слово, которое следует заменить: ').strip()
    while len(word) == 0:
        print('Вы не ввели слово')
        word = input('Введите слово, которое следует заменить: ').strip()
    new_word = input('Введите слово, которое следует вставить на место удаленного: ').strip()
    print()
    while len(new_word) == 0:
        print('Вы не ввели слово')
        new_word = input('Введите слово, которое следует вставить на место удаленного: ').strip()
    flag = 0

    for line in range(len(text)):  # заменяем и считаем количество замен
        text[line], cnt = replace_word_by_index(text[line], word, new_word)
        flag += cnt
    if not flag:
        print(f'Слово "{word}" не было обнаружено')
    else:
        print(f'Заменено {flag} слов')
    return text


def replace_word_by_index(line: str, word: str, new_word: str, start_index: int = 0) -> tuple[str, int]:
    pos = match_word_index(line, word,
                           start_index)  # заменяем слова, пересклеивая строку от индекса который получаем из
    # функции match_word_index и длинной со слова, далее идет строка которая шла после слова изначально
    cnt = 0
    while pos != -1:
        line = line[:pos] + new_word + line[pos + len(word):]
        pos = match_word_index(line, word, pos + len(new_word))
        cnt += 1
    return line, cnt


def match_word_index(line: str, word: str, index: int = 0) -> int:  # ищем индекс слова которое надо заменить
    if index == -1 or index > (len(line) - len(word)):
        # print("превышение")
        return -1
    # print("Поиск:", word)
    pos = line.find(word, index)
    if pos != -1:
        # print(pos, index, line)
        letters = ('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю'
                   'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёЁ-')

        if pos != 0 and line[pos - 1] in letters:
            # print("Что не удовлетворило спереди:"+line[pos-1])
            return match_word_index(line, word, pos + 1)
        if pos + len(word) < len(line) and line[pos + len(word)] in letters:
            # print("Что не удовлетворило после:"+line[pos + len(word)])
            return match_word_index(line, word, pos + 1)
        # print("Слово найдено:", pos)
        return pos
    else:
        # print('Слово не найдено в строке')
        return -1


def find_sentence(text: list[str]):
    # функция по обнаружению и удалению необходимого предложения
    interesting_sym = input('Введите символ, для поиска предложения в котором максимальное количество слов начинается'
                            'на этот символ: ')
    while len(interesting_sym) != 1:
        print('Вы ввели не один символ, повторите попытку!')
        interesting_sym = input()
    position_of_sentence = []
    k = 0
    max_k = 0
    start_of_this_sentence = [0, 0]
    for index_line, line in enumerate(text):
        for sym in range(1, len(line)):
            if line[sym - 1] == ' ' and line[sym] == interesting_sym:
                k += 1
            if line[sym - 1] == '.':
                if k > max_k:
                    position_of_sentence = [start_of_this_sentence, [index_line, sym]]
                    max_k = k
                k = 0
                start_of_this_sentence = [index_line, sym]  # ищем позицию начала и конца предложения с максимальным
                # количеством слов, начинающихся на заданную букву
    if not position_of_sentence:  # если не было найдено предложение ничего не делаем
        print('Необходимое предложение не найдено')
        return text

    else:  # выводим и вырезаем предложения удовлетворяющие условию
        print(f"В предложении найдено {max_k} слов на букву {interesting_sym}\n")
        for line in range(position_of_sentence[0][0], position_of_sentence[1][0] + 1):
            if line != position_of_sentence[0][0] and line != position_of_sentence[1][0]:
                print(text[line])
                text[line] = ''
            else:
                if position_of_sentence[0][0] == position_of_sentence[1][0]:
                    print(text[line][position_of_sentence[0][1]:position_of_sentence[1][1] + 1])
                    text[line] = text[line][:position_of_sentence[0][1]] + text[line][position_of_sentence[1][1] + 1:]
                elif line == position_of_sentence[0][0]:
                    print(text[line][position_of_sentence[0][1]:])
                    text[line] = text[line][:position_of_sentence[0][1]]
                else:
                    print(text[line][:position_of_sentence[1][1] + 1])
                    text[line] = text[line][position_of_sentence[1][1] + 1:]
        return text


def print_text(text: list[str]):  # вывод текста
    print()
    for line in text:
        print(line)
    print()


def main(text):  # тело программы
    text = analyze_text(text)
    if not text:
        print("Текст пуст, выполнение программы завершено.")
        return 0
    print_text(text)
    ans = menu()
    type_of_output = 1
    while ans != 0:
        if not text:
            print("Текст пуст, выполнение программы завершено.")
            return 0
        if ans == '1':
            type_of_output = 1
        if ans == '2':
            type_of_output = 2
        if ans == '3':
            type_of_output = 3
        if ans == '4':
            text = delete_word(text)
        if ans == '5':
            text = replace_word(text)
        if ans == '6':
            text = arithmetical(text)
        if ans == '7':
            text = find_sentence(text)
        if ans == '0':
            break
        text = analyze_text(text)
        if type_of_output == 1:
            print_text(to_left(text.copy()))
        elif type_of_output == 2:
            print_text(to_right(text.copy()))
        else:
            print_text(to_wide(text.copy()))
        ans = menu()

    print('Выход из программы')
    return 0


if __name__ == '__main__':
    main(text)
