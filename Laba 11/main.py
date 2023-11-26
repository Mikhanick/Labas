from time import time
from random import randint


def check_is_float(x: str) -> bool:  # проверка на ввод числа
    flag_digit = 0

    if x[flag_digit] == '-':  # если введен минус, то сдвигаемся на следующий символ
        flag_digit += 1
    if len(x) > flag_digit and x[flag_digit] == '.':
        flag_digit += 1
    if len(x) > flag_digit and x[flag_digit].isdigit():
        flag_digit += 1
    else:  # если первый символ не цифра, то выводим ошибку и просим повторить ввод
        return False

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
            if i == len(x) - 1:
                continue
            if x[i + 1].isdigit():
                continue
            else:
                return False
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
                    return False
            elif x[i + 1].isdigit():
                continue
            else:
                return False
        else:
            return False
    else:
        return True


def input_array() -> list:
    print("Введите через пробел элементы массива, который необходимо отсортировать")  # ввод массива
    array = input().split()
    array_out = []
    for el in array:  # проверка на ввод числа
        if check_is_float(el):
            array_out.append(float(el))
        else:
            print(f'\033[31m\033[1mЭлемент {el} не является числом и поэтому был исключен из массива\033[0m')
    if len(array_out) == 0:  # если массив пустой, то выводим ошибку
        print('\033[31m\033[1mВнимание! В массиве нет чисел\033[0m')
    return array_out


def binary_search(array: list, elem: float, start: int = 0, end: int = 0) -> int:  # бинарный поиск
    if end == 0:  # если конец не задан, то задаем его
        end = len(array)
    if elem < array[start]:  # если элемент меньше первого, то возвращаем первый индекс
        return start
    elif elem >= array[end - 1]:  # если элемент больше последнего, то возвращаем последний индекс
        return end
    index = end // 2
    if array[index] == elem:  # если элемент равен элементу по индексу, то возвращаем индекс
        return index + 1
    elif array[index] > elem:  # если элемент больше элемента по индексу, то сдвигаем конец
        high_index = index
        low_index = start
    else:
        high_index = end - 1
        low_index = index
    while high_index - low_index != 1:  # пока разница между индексами не равна 1
        index = (high_index + low_index) // 2
        array_by_index = array[index]
        if array_by_index > elem:
            high_index = index
        elif array_by_index < elem:
            low_index = index
        else:
            return index + 1
    return high_index


def insert_binary_sort(array: list) -> tuple[list, int]:  # сортировка вставками
    cnt = 0
    for barier in range(len(array) - 1):  # перебираем элементы
        new_element = array[barier + 1]
        new_index = binary_search(array, new_element, end=barier + 1)
        for i in range(barier + 1, new_index, -1):  # сдвигаем элементы
            cnt += 1
            temporary_elem = array[i]
            array[i] = array[i - 1]
            array[i - 1] = temporary_elem
        array[new_index] = new_element
    return array, cnt


def print_array(array: list) -> None:  # вывод массива
    for el in array:
        print(f'{el:.7g}', end=' ')
    print()


def print_table(times_r: list[float], cnt_r: list[int], times_p: list[float], cnt_p: list[int], times_n: list[float],
                cnt_n: list[int], N: list[float, float, float]) -> None:  # вывод таблицы
    print(
        '+----------------------+------------------------------+'
        '------------------------------+------------------------------+')
    print(f'| Размерность массива: | {float(N[0]):^28.5g} | {float(N[1]):^28.5g} | {float(N[2]):^28.5g} |')
    print(
        '+----------------------|-------------+----------------|'
        '-------------+----------------|-------------+----------------+')
    print(
        '|                      |    Время    |  Перестановки  |'
        '    Время    |  Перестановки  |    Время    |  Перестановки  |')
    print(
        '+----------------------|-------------+----------------|'
        '-------------+----------------|-------------+----------------+')
    print('| Упорядоченный список |', end='')
    for i in range(3):
        print(f' {times_p[i]:^11.5g} | {cnt_p[i]:^14.7g} |', end='')
    print(
        '\n+----------------------|-------------+----------------|'
        '-------------+----------------|-------------+----------------+')

    print('|   Случайный список   |', end='')
    for i in range(3):
        print(f' {times_r[i]:^11.5g} | {cnt_r[i]:^14.7g} |', end='')
    print(
        '\n'
        '+----------------------|-------------+----------------|'
        '-------------+----------------|-------------+----------------+')

    print('|    Упорядоченный     |', end='')
    for i in range(3):
        print(f' {times_n[i]:^11.5g} | {cnt_n[i]:^14.7g} |', end='')
    print('\n'
          '|  в обратном порядке  |             |                |'
          '             |                |             |       '
          '         |')
    print(
        '+----------------------+-------------+----------------+'
        '-------------+----------------+-------------+----------------+')


def main():
    array = input_array()  # ввод массива
    print()
    if array:
        print("Отсортированный методом бинарной вставки массив:")  # вывод отсортированного массива
        print_array(insert_binary_sort(array)[0])
    print()

    N = []
    for i in range(1, 4):  # ввод размерностей массивов
        print(f'Введите размерность {i} массива.')
        N.append(int(input()))
    print()

    time_random = []
    time_positive = []
    time_negative = []

    cnt_random = []
    cnt_positive = []
    cnt_negative = []

    for qty in N:  # перебираем размерности
        random_array = [randint(-qty, qty) for _ in range(qty)]
        positive_array = list(range(qty))
        negative_array = list(range(qty, 0, -1))

        t = time()  # считаем время
        cnt_rand = insert_binary_sort(random_array)[1]
        time_rand = time() - t

        t = time()
        cnt_pos = insert_binary_sort(positive_array)[1]
        time_pos = time() - t

        t = time()
        cnt_neg = insert_binary_sort(negative_array)[1]
        time_neg = time() - t

        cnt_positive.append(cnt_pos)  # добавляем количество перестановок
        cnt_random.append(cnt_rand)
        cnt_negative.append(cnt_neg)

        time_negative.append(time_neg)  # добавляем время
        time_random.append(time_rand)
        time_positive.append(time_pos)

    print_table(time_random, cnt_random, time_positive, cnt_positive, time_negative, cnt_negative, N)


if __name__ == '__main__':
    main()
