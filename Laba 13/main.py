# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 13
# База данных на текстовом файле
import os


def menu(file_is_opened=1):  # основное меню
    if file_is_opened == 2:
        print('+--------------------------------------------------------------------------------------+')
        print('|1. Выбор файла для работы с ним                                                       |')
        print('|2. Инициализация базы данных (создание или перезапись файла и заполнение его данными) |')
        print('|3. Вывод содержимого базы данных                                                      |')
        print('|4. Добавление записи в конец базы данных                                              |')
        print('|5. Поиск по одному полю                                                               |')
        print('|6. Поиск по двум полям                                                                |')
        print('|0. Выход из программы                                                                 |')
        print('+--------------------------------------------------------------------------------------+')
        inp = input('|Вариант ответа: ').strip()
        while not (
                inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6' or inp == '0'):  # проверка
            # на корректность ввода
            print('Некорректный ввод, повторите попытку')
            inp = input()
        return inp
    elif file_is_opened == 1:
        print('+--------------------------------------------------------------------------------------+')
        print('|1. Выбор файла для работы с ним                                                       |')
        print('|2. Инициализация базы данных (создание или перезапись файла и заполнение его данными) |')
        print('|0. Выход из программы                                                                 |')
        print('+--------------------------------------------------------------------------------------+')
        inp = input('|Вариант ответа: ').strip()
        while not (
                inp == '1' or inp == '2' or inp == '0'):  # проверка
            # на корректность ввода
            print('Некорректный ввод, повторите попытку')
            inp = input()
        return inp
    else:
        print('+--------------------------------------------------------------------------------------+')
        print('|1. Выбор файла для работы с ним                                                       |')
        print('|0. Выход из программы                                                                 |')
        print('+--------------------------------------------------------------------------------------+')
        inp = input('|Вариант ответа: ').strip()
        while not (
                inp == '1' or inp == '0'):  # проверка
            # на корректность ввода
            print('Некорректный ввод, повторите попытку')
            inp = input()
        return inp

def is_name_correct(name):  # проверка на корректность частей имен файла
    for i in ',.<>:\'"/?|*\\':
        if i in name:
            return False
    return True


def is_file_name_correct(name):  # проверка на корректность имени файла
    tmp = name.split('.')
    if len(tmp) != 2 or tmp[1] == '' or tmp[0] == '':
        return False
    if not is_name_correct(tmp[0]) or not is_name_correct(tmp[1]):
        return False
    return True


def choosing_file() -> int | tuple[str, int]:  # выбор файла
    file_name = input('Введите имя файла: ').strip().split('/')
    if len(file_name) == 0:  # проверка на пустой ввод
        print('Некорректный ввод, операция отменена.')
        return 0
    if not is_file_name_correct(file_name[-1]):  # проверка на корректность имени файла
        print('Некорректный ввод, операция отменена.')
        return 0
    if file_name[0] == '..' or file_name[0] == '.':
        start = 1
    else:
        start = 0
    for i in range(start, len(file_name) - 1):  # проверка на корректность пути имени файла
        if not is_name_correct(file_name[i]):
            return 0
    try:
        with open('/'.join(file_name), 'r') as _:  # проверка на существование файла
            print('Файл выбран и существует')
        return '/'.join(file_name), 1
    except FileNotFoundError:  # файл не существует
        print("Файл выбран, но не существует, доступно только создание нового файла базы данных")
        return '/'.join(file_name), 0


def initialize_db(name,
                  separator_in_file='!¤!'):  # 1 - порядковый номер, 2 - группа, 3 - песня, 4 - альбом, 5 - год
    # создания,
    # 6 - длительность в секундах
    with open(name, 'w', encoding='UTF-8') as file:  # создание файла
        file.write('')
    print(f'Ввод данных в файл {name}. Для завершения ввода введите пустую строку')
    n = 0
    names = ['группу', 'песню', 'альбом', 'год создания', 'длительность в секундах']
    flag_to_read = True
    flag_to_write = True
    while flag_to_read:  # ввод данных
        n += 1
        print(f'Запись песни №{n}')
        temp_array = [str(n)]
        for field in names:
            inp = input(f'Введите {field}: ').strip()
            if inp == '' or inp == separator_in_file:
                if inp == separator_in_file:
                     print(f'Вы ввели недопустимую комбинацию {separator_in_file},'
                           f'являющуюся разделителем в базе данных.')
                print('Ввод завершен')
                if temp_array:
                    print('Запись о песне не завершена, она будет удалена')
                    flag_to_write = False
                flag_to_read = False
                break
            temp_array.append(inp)
        if flag_to_write:  # запись данных в файл построчно
            with open(name, 'a', encoding='UTF-8') as file:
                text = separator_in_file.join(temp_array) + '\n'
                file.write(text)
    print(f'Запись базы данных в файл {name} завершена')
    return 0


def find_last_number(name, separator_in_file='!¤!'):  # поиск последнего номера в файле
    with open(name, 'rb') as f:
        try:
            f.seek(-2, os.SEEK_END)  # Переходим на конец файла
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)  # Переходим на предыдущий символ, пока не наткнемся на \n или начало файла
        except OSError:
            f.seek(0)
        last_line = f.readline().decode(encoding='UTF-8')  # Последняя строка
    return last_line.split(separator_in_file)[0]  # возвращаем последний номер


def print_db(name, separator_in_file='!¤!'):  # вывод базы данных
    try:
        with open(name, 'r', encoding='UTF-8') as file:
            print('База данных:')
            print(
                '+-----+---------------------------+-------------------------+--------------------------+--------------+--'
                '-----------------------+')
            print(
                '|  №  |          Группа           |          Песня          |          Альбом          | Год создания |'
                ' Длительность в секундах |')
            print(
                '+-----+---------------------------+-------------------------+--------------------------+--------------+'
                '-------------------------+')
            for line in file:  # вывод данных построчно

                array = line.split(separator_in_file)
                if len(array) != 6:
                    text = '" '+'|'.join(array)+ ' "'
                    print(
                        f'Ошибка чтения файла {name} в строке {text} \nИспользуйте другой файл или инициализируйте этот повторно.')
                    return 1
                print(f'|{array[0]:^5}|{array[1]:^27}|{array[2]:^25}|{array[3]:^26}|{array[4]:^14}|{array[5][:-1]:^25}|')
            print(
                '+-----+---------------------------+-------------------------+--------------------------+--------------+--'
                '-----------------------+')
        print(f'Всего записей: {array[0]}')
    except UnicodeDecodeError:
        print(f'Ошибка чтения файла {name}. Используйте другой файл или инициализируйте этот повторно.')
        return 1
    return 0


def add_to_the_end_of_db(name, separator_in_file='!¤!',empty_file=1):  # добавление записи в конец базы данных
    print(f'Ввод данных в конец файла {name}. Для завершения ввода введите пустую строку')
    if empty_file:
        n=0
    else:
        try:
            n = int(find_last_number(name, separator_in_file))  # находим последний номер
        except UnicodeDecodeError:
            print(f'Ошибка чтения файла {name} из-за неправильной кодировки. '
                  f'Используйте другой файл или инициализируйте этот повторно.')
            return 1
        except Exception:
            print('Ошибка чтения базы данных. Используйте другой файл или инициализируйте этот повторно.')
            return 1
    names = ['группу', 'песню', 'альбом', 'год создания', 'длительность в секундах']
    flag_to_read = True
    flag_to_write = True
    while flag_to_read:  # аналогично инициализации базы данных
        n += 1
        print(f'Запись песни №{n}')
        temp_array = [str(n)]
        for field in names:
            inp = input(f'Введите {field}: ').strip()
            if inp == '' or inp == separator_in_file:
                if inp == separator_in_file:
                    print(f'Вы ввели недопустимую комбинацию {separator_in_file},'
                          f'являющуюся разделителем в базе данных.')
                print('Ввод завершен')
                if temp_array:
                    print('Запись о песне не завершена, она будет удалена')
                    flag_to_write = False
                flag_to_read = False
                break
            temp_array.append(inp)
        if flag_to_write:
            with open(name, 'a', encoding='UTF-8') as file:
                text = separator_in_file.join(temp_array) + '\n'
                file.write(text)
    print(f'Запись базы данных в файл {name} завершена')
    return 0


def search_by_one_field(name, separator_in_file='!¤!'):  # поиск по одному полю
    print('+-------------------------------------+')
    print('|Поиск по одному полю                 |')
    print('|1. Поиск по номеру                   |')
    print('|2. Поиск по группе                   |')
    print('|3. Поиск по песне                    |')
    print('|4. Поиск по альбому                  |')
    print('|5. Поиск по году создания            |')
    print('|6. Поиск по длительности в секундах  |')
    print('|0. Отмена                            |')
    print('+-------------------------------------+')

    col = input('Введите номер поля для поиска: ')
    while not (col == '1' or col == '2' or col == '3' or col == '4' or col == '5' or col == '6' or col == '0'):
        print('Вы ввели некорректный номер поля')
        col = input('Введите номер поля повторно: ')
    col = int(col) - 1
    if col == -1:
        return 0
    inp = input('Введите значение для поиска: ').strip()
    print('Найденные записи:')
    print(
        '+-----+---------------------------+-------------------------+--------------------------+--------------+'
        '-------------------------+')
    print(
        '|  №  |          Группа           |          Песня          |          Альбом          | Год создания |'
        ' Длительность в секундах |')
    print(
        '+-----+---------------------------+-------------------------+--------------------------+--------------+'
        '-------------------------+')
    with open(name, 'r', encoding='UTF-8') as file:  # Построчно ищем и выводим записи
        for line in file:
            array = line.split(separator_in_file)

            if len(array) != 6:
                text = '" '+'|'.join(array)+ ' "'
                print(
                    f'Ошибка чтения файла {name} в строке {text} \nИспользуйте другой файл или инициализируйте этот повторно.')
                return 1
            if array[col] == inp:
                print(f'|{array[0]:^5}|{array[1]:^27}|{array[2]:^25}|{array[3]:^26}|{array[4]:^14}|{array[5][:-1]:^25}|')
    print(
        '+-----+---------------------------+-------------------------+--------------------------+--------------+-----'
        '--------------------+')
    return 0


def search_by_two_fields(name, separator_in_file='!¤!'):  # поиск по двум полям
    print('+-------------------------------------+')
    print('|Поиск по двум полям                  |')
    print('|1. Поиск по номеру                   |')
    print('|2. Поиск по группе                   |')
    print('|3. Поиск по песне                    |')
    print('|4. Поиск по альбому                  |')
    print('|5. Поиск по году создания            |')
    print('|6. Поиск по длительности в секундах  |')
    print('|0. Отмена                            |')
    print('+-------------------------------------+')
    col1 = input('Введите номер первого поля для поиска: ')
    while not (col1 == '1' or col1 == '2' or col1 == '3' or col1 == '4' or col1 == '5' or col1 == '6' or col1 == '0'):
        print('Вы ввели некорректный номер поля')
        col1 = input('Введите первого номер поля повторно: ')
    col1 = int(col1) - 1
    if col1 == -1:
        return 0
    col2 = input('Введите номер второго поля для поиска: ')
    while not (col2 == '1' or col2 == '2' or col2 == '3' or col2 == '4' or col2 == '5' or col2 == '6' or col2 == '0'):
        print('Вы ввели некорректный номер поля')
        col2 = input('Введите номер второго поля повторно: ')
    col2 = int(col2) - 1
    if col2 == -1:
        return 0
    inp1 = input('Введите значение первого поля для поиска: ').strip()
    inp2 = input('Введите значение второго поля для поиска: ').strip()
    print('Найденные записи:')
    print(
        '+-----+---------------------------+-------------------------+--------------------------+--------------+----'
        '---------------------+')
    print(
        '|  №  |          Группа           |          Песня          |          Альбом          | Год создания | '
        'Длительность в секундах |')
    print(
        '+-----+---------------------------+-------------------------+--------------------------+--------------+----'
        '---------------------+')
    with open(name, 'r', encoding='UTF-8') as file:
        for line in file:
            array = line.split(separator_in_file)
            if len(array) != 6:
                text = '" ' + '|'.join(array) + ' "'
                print(
                    f'Ошибка чтения файла {name} в строке {text} \nИспользуйте другой файл или инициализируйте этот повторно.')
                return 1
            if array[col1] == inp1 and array[col2] == inp2:
                print(f'|{array[0]:^5}|{array[1]:^27}|{array[2]:^25}|{array[3]:^26}|{array[4]:^14}|{array[5][:-1]:^25}|')
    print(
        '+-----+---------------------------+-------------------------+--------------------------+--------------+-------'
        '------------------+')
    return 0


def main():
    SEPARATOR_IN_FILE = '!¤!'
    file_selected = 0  # 0 - файл не выбран, 1 - файл выбран, доступен только для записи,
    # 2 - файл выбран, доступен для чтения
    ans = menu(file_selected)
    return_code = 0
    file_name = ''
    while ans != '0':
        try:
            if ans == '1':
                file = choosing_file()
                if file:
                    file_selected = file[1] + 1
                    file_name = file[0]
            elif ans == '2':
                if file_selected > 0:
                    initialize_db(file_name,separator_in_file=SEPARATOR_IN_FILE)
                    file_selected = 2
                else:
                    print('Файл не выбран')
            elif ans == '3':
                if file_selected == 2:
                    return_code = print_db(file_name)
                else:
                    print('Файл не выбран или доступен только для записи')
            elif ans == '4':
                if file_selected == 1:
                    return_code = add_to_the_end_of_db(file_name,separator_in_file=SEPARATOR_IN_FILE)
                elif file_selected == 2:
                    return_code = add_to_the_end_of_db(file_name,empty_file=0,separator_in_file=SEPARATOR_IN_FILE)
                else:
                    print('Файл не выбран или доступен только для записи')
            elif ans == '5':
                if file_selected == 2:
                    return_code = search_by_one_field(file_name,separator_in_file=SEPARATOR_IN_FILE)
                else:
                    print('Файл не выбран или доступен только для записи')
            elif ans == '6':
                if file_selected == 2:
                    return_code = search_by_two_fields(file_name,separator_in_file=SEPARATOR_IN_FILE)
                else:
                    print('Файл не выбран или доступен только для записи')

            if return_code:
                print('\nФайл был открыт некорректно и теперь доступен только для записи.')
                file_selected = 1
                return_code = 0
        except FileNotFoundError:
            print(f"Произошла непредвиденная ошибка, файл {file_name} не найден")
            print("Проверьте правильность ввода имени файла или введите другой файл")
            file = choosing_file()
            if file:
                file_selected = file[1] + 1
                file_name = file[0]
        ans = menu(file_is_opened=file_selected)
    print('Программа завершена')


if __name__ == '__main__':
    main()
