# �������� ������ ������ ��7-16�
# ������������ ������ ����� 14
# ���� ������ �� �������� �����
import os
import struct


def structurize_line(line, bd_struct='30s 30s 30s 5s 5s',
                     encode='Windows-1251'):  # �������������� ������ � ���������
    for i in range(0, len(line)):
        line[i] = line[i].encode(encoding=encode)
    structed_line = struct.pack(bd_struct, *line)
    return structed_line


def destructurize_line(line, bd_struct='30s 30s 30s 5s 5s', encode='Windows-1251'):
    # �������������� ��������� � ������
    line = struct.unpack(bd_struct, line)
    line = list(line)
    for i in range(0, len(line)):  # �������� ������� ������
        line[i] = line[i].decode(encoding=encode).replace('\x00', '')
    return line

def menu(file_is_opened=1):  # �������� ����
    if file_is_opened == 2:
        print('+--------------------------------------------------------------------------------------+')
        print('|1. ����� ����� ��� ������ � ���                                                       |')
        print('|2. ������������� ���� ������ (�������� ��� ���������� ����� � ���������� ��� �������) |')
        print('|3. ����� ����������� ���� ������                                                      |')
        print('|4. ���������� ������ � ����� ���� ������                                              |')
        print('|5. �������� ������                                                                    |')
        print('|6. ����� �� ������ ����                                                               |')
        print('|7. ����� �� ���� �����                                                                |')
        print('|0. ����� �� ���������                                                                 |')
        print('+--------------------------------------------------------------------------------------+')
        inp = input('|������� ������: ').strip()
        while not (
                inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6'
                or inp == '0' or inp == '7'):  # ��������
            # �� ������������ �����
            print('������������ ����, ��������� �������')
            inp = input()
        return inp
    elif file_is_opened == 1:
        print('+--------------------------------------------------------------------------------------+')
        print('|1. ����� ����� ��� ������ � ���                                                       |')
        print('|2. ������������� ���� ������ (�������� ��� ���������� ����� � ���������� ��� �������) |')
        print('|0. ����� �� ���������                                                                 |')
        print('+--------------------------------------------------------------------------------------+')
        inp = input('|������� ������: ').strip()
        while not (
                inp == '1' or inp == '2' or inp == '0'):  # ��������
            # �� ������������ �����
            print('������������ ����, ��������� �������')
            inp = input()
        return inp
    else:
        print('+--------------------------------------------------------------------------------------+')
        print('|1. ����� ����� ��� ������ � ���                                                       |')
        print('|0. ����� �� ���������                                                                 |')
        print('+--------------------------------------------------------------------------------------+')
        inp = input('|������� ������: ').strip()
        while not (
                inp == '1' or inp == '0'):  # ��������
            # �� ������������ �����
            print('������������ ����, ��������� �������')
            inp = input()
        return inp

def is_name_correct(name):  # �������� �� ������������ ������ ���� �����
    for i in ',.<>:\'"/?|*\\':
        if i in name:
            return False
    return True


def is_file_name_correct(name):  # �������� �� ������������ ����� �����
    tmp = name.split('.')
    if len(tmp) != 2 or tmp[1] == '' or tmp[0] == '':
        return False
    if not is_name_correct(tmp[0]) or not is_name_correct(tmp[1]):
        return False
    return True

def choosing_file() -> int | tuple[str, int]:  # ����� �����
    file_name = input('������� ��� �����: ').strip().split('/')
    if len(file_name) == 0:  # �������� �� ������ ����
        print('������������ ����, �������� ��������.')
        return 0
    if not is_file_name_correct(file_name[-1]):  # �������� �� ������������ ����� �����
        print('������������ ����, �������� ��������.')
        return 0
    if file_name[0] == '..' or file_name[0] == '.':
        start = 1
    else:
        start = 0
    for i in range(start, len(file_name) - 1):  # �������� �� ������������ ���� ����� �����
        if not is_name_correct(file_name[i]):
            return 0
    try:
        with open('/'.join(file_name), 'r') as _:  # �������� �� ������������� �����
            print('���� ������ � ����������')
        return '/'.join(file_name), 1
    except FileNotFoundError:  # ���� �� ����������
        print("���� ������, �� �� ����������, �������� ������ �������� ������ ����� ���� ������")
        return '/'.join(file_name), 0


def initialize_db(name, bd_struct='30s 30s 30s 5s 5s'):
    # 1 id, 2 - ������, 3 - �����, 4 - ������, 5 - ��� ��������, 6 - ������������ � ��������
    print(f'���� ������ � ���� {name}. ��� ���������� ����� ������� ������ ������')
    n = 0
    names = ['������', '�����', '������', '��� ��������', '������������ � ��������']
    flag_to_read = True
    flag_to_write = True
    while flag_to_read:  # ���� ������
        n += 1
        print(f'������ ����� c id = {n}')
        temp_array = []
        for field in names:  # ���� ������
            inp = input(f'������� {field}: ').strip()
            if field == '��� ��������' or field == '������������ � ��������':  # �������� �� ������������ �����
                try:
                    inp = int(inp)
                except ValueError:
                    inp = -1
            while (field == '��� ��������' or field == '������������ � ��������') and not inp > 0:
                print('��� �������� � ������������ � �������� ������ ���� ������ �������������� �������')
                inp = input(f'������� {field}: ').strip()
                try:
                    inp = int(inp)
                except ValueError:
                    inp = -1
            if field == '��� ��������' or field == '������������ � ��������':
                inp = str(inp)
            if inp == '':  # ���������� �����

                print('���� ��������')
                if temp_array:
                    print('������ � ����� �� ���������, ��� ����� �������')
                    flag_to_write = False
                flag_to_read = False
                break
            temp_array.append(inp)  # ���������� ��������� ������ � ������
        if flag_to_write:  # ������ ������ � ���� ������������
            with open(name, 'ab') as file:
                file.write(structurize_line(temp_array, bd_struct=bd_struct))  # ������ � ����
    if flag_to_write:
        print(f'������ ���� ������ � ���� {name} ���������')
    else:
        print(f'������ ���� ������ � ���� {name} �� ���� �����������')
    return 0


def print_db(name, bd_struct='30s 30s 30s 5s 5s'):  # ����� ���� ������
    len_line = struct.calcsize(bd_struct)
    cnt = 0
    try:
        with open(name, 'rb') as file:
            print('���� ������:')
            print(
                '+------+---------------------------+-------------------------+--------------------------+'
                '--------------+-------------------------+')
            print(
                '|  id  |          ������           |          �����          |          ������          |'
                ' ��� �������� |'
                ' ������������ � �������� |')
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
                        f'������ ������ ����� {name} � ������ {text} \n����������� ������ ���� ���'
                        f' ��������������� ���� ��������.')
                    return 1
                print(f'|{cnt:^6}|{array[0]:^27}|{array[1]:^25}|{array[2]:^26}|{array[3]:^14}|{array[4]:^25}|')
            print(
                '+------+---------------------------+-------------------------+--------------------------+'
                '--------------+--'
                '-----------------------+')
        print(f'����� �������: {cnt}')

    except ZeroDivisionError:
        print(f'������ ������ ����� {name}. ����������� ������ ���� ��� ��������������� ���� ��������.')
        return 1
    return 0


def add_to_the_end_of_db(name, bd_struct='30s 30s 30s 5s 5s'
                         ):  # ���������� ������ � ����� ���� ������
    print(f'���� ������ � ����� ����� {name}. ��� ���������� ����� ������� ������ ������')
    names = ['������', '�����', '������', '��� ��������', '������������ � ��������']
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
    while flag_to_read:  # ���� ������
        print('������� ����� ������� ���� ���������� �������� ������, ���� ����� ������ ��� ���������� '
              '�������, ������ ������������ � ����� �����.')
        while True:
            n = input()
            try:
                n=int(n)
                n = max(0,min(qty_recordings,n))
                break
            except TypeError:
                print('�� ����� �� ����� ��������� ����.')

        print(f'������ ����� id{n}')
        temp_array = [str(n)]
        for field in names:
            inp = input(f'������� {field}: ').strip()
            if field == '��� ��������' or field == '������������ � ��������':
                try:
                    inp = int(inp)
                except ValueError:
                    inp = -1
            while (field == '��� ��������' or field == '������������ � ��������') and not inp > 0:
                print('��� �������� � ������������ � �������� ������ ���� ������ �������������� �������')
                inp = input(f'������� {field}: ').strip()
                try:
                    inp = int(inp)
                except ValueError:
                    inp = -1
            if field == '��� ��������' or field == '������������ � ��������':
                inp = str(inp)
            if inp == '':

                print('���� ��������')
                if temp_array:
                    print('������ � ����� �� ���������, ��� ����� �������')
                    flag_to_write = False
                flag_to_read = False
                break
            temp_array.append(inp)
        if flag_to_write:  # ������ ������ � ���� ������������
            with open(name, 'r+b') as file:
                file.seek(n*len_line)
                file.write(structurize_line(temp_array, bd_struct=bd_struct))
    print(f'������ ���� ������ � ���� {name} ���������')
    return 0

def search_by_one_field(name, bd_struct='30s 30s 30s 5s 5s'
                        ):  # ����� �� ������ ����
    print('+-------------------------------------+')
    print('|����� �� ������ ����                 |')
    print('|1. ����� �� id                       |')
    print('|2. ����� �� ������                   |')
    print('|3. ����� �� �����                    |')
    print('|4. ����� �� �������                  |')
    print('|5. ����� �� ���� ��������            |')
    print('|6. ����� �� ������������ � ��������  |')
    print('|0. ������                            |')
    print('+-------------------------------------+')

    col = input('������� id ���� ��� ������: ')
    while not (col == '1' or col == '2' or col == '3' or col == '4' or col == '5' or col == '6' or col == '0'):
        print('�� ����� ������������ ����� ����')
        col = input('������� ����� ���� ��������: ')
    col = int(col) - 1
    if col == -1:
        return 0
    inp = input('������� �������� ��� ������: ').strip()
    print('��������� ������:')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+'
        '-------------------------+')
    print(
        '|  id  |          ������           |          �����          |          ������          | ��� �������� |'
        ' ������������ � �������� |')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+'
        '-------------------------+')
    with open(name, 'rb') as file:  # ��������� ���� � ������� ������
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
                    f'������ ������ ����� {name} � ������ {text} \n����������� ������ ���� ���'
                    f' ��������������� ���� ��������.')
                return 1
            if col!=1 and array[col] == inp or col==1 and str(cnt)==inp:
                print(f'|{cnt:^6}|{array[0]:^27}|{array[1]:^25}|{array[2]:^26}|{array[3]:^14}|{array[4]:^25}|')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+-----'
        '--------------------+')
    return 0


def search_by_two_fields(name, bd_struct='6s 30s 30s 30s 5s 5s'):  # ����� �� ���� �����
    print('+-------------------------------------+')
    print('|����� �� ���� �����                  |')
    print('|1. ����� �� id                       |')
    print('|2. ����� �� ������                   |')
    print('|3. ����� �� �����                    |')
    print('|4. ����� �� �������                  |')
    print('|5. ����� �� ���� ��������            |')
    print('|6. ����� �� ������������ � ��������  |')
    print('|0. ������                            |')
    print('+-------------------------------------+')
    col1 = input('������� ����� ������� ���� ��� ������: ')
    while not (col1 == '1' or col1 == '2' or col1 == '3' or col1 == '4' or col1 == '5' or col1 == '6' or col1 == '0'):
        print('�� ����� ������������ ����� ����')
        col1 = input('������� ������� ����� ���� ��������: ')
    col1 = int(col1) - 1
    if col1 == -1:
        return 0
    col2 = input('������� ����� ������� ���� ��� ������: ')
    while not (col2 == '1' or col2 == '2' or col2 == '3' or col2 == '4' or col2 == '5' or col2 == '6' or col2 == '0'):
        print('�� ����� ������������ ����� ����')
        col2 = input('������� ����� ������� ���� ��������: ')
    col2 = int(col2) - 1
    if col2 == -1:
        return 0
    inp1 = input('������� �������� ������� ���� ��� ������: ').strip()
    inp2 = input('������� �������� ������� ���� ��� ������: ').strip()
    print('��������� ������:')
    print(
        '+------+---------------------------+-------------------------+--------------------------+--------------+----'
        '---------------------+')
    print(
        '|  id  |          ������           |          �����          |          ������          | ��� �������� | '
        '������������ � �������� |')
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
                    f'������ ������ ����� {name} � ������ {text} \n����������� ������ ���� ���'
                    f' ��������������� ���� ��������.')
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
    file_selected = 0  # 0 - ���� �� ������, 1 - ���� ������, �������� ������ ��� ������,
    # 2 - ���� ������, �������� ��� ������
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
                print('\n���� ��� ������ ����������� � ������ �������� ������ ��� ������.')
                file_selected = 1
                return_code = 0
        except FileNotFoundError:
            print(f"��������� �������������� ������, ���� {file_name} �� ������")
            print("��������� ������������ ����� ����� ����� ��� ������� ������ ����")
            file = choosing_file()
            if file:
                file_selected = file[1] + 1
                file_name = file[0]
        ans = menu(file_is_opened=file_selected)
    print('��������� ���������')


if __name__ == '__main__':
    main()