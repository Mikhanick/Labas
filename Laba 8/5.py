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
    mx = float('-inf')
    mn = float('inf')
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            if i>j:
                mn = min(mn,matrix[i][j])
            if i<j:
                mx = max(mx,matrix[i][j])

    print(f'Максимальное: {mx} Минимальное: {mn}')