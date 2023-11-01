matrix = []
print('Для ввода матрицы напишите через пробел значения строк, затем нажмите Enter. По окончании ввода строк нажмите '
      'Enter')
while True:
    line = [int(i) for i in input().split()]
    if matrix == []:
        matrix.append(line)
    elif line == []:
        print('Ввод матрицы завершен.')
        break
    elif len(matrix[0]) == len (line):
        matrix.append(line)
    else:
        print(f'Ошибка. Длина строк в матрице должна совпадать, и должна быть равна {len(matrix[0])}.\nПовторите ввод!')
if len(matrix) == 0:
    print("Ошибка. Вы ввели пустую матрицу. Работа программы завершена с ошибкой!")
else:

    max_cnt = float('-inf')
    min_cnt = float('inf')

    index_max = -1
    index_min = -1

    for i in range(len(matrix)):
        cnt = 0
        for j in matrix[i]:
            if j < 0:
                cnt += 1
        #print('cnt =', cnt,'max count', max_cnt,'min_count', min_cnt)
        if cnt>max_cnt:
            max_cnt = cnt
            index_max = i

        if cnt < min_cnt and cnt > 0:
            min_cnt = cnt
            index_min = i

    #print(index_max,index_min)
    if index_min > -1 and index_max > -1:
        matrix[index_max], matrix[index_min] = matrix[index_min],matrix[index_max]

    for line in matrix:
        print(*line)