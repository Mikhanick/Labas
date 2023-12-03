from text import text
import math


def menu():
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
    while not(inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6' or inp == '7' or inp == '0'):
        print('Некорректный ввод, повторите попытку')
        inp = input()
    return inp
def to_left(text):
    for line in range(len(text)):
        text[line] = ' '.join(text[line].split())
    return text


def to_right(text):
    ln = [len(i) for i in text]
    linemx = max(ln)
    for line in range(len(text)):
        text[line] = ' ' * (linemx - ln[line]) + text[line]
    return text


def to_wide(text: list[str]):
    ln = max([len(i) for i in text])
    for line in range(len(text)):
        delta = ln - len(text[line].replace(' ', ''))
        k = delta // (max(len(text[line].split())-1,1))
        space = ' ' * max(1, k)
        text[line] = space.join(text[line].split())
    return to_mid(text)


def to_mid(text: list[str]):
    ln = [len(i) for i in text]
    linemx = max(ln)
    for line in range(len(text)):
        text[line] = ' ' * (math.ceil((linemx - ln[line]) / 2)) + text[line]
    return text


def delete_word(text: list[str]):
    word = input('Введите слово, которое следует удалить: ').strip()
    flag = 0
    for line in range(len(text)):
        if word in text[line]:
            text[line] = text[line].replace(word, '')
            flag += 1
    if not flag:
        print(f'Слово "{word}" не было обнаружено')
    else:
        print(f'Удалено {flag} слов')
    return text


def replace_word(text: list[str]):
    word = input('Введите слово, которое следует заменить: ').strip()
    new_word = input('Введите слово, которое следует вставить на место удаленного: ').strip()
    flag = 0
    letters = ('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВА'
               'ПРОЛДЖЭЯЧСМИТЬБЮ')
    for line in range(len(text)):
        pos_to_replace = text[line].find(word)
        print(pos_to_replace)
        while (pos_to_replace!=-1 and (pos_to_replace==0 or text[line][pos_to_replace-1] not in letters)
               and ((pos_to_replace+len(word)==(len(text[line]))) or text[line][pos_to_replace+len(word)])):
            print(text[line][pos_to_replace-1])
            if pos_to_replace!=0:
                word = text[line][pos_to_replace-1]+word
                new_word = text[line][pos_to_replace-1]+new_word
            if (pos_to_replace+len(word))==len(text[line]):
                word = word+text[line][pos_to_replace+len(word)]
                new_word = new_word+text[line][pos_to_replace+len(word)]
            text[line] = text[line].replace(word, new_word)
            pos_to_replace = text[line].find(word,pos_to_replace+1)
            flag += 1
    if not flag:
        print(f'Слово "{word}" не было обнаружено')
    else:
        print(f'Заменено {flag} слов')
    return text


def print_text(text: list[str]):
    for line in text:
        print(line)

def main(text):
    ans = menu()
    while ans!=0:
        if ans == '1':
            text = to_left(text)
            print_text(text)
        if ans == '2':
            text = to_right(text)
            print_text(text)
        if ans == '3':
            text = to_wide(text)
            print_text(text)
        if ans == '4':
            text = delete_word(text)
            print_text(text)
        if ans == '5':
            text = replace_word(text)
            print_text(text)
        if ans == '6':
            text = to_right(text)
            print_text(text)
        if ans == '7':
            text = to_right(text)
            print_text(text)

        ans = menu()

    print('Выход из программы')

if __name__ == '__main__':
    main(text)
