# Саватеев Михаил Дмитриевич, группа ИУ7-16Б
# Лабораторная работа номер 15, задание 2
# После каждого четного числа добавить его удвоенное значение

import struct
from random import randint


def main():
    print('Программа добавляет после каждого четного числа его удвоенное значение.')
    cnt_of_numbers = 10
    with open('file.bin', 'wb') as f: # Запись чисел в файл
        randomise_numbers = input('Введите 1 чтобы ввести свои числа, иначе будут сгенерированы случайные: ')
        if randomise_numbers == '1':
            while True:
                try:
                    cnt_of_numbers = int(input('Введите количество чисел: '))
                    break
                except ValueError:
                    print('Ошибка. Введите число!')
            for i in range(cnt_of_numbers):
                while True:
                    try:
                        f.write(struct.pack('i', int(input(f'Введите {i+1} число: '))))
                        break
                    except ValueError:
                        print('Ошибка. Введите число!')
        else:
            for i in range(cnt_of_numbers):
                f.write(struct.pack('i', randint(-100, 100)))

    with open('file.bin', 'rb') as f: # Подсчет количества чисел, которые нужно добавить
        cnt_to_add = 0
        print('Исходный файл:')
        print(*struct.unpack('i'*cnt_of_numbers,(f.read())))
        for i in range(cnt_of_numbers):
            f.seek(i*4)
            number = struct.unpack('i', f.read(4))[0]
            if number % 2 == 0:
                cnt_to_add += 1
    with open('file.bin', 'ab') as f: # Добавление необходимого количества места под числа
        f.write(struct.pack('i'*cnt_to_add, *(0 for _ in range(cnt_to_add))))
    with open('file.bin', 'r+b') as f:
        offset = cnt_to_add # Смещение
        for i in range(cnt_of_numbers-1, -1, -1): # Перебираем числа с конца и если число четное, то увеличиваем смещение
            f.seek(i*4)
            number = struct.unpack('i', f.read(4))[0]
            if number % 2 == 0: # Записываем удвоенное четное число на перед четным (если смотреть с конца)
                f.seek((i+offset)*4)
                f.write(struct.pack('i', number*2))
                offset -= 1
            f.seek((i+offset)*4)
            f.write(struct.pack('i', number)) # Записываем число на новое место
        f.seek(0)
        print('Результат:')
        print(*struct.unpack('i' * (cnt_of_numbers+cnt_to_add), f.read()))


if __name__ == '__main__':
    main()

