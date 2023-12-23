# Саватеев Михаил Дмитриевич, группа ИУ7-16Б
# Лабораторная работа номер 15, задание 1
# Вариант 3. Удалить из файла все нечетные числа.


import struct
from random import randint
def main():
    print('Программа удаляет из файла все нечетные числа.')
    cnt_of_numbers = 30
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

    with open('file.bin', 'r+b') as f:
        print('Исходный файл:') # Вывод исходного файла
        print(*struct.unpack('i'*cnt_of_numbers,(f.read())))
        offset = 0
        for i in range(cnt_of_numbers): # перебираем все числа и если число нечетное, то увеличиваем смещение
            f.seek(i * 4)
            number = struct.unpack('i', f.read(4))[0]
            f.seek(i*4-offset)
            if number % 2 != 0:
                offset += 4
            f.write(struct.pack('i', number)) # записываем число на новое место
        f.truncate(cnt_of_numbers*4-offset) # обрезаем файл
        f.seek(0)
        print('Результат:')
        print(*struct.unpack('i' * ((cnt_of_numbers*4-offset)//4), f.read()))


if __name__ == '__main__':
    main()