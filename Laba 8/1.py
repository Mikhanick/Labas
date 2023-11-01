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
    index_of_max = -1
    maxcnt = 0
    for index, line in enumerate(matrix):
        cnt = 0
        for el in line:
            if el%2==0:
                cnt+=1
        if cnt > maxcnt:
            index_of_max = index
            maxcnt = cnt
if index_of_max == -1:
    print("Не было введено строки, содержащей четные числа")
else:
    print(f'Наибольшее число четных элементов было в строке {index_of_max+1}: ',end='')
    print(*matrix[index_of_max])