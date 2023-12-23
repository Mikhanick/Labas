# Саватеев Михаил Дмитриевич. ИУ7-16Б
# Лабораторная работа номер 15, задание 3
# Сортировка файла методом бинарных вставок
import struct
from random import randint


def main():
    print('Программа сортирует файл методом бинарных вставок.')
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
            for border in range(cnt_of_numbers):
                while True:
                    try:
                        f.write(struct.pack('i', int(input(f'Введите {border + 1} число: '))))
                        break
                    except ValueError:
                        print('Ошибка. Введите число!')
        else:
            for border in range(cnt_of_numbers):
                f.write(struct.pack('i', randint(-100, 100)))

    with open('file.bin', 'r+b') as f:
        print('Исходный файл:')
        print(*struct.unpack('i'*cnt_of_numbers,(f.read()))) # Вывод исходного файла
        for border in range(1, cnt_of_numbers):
            f.seek(border * 4) # Поиск места для вставки
            number = struct.unpack('i', f.read(4))[0]
            f.seek(0)
            left = 0
            right = border
            middle = 0
            while left < right:
                middle = (left + right) // 2
                f.seek(middle * 4)
                if struct.unpack('i',f.read(4))[0] > number:
                    right = middle
                else:
                    left = middle + 1
            f.seek(middle * 4) # Если число для вставки меньше найденного, то вставляем перед ним
            if struct.unpack('i',f.read(4))[0] > number:
                middle-=1
            for i in range(border, middle+1, -1): # Сдвигаем найденный элемент влево до его найденного места
                f.seek(i*4)
                right_element = f.read(4)
                f.seek((i-1)*4)
                left_element = f.read(4)
                f.seek(i*4)
                f.write(left_element)
                f.seek((i-1)*4)
                f.write(right_element)
        print('Результат:') # Вывод отсортированного файла
        f.seek(0)
        print(*struct.unpack('i'*cnt_of_numbers,(f.read())))


if __name__ == '__main__':
    main()