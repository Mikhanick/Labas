# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 8, задание 5
matrix = [] #инициализируем матрицу
print('Для ввода матрицы напишите через пробел значения строк, затем нажмите Enter. Когда матрица станет квадратной,'
      'ввод окончится')
while True:
    line = [int(i) for i in input().split()] # ввод строки в матрицу
    if matrix == []:
        matrix.append(line) # Если матрица еще пустая то просто добавляем любую строку

    elif len(matrix[0]) == len (line): # если длина строки равна длине первой строке, иначе выводим ошибку и просим
        # повторить ввод
        matrix.append(line)
    else:
        print(f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна {len(matrix[0])}.\nПовторите ввод!')


    if len(matrix) == len(matrix[0]): # если введена пустая строка то завершаем ввод матрицы
        print('Ввод матрицы завершен.')
        break
if len(matrix) == 0:
    print("Ошибка. Вы ввели пустую матрицу. Работа программы завершена с ошибкой!") # выводим ошибку что не совпадает
    # количестао элементов в строке с отальной матрицей
else:
    #инициаизируем переменные
    mx = matrix[0][1]
    mn = matrix[1][-1]
    for i in range (len(matrix)): # перебираем строки
        for j in range (len(matrix[0])): #перебираем столбцы
            if i>(len(matrix[0])-j-1): # если ниже побочной диагонали ищем минимальное
                #print(matrixD[i][j])
                mn = min(mn,matrix[i][j])
            if i<j: # если выше главной ищем макс
                mx = max(mx,matrix[i][j])


    for line in matrix: # вывод
        for el in line:
            print(f'{el:5.5g}',end='')
        print()
    print(f'Максимальное: {mx} Минимальное: {mn}') #вывод