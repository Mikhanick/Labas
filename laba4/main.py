# Саватеев Михаил ИУ7-16Б
# Лабораторная работа номер 4 “График”
import math

WIDTH = 90  # Задаем ширину графического поля

# start_value = 0
# step = 0.05
# stop_value = 1.2
#
start_value = float(input('Введите первый элемент последовательности: '))  # Ввод начального элемента последовательности
step = float(input('Введите разность последовательности: '))  # ввод шага последовательности
stop_value = float(input('Введите конечный элемент последовательности: '))  # ввод конца последовательности
if start_value < stop_value and (stop_value-start_value)>step and step>0:
    iterations = math.ceil(
        (stop_value - start_value) / step) + 1  # вычисляем количество элементов в заданной последовательности
    first_table = '''+-----------------------------------+
|    q      |    x1     |    x2     |
+-----------------------------------+'''  # формируем начало первой таблицы
    for iter in range(iterations):  # перебираем элементы последовательности
        q = start_value + step * iter  # элемент последовательности
        x1 = 2.97 * q ** 4 + 4.84 * q ** 3 - 16.4 * q ** 2 + 41.2 * q - 33.2  # значение х1 для элемента последовательности
        if q>100:
            x2 = float('-inf')
        else:
            x2 = 2 - q * math.e ** q  # значение х2 для элемента последовательности

        if iter == 0:  # если это первый элемент последовательности, то он становится и наибольшим и наименьшим
            max1, min1 = x1, x1
            max2, min2 = x2, x2
        if x1 > max1:  # поиск наибольших и наименьших значений
            max1 = x1
        elif x1 < min1:
            min1 = x1
        if x2 > max2:
            max2 = x2
        elif x2 < min2:
            min2 = x2

        qstr = f'{q:^11.5g}'  # форматируем значения к нужному виду, так как они могут быть большие устанавливаем
        # максимальную длину 11 символов, центрируем посередине
        x1str = f'{x1:^11.5g}'
        x2str = f'{x2:^11.5g}'
        first_table += '\n|' + qstr + '|' + x1str + '|' + x2str + '|'  # добавление строки в строковую переменную для
        # последующего вывода
    first_table += '\n+-----------------------------------+'
    print(first_table)  # вывод таблицы со значениями

    serifs = int(input('Введите количество засечек: '))  # ввод количества засечек в шапке графика

    second_table = ' ' * 12 + f'{min1:<11.5g}'  # инициализируем вторую таблицу, вводя минимальное значение
    serif_fraction = (max1 - min1) / (serifs - 1)  # находим, какая часть графика находится между каждыми двумя засечками
    for i in range(1, serifs - 1):
        serif = serif_fraction * i + min1
        second_table += f'{serif:^{round((WIDTH - 2 * 11) / (serifs - 2))}.5g}'  # добавляем все засечки в шапку
    second_table += f'{max1:>11.5g}'

    y_scale = (max1 - min1) / WIDTH  # находим цену деления одной точки на графике
    if min1 > 0 or max1 < 0:  # частный случай, когда весь график с одной стороны от прямой у=0, тогда прямую не
        # отрисовываем
        for iter in range(0, iterations):
            q = start_value + step * iter
            if iter%2==0:
                empty_symbol = ' '
            else:
                empty_symbol = '-'
            x1 = 2.97 * q ** 4 + 4.84 * q ** 3 - 16.4 * q ** 2 + 41.2 * q - 33.2
            x1 = x1 - min1  # находим значение функции аналогично первой таблице
            dot = round(x1 / y_scale)  # находим порядковый номер точки в таблице
            qstr = f'{q:^11.5g}'
            second_table += '\n' + qstr + '|' + empty_symbol * (dot - 1) + '*' + empty_symbol * (WIDTH - dot)  # добавляем строчку в переменную
        print(second_table)
    else:
        dot0 = max(1, round(-min1 / y_scale))  # находим порядковый номер точки, в которой проходит прямая у=0
        for iter in range(0, iterations):
            q = start_value + step * iter
            x1 = 2.97 * q ** 4 + 4.84 * q ** 3 - 16.4 * q ** 2 + 41.2 * q - 33.2
            x1 = x1 - min1
            dot = max(1, round(x1 / y_scale))
            qstr = f'{q:^11.5g}'  # аналогичные действия
            if iter%2==0:
                empty_symbol = ' '
            else:
                empty_symbol = '-'
            if dot0 == dot:
                second_table += '\n' + qstr + '|' + empty_symbol * (dot - 1) + '*' + empty_symbol * (
                            WIDTH - dot)  # если точка совпадает с прямой у=0, то выводим только точку
            elif dot0 < dot:
                second_table += '\n' + qstr + '|' + empty_symbol * (dot0 - 1) + '|' + empty_symbol * (dot - 1 - dot0) + '*' + empty_symbol * (
                            WIDTH - dot)  # если прямая левее точки
            else:
                second_table += ('\n' + qstr + '|' +
                                 empty_symbol * (dot - 1) + '*'+
                                 empty_symbol * (dot0 - 1 - dot)+
                                 '|' + empty_symbol * (WIDTH - dot0 ))  # если точка правее прямой

        print(second_table)  # отрисовываем график
        print('Дополнительное задание:\nXmax1 - Xmax2 =',max1-max2)
else:
    print('Ошибка! Левый конец отрезка должен быть меньше правого, между значениями должно быть больше одного шага, шаг должен быть положительным!')