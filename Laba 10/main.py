# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 10
# Варианты: Правых прямоугольников / Трапеций

from user_inputs import *


def check_is_float(prompt: str) -> float:  # проверка на ввод числа
    while True:
        x = input(prompt)
        flag_digit = 0

        if x[flag_digit] == '-':  # если введен минус, то сдвигаемся на следующий символ
            flag_digit += 1
        if x[flag_digit] == '.':
            flag_digit += 1
        if x[flag_digit].isdigit():
            flag_digit += 1
        else:  # если первый символ не цифра, то выводим ошибку и просим повторить ввод
            print('\033[31m\033[1mОшибка. Введите число!\033[0m')
            continue

        col_e = 0
        col_dot = 0

        flag_to_pass = 0
        for i in range(flag_digit, len(x)):  # перебираем символы
            if flag_to_pass:
                flag_to_pass = 0
                continue
            if x[i].isdigit():
                continue
            elif x[i] == '.' and col_dot == 0 and col_e == 0:  # если точка и ее еще не было, то сдвигаемся на следующий
                col_dot += 1
                if i == len(x)-1:
                    continue
                if x[i + 1].isdigit():
                    continue
                else:
                    print('\033[31m\033[1mОшибка. Введите число!\033[0m')
                    break
            elif x[i] == 'e' and col_e == 0 and i != (
                    len(x) - 1):  # если e и ее еще не было, то сдвигаемся на следующий
                col_e = 1
                if (x[i + 1] == '-' or x[i + 1] == '+') and i != (
                        len(x) - 2):  # если следующий символ минус или плюс и он не
                    # последний, то сдвигаемся на следующий
                    if x[i + 2].isdigit():
                        flag_to_pass = 1
                        continue
                    else:
                        print('\033[31m\033[1mОшибка. Введите число!\033[0m')
                        break
                elif x[i + 1].isdigit():
                    continue
                else:
                    print('\033[31m\033[1mОшибка. Введите число!\033[0m')
                    break
            else:
                print('\033[31m\033[1mОшибка. Введите число!\033[0m')
                break
        else:
            break
    return float(x)


def check_is_int(prompt: str) -> int:  # проверка на ввод целого числа
    while True:
        x = input(prompt)
        flag_digit = 0
        if x[0] == '-':
            flag_digit = 1
        if all([i.isdigit() for i in x[flag_digit:]]):  # если все символы цифры, то прерываем цикл
            break
        else:
            print('\033[31m\033[1mОшибка. Введите целое число!\033[0m')
    return int(x)


def input_with_check() -> tuple[float, float, int, int]:  # ввод данных с проверкой
    global negative
    negative = 1
    start = check_is_float('Введите начало отрезка: ')  # проверка на ввод числа
    end = check_is_float('Введите конец отрезка: ')  # проверка на ввод числа
    if start > end:
        start, end = end, start
        negative = -1
    while True:
        n1 = check_is_int('Введите количество разбиений для первого способа: ')
        n2 = check_is_int('Введите количество разбиений для второго способа: ')
        if n1 <= 0 or n2 <= 0:  # проверка на количество разбиений
            print('\033[31m\033[1mОшибка. Количество разбиений должно быть больше нуля!\033[0m')
        else:
            break
    return start, end, n1, n2


def integral_trapezoid(start: float, end: float, n: int) -> float:  # метод трапеций
    h = (end - start) / n
    sm = 0
    global negative
    for i in range(n):
        sm += (function(start + h * i) + function(start + h * (i + 1))) / 2 * h
    return sm*negative


def integral_right_rectangles(start: float, end: float, n: int) -> float:  # метод правых прямоугольников
    h = (end - start) / n
    global negative
    sm = 0
    for i in range(1,n+1):
        sm += function(start + h * i) * h
    return sm*negative


def print_table(l1: float, l2: float, l3: float, l4: float):  # вывод таблицы
    print()
    print('+---------------+---------------------+---------------------+')
    print('|               |         N1          |         N2          |')
    print('|---------------|---------------------|---------------------|')
    print(f'|  Правых прям. |     {l1:^11.5g}     |     {l2:^11.5g}     |')
    print(f'|   Трапеций    |     {l3:^11.5g}     |     {l4:^11.5g}     |')
    print('+---------------+---------------------+---------------------+')

def porabol_integral(start,stop,n):
    global negative
    sm = 0
    h = (stop-start)/n
    if n%2==0:
        for i in range(0,n-2):
            sm+=(h/6)*(function(start + h * i) + 4 * function(start + (1 + i) * h) + function(start + ( i + 2 ) * h ))
    else:
        print('количество разбиений должно быть кратно 2м')
        return 0
    return sm*negative
def main(e: float):  # основная функция
    start, end, n1, n2 = input_with_check()
    global negative
    l1 = integral_right_rectangles(start, end, n1)
    l2 = integral_right_rectangles(start, end, n2)
    l3 = integral_trapezoid(start, end, n1)
    l4 = integral_trapezoid(start, end, n2)

    integral_ans = (integral(end) - integral(start))*negative
    print_table(l1, l2, l3, l4)
    print()
    print(f'Точное значение интеграла: {integral_ans:.7g}\n')  # выводим точное значение интеграла
    # (для отладки, не по задаче)
    print(f'Значение интеграла по методу параболы с n1: {porabol_integral(start, end, n1):.7g}')
    print(f'Значение интеграла по методу параболы с n2: {porabol_integral(start, end, n2):.7g}')
    most_accuracy = 2  # выбираем наиболее точный метод
    accuracy = l4 - integral_ans

    if abs(l1 - integral_ans) < abs(accuracy):
        most_accuracy = 1
        accuracy = l1 - integral_ans

    if abs(l2 - integral_ans) < abs(accuracy):
        most_accuracy = 1
        accuracy = l2 - integral_ans

    if abs(l3 - integral_ans) < abs(accuracy):
        most_accuracy = 2
        accuracy = l3 - integral_ans
    if integral_ans != 0:

        relation_accuracy = accuracy / abs(integral_ans) * 100
        print(f'Наименьшая погрешность: {abs(accuracy):.7g}\n'
              f'Относительная погрешность: {relation_accuracy:.7g}%\n')  # выводим погрешность
    else:
        print(f'Наименьшая погрешность: {abs(accuracy):.7g}\n'
              'Невозможно вычислить погрешность, из-за деления на ноль')
    n = 1

    if most_accuracy == 2:  # выбираем метод для уточнения
        l = integral_right_rectangles(start, end, n)
        while abs(l - integral_right_rectangles(start, end, n * 2)) > e:  # находим необходимое количество разбиений
            n *= 2
            l = integral_right_rectangles(start, end, n)

        print(f'Наиболее точный результат для метода правых прямоугольников: {l:.7g}\n'
              f'Необходимое количество разбиений: {n}')
    else:
        l = integral_trapezoid(start, end, n)
        while abs(l - integral_trapezoid(start, end, n * 2)) > e:
            n *= 2
            l = integral_trapezoid(start, end, n)

        print(f'Наиболее точный результат для метода трапеций: {l:.7g}\n'
              f'Необходимое количество разбиений: {n}')


if __name__ == '__main__':
    main(NEEDED_ACCURACY)
