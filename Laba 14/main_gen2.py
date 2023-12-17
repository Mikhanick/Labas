# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 14
# База данных на бинарном файле
import os
import struct


def structurize_line(line, bd_struct='30s 30s 30s 5s 5s',
                     encode='Windows-1251'):  # преобразование строки в структуру
    for i in range(0, len(line)):
        line[i] = line[i].encode(encoding=encode)
    structed_line = struct.pack(bd_struct, *line)
    return structed_line


def destructurize_line(line, bd_struct='30s 30s 30s 5s 5s', encode='Windows-1251'):
    # преобразование структуры в строку
    line = struct.unpack(bd_struct, line)
    line = list(line)
    for i in range(0, len(line)):  # удаление нулевых байтов
        line[i] = line[i].decode(encoding=encode).replace('\x00', '')
    return line

def menu(file_is_opened=1):  # основное меню
    if file_is_opened == 2:
        print('+--------------------------------------------------------------------------------------+')
        print('|1. Выбор файла для работы с ним                                                       |')
        print('|2. Инициализация базы данных (создание или перезапись файла и заполнение его данными) |')
        print('|3. Вывод содержимого базы данных                                                      |')
        print('|4. Добавление записи в конец базы данных                                              |')
        print('|5. Удаление строки                                                                    |')
        print('|6. Поиск по одному полю                                                               |')
        print('|7. Поиск по двум полям                                                                |')
        print('|0. Выход из программы                                                                 |')
        print('+--------------------------------------------------------------------------------------+')
        inp = input('|Вариант ответа: ').strip()
        while not (
                inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6'
                or inp == '0' or inp == '7'):  # проверка
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


def initialize_db(name, bd_struct='30s 30s 30s 5s 5s'):
    # 1 id, 2 - группа, 3 - песня, 4 - альбом, 5 - год создания, 6 - длительность в секундах
    print(f'Ввод данных в файл {name}. Для завершения ввода введите пустую строку')
    n = 0
    names = ['группу', 'песню', 'альбом', 'год создания', 'длительность в секундах']
    flag_to_read = True
    flag_to_write = True
    while flag_to_read:  # ввод данных
        n += 1
        print(f'Запись песни c id = {n}')
        temp_array = []
        for field in names:  # ввод данных
            inp = input(f'Введите {field}: ').strip()
            if field == 'год создания' or field == 'длительность в секундах':  # проверка на корректность ввода
                try:
                    inp = int(inp)
                except ValueError:
                    inp = -1
            while (field == 'год создания' or field == 'длительность в секундах') and not inp > 0:
                print('Год создания и длительность в секундах должны быть целыми положительными числами')
                inp = input(f'Введите {field}: ').strip()
                try:
                    inp = int(inp)
                except ValueError:
                    inp = -1
            if field == 'год создания' or field == 'длительность в секундах':
                inp = str(inp)
            if inp == '':  # завершение ввода

                print('Ввод завершен')
                if temp_array:
                    print('Запись о песне не завершена, она будет удалена')
                    flag_to_write = False
                flag_to_read = False
                break
            temp_array.append(inp)  # добавление введенных данных в массив
        if flag_to_write:  # запись данных в файл поструктурно
            with open(name, 'ab') as file:
                file.write(structurize_line(temp_array, bd_struct=bd_struct))  # запись в файл
    if flag_to_write:
        print(f'Запись базы данных в файл {name} завершена')
    else:
        print(f'Запись базы данных в файл {name} не была произведена')
    return 0


def print_db(name, bd_struct='30s 30s 30s 5s 5s'):  # вывод базы данных
    len_line = struct.calcsize(bd_struct)
    cnt = 0
    try:
        with open(name, 'rb') as file:
            print('База данных:')
            print(
                '+------+---------------------------+-------------------------+--------------------------+'
                '--------------+-------------------------+')
            print(
                '|  id  |          Группа           |          Песня          |          Альбом          |'
                ' Год создания |'
                ' Длительность в секундах |')
            print(
                '+------+---------------------------+-------------------------+--------------------------+'
                '--------------+'
                '-------------------------+')

            while True:
                text = file.read(len_line)
                if not text:
                    break
                array = destructurize_line(text, bd_struct=bd_struct)
                cnt+=1
                if len(array) != 6:
                    text = '" ' + '|'.join(array) + ' "'
                    print(
                        f'Ошибка чтения файла {name} в строке {text} \nИспользуйте другой файл или'
                        f' инициализируйте этот повторно.')
                    return 1
                print(f'|{cnt:^6}|{array[0]:^27}|{array[1]:^25}|{array[2]:^26}|{array[3]:^14}|{array[4]:^25}|')
            print(
                '+------+---------------------------+-------------------------+--------------------------+'
                '--------------+--'
                '-----------------------+')
        print(f'Всего записей: {cnt}')

    except ZeroDivisionError:
        print(f'Ошибка чтения файла {name}. Используйте другой файл или инициализируйте этот повторно.')
        return 1
    return 0


def add_to_the_end_of_db(name, bd_struct='30s 30s 30s 5s 5s'
                         ):  # добавление записи в конец базы данных
    print(f'Ввод данных в конец файла {name}. Для завершения ввода введите пустую строку')
    names = ['группу', 'песню', 'альбом', 'год создания', 'длительность в секундах']
    flag_to_read = True
    flag_to_write = True
    try:
        with open(name, 'rb') as file:
            end = file.seek(0,2)
    except FileNotFoundError:
        end = 0
        with open(name,'wb'):
            pass
    len_line = struct.calcsize(bd_struct)
    qty_recordings = int(end/len_line)
    while flag_to_read:  # ввод данных
        print('Введите номер позиции куда необходимо вставить запись, если номер больше чем количество '
              'записей, запись осуществится в конец файла.')
        while True:
            n = input()
            try:
                n=int(n)
                n = max(0,min(qty_recordings,n))
                break
            except TypeError:
                print('Вы ввели не число повторите ввод.')

        print(f'Запись песни id{n}')
        temp_array = [str(n)]
        for field in names:
            inp = input(f'Введите {field}: ').strip()
            if field == 'год создания' or field == 'длительность в секундах':
                try:
                    inp = int(inp)
                except ValueError:
                    inp = -1
            while (field == 'год создания' or field == 'длительность в секундах') and not inp > 0:
                print('Год создания и длительность в секундах должны быть целыми положительными числами')
                inp = input(f'Введите {field}: ').strip()
                try:
                    inp = int(inp)
                except ValueError:
                    inp = -1
            if field == 'год создания' or field == 'длительность в секундах':
                inp = str(inp)
            if inp == '':

                print('Ввод завершен')
                if temp_array:
                    print('Запись о песне не завершена, она будет удалена')
                    flag_to_write = False
                flag_to_read = False
                break
            temp_array.append(inp)
        if flag_to_write:  # запись данных в файл поструктурно
            with open(name, 'r+b') as file:
                file.seek(n*len_line)
                file.write(structurize_line(temp_array, bd_struct=bd_struct))
    print(f'Запись базы данных в файл {name} завершена')
    return 0

def search_by_one_field(name, bd_struct='30s 30s 30s 5s 5s'
                        ):  # поиск по одному полю
    print('+-------------------------------------+')
    print('|Поиск по одному полю                 |')
    print('|1. Поиск по id                       |')
    print('|2. Поиск по группе                   |')
    print('|3. Поиск по песне                    |')
    print('|4. Поиск по альбому                  |')
    print('|5. Поиск по году создания            |')
    print('|6. Поиск по длительности в секундах  |')
    print('|0. Отмена                            |')
    print('+-------------------------------------+')

    col = input('Введите id поля для поиска: ')
    while not (col == '1' or col == '2' or col == '3' or col == '4' or col == '5' or col == '6' or col == '0'):
        print('Вы ввели некорректный номер поля')
        col = input('Введите номер поля повторно: ')
    col = int(col) - 1
    if col == -1:
        return 0
    inp = input('Введите значение для поиска: ').strip()
    print('Найденные записи:')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+'
        '-------------------------+')
    print(
        '|  id  |          Группа           |          Песня          |          Альбом          | Год создания |'
        ' Длительность в секундах |')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+'
        '-------------------------+')
    with open(name, 'rb') as file:  # Построчно ищем и выводим записи
        len_line = struct.calcsize(bd_struct)
        cnt=0
        while True:
            cnt+=1
            text = file.read(len_line)
            if not text:
                break
            array = destructurize_line(text, bd_struct=bd_struct)
            if len(array) != 6:
                text = '" ' + '|'.join(array) + ' "'
                print(
                    f'Ошибка чтения файла {name} в строке {text} \nИспользуйте другой файл или'
                    f' инициализируйте этот повторно.')
                return 1
            if col!=1 and array[col] == inp or col==1 and str(cnt)==inp:
                print(f'|{cnt:^6}|{array[0]:^27}|{array[1]:^25}|{array[2]:^26}|{array[3]:^14}|{array[4]:^25}|')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+-----'
        '--------------------+')
    return 0


def search_by_two_fields(name, bd_struct='6s 30s 30s 30s 5s 5s'):  # поиск по двум полям
    print('+-------------------------------------+')
    print('|Поиск по двум полям                  |')
    print('|1. Поиск по id                       |')
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
        '+------+---------------------------+-------------------------+--------------------------+--------------+----'
        '---------------------+')
    print(
        '|  id  |          Группа           |          Песня          |          Альбом          | Год создания | '
        'Длительность в секундах |')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+----'
        '---------------------+')
    with open(name, 'rb') as file:
        cnt=0
        len_line = struct.calcsize(bd_struct)
        while True:
            cnt+=1
            text = file.read(len_line)
            if not text:
                break
            array = destructurize_line(text, bd_struct=bd_struct)
            if len(array) != 6:
                text = '" ' + '|'.join(array) + ' "'
                print(
                    f'Ошибка чтения файла {name} в строке {text} \nИспользуйте другой файл или'
                    f' инициализируйте этот повторно.')
                return 1
            if (col1!=1 and array[col1] == inp1 or col1==1 and str(cnt)==inp1) and (col2!=1 and array[col2] == inp2 or col1==1 and str(cnt)==inp1):
                print(f'|{cnt:^6}|{array[0]:^27}|{array[1]:^25}|{array[2]:^26}|{array[3]:^14}|{array[4]:^25}|')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+-------'
        '------------------+')
    return 0


def delete_line(file_name, bd_struct):
    pass


def main():
    BD_STRUCT = '6s 30s 30s 30s 5s 5s'
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
                initialize_db(file_name, bd_struct=BD_STRUCT)
                file_selected = 2
            elif ans == '3':
                return_code = print_db(file_name)
            elif ans == '4':
                return_code = add_to_the_end_of_db(file_name, bd_struct=BD_STRUCT)
            elif ans == '6':
                return_code = search_by_one_field(file_name, bd_struct=BD_STRUCT)
            elif ans == '7':
                return_code = search_by_two_fields(file_name, bd_struct=BD_STRUCT)
            elif ans == '5':
                return_code = delete_line(file_name, bd_struct=BD_STRUCT)
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