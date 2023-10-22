max_len = 0  # инициализируем максимальную длину
array = [1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 7, 6, 5, 6, 7, 8, 3, 3, 3, 7, 11, 17, 21]
len_of_row = 0
index_of_start_row = 0
array.append(0) # добавляем нулевой элемент, чтобы не выйти за границы массива

for i in range(len(array) - 1): # ищем максимальную длину возрастающей последовательности
    if array[i + 1] == 1:
        simple1 = False
    for j in range(2, int(array[i + 1] ** 0.5) + 1): # проверяем, является ли следующий элемент простым
        if array[i + 1] % j == 0:
            simple1 = False
            break
    else:
        simple1 = True

    if array[i] == 1:
        simple = False
    for j in range(2, int(array[i] ** 0.5) + 1):
        if array[i] % j == 0:
            simple = False
            break
    else:
        simple = True

    if array[i] < array[i + 1] and simple and simple1: # если элементы возрастают и являются простыми, то увеличиваем длину
        len_of_row += 1 # увеличиваем длину на единицу
    else:
        if len_of_row > max_len: # если длина больше максимальной, то присваиваем ее значение максимальной
            max_len = len_of_row # присваиваем максимальной длине значение текущей длины
            index_of_start_row = i - len_of_row

        len_of_row = 0
for i in range(index_of_start_row, index_of_start_row + max_len + 1): # выводим элементы возрастающей последовательности
    print(array[i], end=' ')