# Саватеев Михаил ИУ7-16Б
# Лабораторная работа номер 3 "Треугольник"
from typing import Tuple, List


def input_koord()-> tuple[list[int], list[int], list[int]]:  # Функция ввода коорднат
    while True:
        x1 = int(input('Введите координату Х1: '))
        y1 = int(input('Введите координату Y1: '))
        x2 = int(input('Введите координату X2: '))
        y2 = int(input('Введите координату Y2: '))
        x3 = int(input('Введите координату X3: '))
        y3 = int(input('Введите координату Y3: '))
        print()
        if len({(x1, y1), (x2, y2), (x3, y3)}) != 3:  # проверка на различные точки
            print('\033[31m\033[1mОшибка! Точки должны быть различны. Повторите ввод.\033[0m')
        else:
            return [x1, y1], [x2, y2], [x3, y3]


def length(x1:float, y1:float, x2:float, y2:float)->float:  # функция для вычисления длины стороны треугольника
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def area(a1:float, a2:float, a3:float) -> float:  # функция для вычисления стороны стороны треугольника
    p = (a1 + a2 + a3) / 2
    return (p * (p - a1) * (p - a2) * (p - a3)) ** 0.5


def main():
    coordinates = input_koord()  # ввод координат треугольника
    d1 = length(*coordinates[0], *coordinates[1])
    d2 = length(*coordinates[0], *coordinates[2])
    d3 = length(*coordinates[1], *coordinates[2])
    S = area(d1, d2, d3)  # рассчет площади треугольника
    if S == 0:  # проверка на принадлежность точек одной прямой
        print('\033[31m\033[1mОшибка. Точки лежат на прямой.\033[0m')
    print(f'\033[32mДлины сторон треугольника равны: {d1:.7g}; {d2:.7g}; {d3:.7g}\033[0m')
    h1 = S / d1 * 2  # рассчет длины высоты (расстояния от вершины до прямой)
    h2 = S / d2 * 2
    h3 = S / d3 * 2
    out = max(h1, h2, h3)
    print(f'\033[32mДлина высоты, проведенной из наименьшего угла равна {out:.7g} \033[0m')
    sortedArrayOfLength = sorted([d1, d2, d3])  # сортировка длин сторон чтобы наибольший угол
    if (sortedArrayOfLength[0] ** 2 + sortedArrayOfLength[1] ** 2) > sortedArrayOfLength[
        2] ** 2:  # использование теоремы пифагора для нахождения типа треугольника
        print('\033[32mТреугольник остроугольный\033[0m')
    else:
        print('\033[32mТреугольник не остроугольный\033[0m')

    print() #вводд координат точки
    dotCoordinateX = float(input('Введите координатy X точки: '))
    dotCoordinateY = float(input('Введите координатy Y точки: '))
    print()

    dotAreas = [0] * 3  # массив площадей, на которые точка делит изначальный треугольник
    dotRange = [0] * 3  # массив расстоний от точки до сторон треугольника

    for i in range(3):  # обработка всех трех треугольника, на которые точка делит основной
        a1 = length(*coordinates[(i + 1) % 3], *coordinates[i])
        a2 = length(dotCoordinateX, dotCoordinateY, *coordinates[i])
        a3 = length(dotCoordinateX, dotCoordinateY, *coordinates[(i + 1) % 3])

        dotAreas[i] = area(a1, a2, a3)
        dotRange[i] = dotAreas[i] / a1 * 2
    if abs(sum(dotAreas) - S) < 0.0000001:  # сравнение суммы площадей треугольника с изначальным треугольника с учетом погрешности float числа
        if dotAreas[0] != 0 and dotAreas[1] != 0 and dotAreas[2] != 0:
            print('\033[32mТочка лежит внутри треугольника.\033[0m')
        else:
            print('\033[32mТочка лежит на стороне треугольнка.\033[0m')
        out = max(dotRange)
        print(
            f'\033[32mРасстояние до самой удаленной от точки стороны или её продолжения '
            f'равно: {out:.7g} \033[0m')
    else:
        print('\033[32mТочка лежит вне треугольника\033[0m')


if __name__ == '__main__':
    main()
