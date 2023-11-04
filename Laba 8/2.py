# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 8, задание 22
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
    # инициализируем макс/мин элементы и индексы на котороых они находятся
    max_cnt = 0
    min_cnt = len(matrix[0])
    index_max = -1
    index_min = -1

    for i in range(len(matrix)): # перебираем строки в матрицце
        cnt = 0
        for j in matrix[i]: # если отрицательное прибавлем счетчик
            if j < 0:
                cnt += 1
        #print('cnt =', cnt,'max count', max_cnt,'min_count', min_cnt)
        if cnt>max_cnt: # если счетчик больше максимального
            max_cnt = cnt
            index_max = i

        if cnt < min_cnt and cnt > 0: # если счетчик меньше миниума но больше нуля
            min_cnt = cnt
            index_min = i

    #print(index_max,index_min)
    if index_min > -1 and index_max!=index_min: #если встретились и максимальное и минимальное количество то меняем их строки
        matrix[index_max], matrix[index_min] = matrix[index_min],matrix[index_max]

    for line in matrix:  # вывод
        for el in line:
            print(f'{el:5.5g}', end='')
        print()