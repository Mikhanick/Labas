# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 6, защита
array = [int (i) for i in input("Введите массив: ").split()] #
array_old = array.copy()
chets = []
nechets = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        chets.append(array[i])
    else:
        nechets.append(array[i])
for i in range(len(array)):
    if array[i] % 2 != 0:
        if len(chets)==0:
            print(array[i],end=' ')
        else:
            print(chets.pop(0),end=' ')
    else:
        if len(nechets)==0:
            print(array[i], end=' ')
        else:
            print(nechets.pop(0), end=' ')