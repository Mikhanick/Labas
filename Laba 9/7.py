matrix_3d = []
out_flag = 0
length_of_matrix = -1
while True:

    matrix = [] #инициализируем матрицу
    if length_of_matrix ==-1:
        print('Для ввода слоя напишите через пробел значения строк, затем нажмите Enter. По окончании ввода строк нажмите '
              'Enter')
    else:
        print(
            'Для ввода следующего слоя напишите через пробел значения строк, затем нажмите Enter. Когда размер слоя матрицы '
            'будет равен размеру других слоев, ввод слоя завершится.\nДля окончания ввода трехмерной матрицы введите '
            'пустой слой трехмерной матрицы.')
    while True:
        line = [i for i in input().split()] # ввод строки в матрицу
        if matrix == [] and len(line)!=0 and length_of_matrix == -1:
            matrix.append(line) # Если матрица еще пустая то просто добавляем любую строку
        elif matrix == [] and len(line)==0:
            out_flag = 1
            break
        elif len(line)==0 and length_of_matrix == -1:
            print("Ввод первого слоя матрицы завершен")
            break

        elif len(matrix[0]) == len (line) and length_of_matrix == -1 or length_of_matrix != -1 and len(matrix_3d[0][0]) == len (line): # если длина строки равна длине первой строке, иначе выводим ошибку и просим
            # повторить ввод
            matrix.append(line)
        else:
            print(f'\033[31mОшибка. Длина строк в матрице должна совпадать с длиной строк в первой матрице, и должна быть равна {len(matrix_3d[0][0])}.\nПовторите ввод!\033[0m')
        if len(matrix) == length_of_matrix:
            break
    if out_flag == 1 and matrix_3d!=[]:
        print("Ввод трехмерной матрицы завершен.\n")
        break
    elif out_flag == 1 and matrix_3d == []:
        print("\033[31mОшибка. Вы ввели пустую трёхмерную матрицу, повторите ввод!\n\033[0m")
        out_flag = 0
    else:
        matrix_3d.append(matrix)
        if length_of_matrix ==-1:
            length_of_matrix = len(matrix)
while True:

    i = int(input("Выберите I-тый срез: "))
    if 0<i<=len(matrix_3d):
        break
    else:
        print("\033[31m\nОшибка. Вы ввели несуществующий срез, повторите ввод!\n\033[0m")
for line in matrix_3d[i-1]:  # вывод
    for el in line:
        print(f' {el} ', end='')
    print()