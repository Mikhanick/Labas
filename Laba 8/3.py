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
    index = -1
    min_cnt = float('inf')
    for i in range (len(matrix[0])):
        cnt = 0
        for j in range (len(matrix)):
           if matrix[j][i]<0:
               cnt+=1
        if 0<cnt<min_cnt:
            min_cnt = cnt
            index = i

    if index>-1:
        for i in range(len(matrix)):
            print(matrix[i][index])
    else:
        print('Нет колонки с отрицательным элеменетом')