# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 8, задание 3, вариант 2
# поиск столбца с наименьшим количеством отрицательных элементов
matrix = [] #инициализируем матрицу
print('Для ввода матрицы напишите через пробел значения строк, затем нажмите Enter. По окончании ввода строк нажмите '
      'Enter')
while True:
    line = [int(i) for i in input().split()] # ввод строки в матрицу
    if matrix == []:
        matrix.append(line) # Если матрица еще пустая то просто добавляем любую строку
    elif line == []: # если введена пустая строка то завершаем ввод матрицы
        print('Ввод матрицы завершен.')
        break
    elif len(matrix[0]) == len (line): # если длина строки равна длине первой строке, иначе выводим ошибку и просим
        # повторить ввод
        matrix.append(line)
    else:
        print(f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна {len(matrix[0])}.\nПовторите ввод!')
if len(matrix) == 0:
    print("Ошибка. Вы ввели пустую матрицу. Работа программы завершена с ошибкой!") # выводим ошибку что не совпадает
    # количестао элементов в строке с отальной матрицей
else:
    # инициализируем индекс столбца с минимальными элементами
    index = -1
    min_cnt = len(matrix)
    for i in range (len(matrix[0])): # перебираем индексы элементов в строке
        cnt = 0
        for j in range (len(matrix)): # перебираем индексы строк
           if matrix[j][i]<0:
               cnt+=1
        if 0<cnt<min_cnt: # если есть минимальное количество не равное нулю
            min_cnt = cnt
            index = i

    if index>-1: # если нашли столбец то выводим его иначе ошибка
        for i in range(len(matrix)):
            print(matrix[i][index])
    else:
        print('Нет колонки с отрицательным элеменетом')