
import os

def menu():
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
    while not (inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6' or inp == '0'):
        print('Некорректный ввод, повторите попытку')
        inp = input()
    return inp


def is_name_correct(name):
    for i in ',.<>:\'"/?|*\\':
        if i in name:
            return False
    return True


def is_file_name_correct(name):
    tmp = name.split('.')
    if len(tmp) != 2 or tmp[1] == '' or tmp[0] == '':
        return False
    if not is_name_correct(tmp[0]) or not is_name_correct(tmp[1]):
        return False
    return True


def choosing_file() -> int | tuple[str, int]:
    file_name = input('Введите имя файла: ').strip().split('/')
    if len(file_name) == 0:
        print('Некорректный ввод, операция отменена.')
        return 0
    if not is_file_name_correct(file_name[-1]):
        print('Некорректный ввод, операция отменена.')
        return 0
    if file_name[0] == '..' or file_name[0] == '.':
        start = 1
    else:
        start = 0
    for i in range(start, len(file_name) - 1):
        if not is_name_correct(file_name[i]):
            return 0
    try:
        with open('/'.join(file_name), 'r') as file:
            print('Файл выбран и существует')
        return '/'.join(file_name), 1
    except FileNotFoundError:
        print("Файл выбран, но не существует, доступно только создание нового файла базы данных")
        return '/'.join(file_name), 0


def initialize_db(name, separator_in_file='!¤!'): #1 - порядковый номер, 2 - группа, 3 - песня, 4 - альбом, 5 - год создания,
    # 6 - длительность в секундах
    with open(name, 'w', encoding='UTF-8') as file:
        file.write('')
    print(f'Ввод данных в файл {name}. Для завершения ввода введите пустую строку')
    n = 0
    names = ['группу', 'песню', 'альбом', 'год создания', 'длительность в секундах']
    flag_to_read = True
    flag_to_write = True
    while flag_to_read:
        n+=1
        print(f'Запись песни №{n}')
        temp_array = [str(n)]
        for field in names:
            inp = input(f'Введите {field}: ').strip()
            if inp == '':
                print('Ввод завершен')
                if temp_array != []:
                    print('Запись о песне не завершена, она будет удалена')
                    flag_to_write = False
                flag_to_read = False
                break
            temp_array.append(inp)
        if flag_to_write:
            with open(name, 'a', encoding='UTF-8') as file:
                text = separator_in_file.join(temp_array)+'\n'
                file.write(text)
    print(f'Запись базы данных в файл {name} завершена')

def find_last_number(name, separator_in_file = '!¤!'):
    with open(name, 'rb') as f:
        try:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
    return last_line.split(separator_in_file)[0]

def print_db(name, separator_in_file = '!¤!'):
    with open(name, 'r', encoding='UTF-8') as file:
        print('База данных:')
        print('+-----+---------------------------+-------------------------+--------------------------+--------------+-------------------------+')
        print('|  №  |          Группа           |          Песня          |          Альбом          | Год создания | Длительность в секундах |')
        for line in file:
            array = line.split(separator_in_file)
            print(f'|{array[0]:5}|{array[1]:27}|{array[2]:25}|{array[3]:26}|{array[4]:14}|{array[5][:-1]:25}|')
        print('+-----+---------------------------+-------------------------+--------------------------+--------------+-------------------------+')
    print(f'Всего записей: {array[0]}')

def add_to_the_end_of_db(name, separator_in_file = '!¤!'):
    print(f'Ввод данных в конец файла {name}. Для завершения ввода введите пустую строку')
    n = int(find_last_number(name, separator_in_file))
    names = ['группу', 'песню', 'альбом', 'год создания', 'длительность в секундах']
    flag_to_read = True
    flag_to_write = True
    while flag_to_read:
        n += 1
        print(f'Запись песни №{n}')
        temp_array = [str(n)]
        for field in names:
            inp = input(f'Введите {field}: ').strip()
            if inp == '':
                print('Ввод завершен')
                if temp_array != []:
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


def search_by_one_field(name, separator_in_file = '!¤!'):
    with open(name, 'r', encoding='UTF-8') as file:
        pass




def search_by_two_fields(name, separator_in_file = '!¤!'):
    pass


def main():
    file_chosed = 0 # 0 - файл не выбран, 1 - файл выбран, доступен только для записи,
    # 2 - файл выбран, доступен для чтения
    ans = menu()
    while ans != '0':
        if ans == '1':
            file = choosing_file()
            if file:
                file_chosed = file[1] + 1
                file = file[0]
        elif ans == '2':
            if file_chosed > 0:
                initialize_db(file)
                file_chosed = 2
            else:
                print('Файл не выбран')
        elif ans == '3':
            if file_chosed == 2:
                print_db(file)
            else:
                print('Файл не выбран или доступен только для записи')
        elif ans == '4':
            if file_chosed == 2:
                add_to_the_end_of_db(file)
            else:
                print('Файл не выбран или доступен только для записи')
        elif ans == '5':
            if file_chosed == 2:
                search_by_one_field(file)
            else:
                print('Файл не выбран или доступен только для записи')
        elif ans == '6':
            if file_chosed == 2:
                search_by_two_fields(file)
            else:
                print('Файл не выбран или доступен только для записи')
        ans = menu()
    print('Программа завершена')




if __name__ == '__main__':
    main()
