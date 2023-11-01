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
    min_index = -1
    max_index = -1
    min_sum = float('inf')
    max_sum = float('-inf')
    for i in range(len(matrix[0])):
        sm = 0
        for j in range(len(matrix)):
            sm += matrix[j][i]
        if 0 < sm < min_sum:
            # print('min new')
            min_sum = sm
            min_index = i
        if sm>max_sum:
            # print('max new')
            max_sum = sm
            max_index = i
        # print(sm,max_sum, min_sum)
    # print(max_index,min_index)

    for i in range(len(matrix)):
        matrix[i][max_index],matrix[i][min_index] = matrix[i][min_index],matrix[i][max_index]

    for line in matrix:
        print(*line)