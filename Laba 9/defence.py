# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 9, задание 7
matrix_3d = []
o = 0
u = int(input('Введите N длину куба: '))
for i in range(u):
    matrix_3d.append([])
    for j in range(u):
        matrix_3d[-1].append([])
        for k in range (u):
            o+=1
            matrix_3d[-1][-1].append(o)
    for line in matrix_3d[-1]:
        for el in line:
            print(f'{el:5.5g}',end=' ')
        print()
    print()

# typ = input('введите по какой координате срез: ')
i = int(input("Выберите I-тый срез: "))
for typ in 'xyz':
    ln = len(matrix_3d) if typ == 'y' else len(matrix_3d[0]) if typ == 'z' else len(matrix_3d[0][0])

    print('срез по', typ)
    if typ == 'y':
        for line in range(len(matrix_3d)):
            for el in range(len(matrix_3d[0][0])):
                print(f'{matrix_3d[line][i-1][el]:^5.5g}',end=' ')
            print()
    elif typ == 'z':
        for line in range(len(matrix_3d[0])):
            for el in range(len(matrix_3d[0][0])):
                print(f'{matrix_3d[i-1][line][el]:^5.5g}',end=' ')
            print()
    else:
        for line in range(len(matrix_3d)):
            for el in range(len(matrix_3d[0])):
                print(f'{matrix_3d[line][el][i-1]:^5.5g}',end=' ')
            print()
    print()
'''
          / Y
         /
        /
        ------------- X
        |
        |
        |
        | Z
        '''