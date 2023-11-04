# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 8, задание 4
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
    # инициализируем переменные
    min_index = -1
    max_index = -1
    min_sum = 0
    max_sum = 0
    for i in range(len(matrix[0])): # перебираем индексы элементов в строках
        sm = 0
        for j in range(len(matrix)): # перебираем столбцы и считаем сумму в них
            sm += matrix[j][i]
        if sm < min_sum or min_index == -1: # если сумма минимальна то запоминаем индекс столбца
            # print('min new')
            min_sum = sm
            min_index = i
        if sm>max_sum or max_index == -1: # если сумма максимально то запоминаем индекс столбца
            # print('max new')
            max_sum = sm
            max_index = i
        # print(sm,max_sum, min_sum)
    # print(max_index,min_index)

    for i in range(len(matrix)): # меняем лбцы местами
        matrix[i][max_index],matrix[i][min_index] = matrix[i][min_index],matrix[i][max_index]

    for line in matrix: # вывод
        for el in line:
            print(f'{el:5.5g}',end='')
        print()