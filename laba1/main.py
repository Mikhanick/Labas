# Саватеев Михаил ИУ7-16Б
# задание: написать програму, которая по заданным числовым параметра объемной фигуры определит е характеристики
# вариант 8 усеченный конус

from math import pi, sqrt  # импорт числа пи и функции квадратного корня из библиотеки math
from typing import Tuple


def inp() -> tuple[float, float, float]:  # блок ввода данных
    try:  # обработка некорректного воода данных
        r = float(input('input r: '))  # input r
        R = float(input('input R: '))  # input R
        h = float(input('input h: '))  # input h

        if r < 0 or R < 0 or h < 0:  # проверка введенных значений на неотрицательность
            raise Exception("Ввод отрицательного значения")  # вызов ошибки при отрицательных данных
    except Exception:
        print('\033[31m\033[1mБыли введены некорректные значения! Перезапустите программу.\033[32m')
        exit(-1)
    print()
    return r, R, h  # возврат значений в виде кортежа


def main(r: int, R: int, h: int) -> dict:  # начало функции счета
    L = sqrt(((R - r) ** 2 + h ** 2))  # рассчет длины апофемы
    sideSurfaceArea = pi * (R + r) * L  # рассчет площади бока
    totalSurfaceArea = sideSurfaceArea + pi * r ** 2 + pi * R ** 2  # рассчет полной площади
    V = (1 / 3) * pi * h * (r ** 2 + R ** 2 + R * r)  # рассчет объема
    return {'V': V, 'Sполн': totalSurfaceArea,
            'Sбок': sideSurfaceArea}  # возврат значений в виде кортежа


def out(value: intl):
    print(f'\033[92m\033[3m\033[4m{value[0]}: {value[1]:.7g}\033[0m')  # привод к требуемому виду и вывод


if __name__ == '__main__':
    for i in main(*inp()).items():  # перебор значений в парах в словаре
        out(i)  # вызов функции вывода
