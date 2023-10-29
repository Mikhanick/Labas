# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 6, задание 5

array = [-1, 0, 1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 7, 6, 5, 6, 7, 8]  # инициализируем массив
max_positive = 0
min_positive = 0
index_of_max_positive = 0  # инициализируем индексы максимального и минимального положительных элементов
index_of_min_positive = 0
for i in range(len(array)):  # ищем максимальный и минимальный положительные элементы
    if max_positive == 0 and array[i] > 0:  # если максимальный положительный элемент еще не найден, то присваиваем
        # ему значение первого положительного элемента
        max_positive = array[i]
        index_of_max_positive = i
    if min_positive == 0 and array[
            i] > 0:  # если минимальный положительный элемент еще не найден, то присваиваем ему значение первого
        # положительного элемента
        min_positive = array[i]
        index_of_min_positive = i
    if array[i] > 0 and array[
            i] > max_positive:  # если текущий элемент больше максимального положительного, то присваиваем ему значение
        # максимального положительного
        max_positive = array[i]
        index_of_max_positive = i
    if 0 < array[
            i] < min_positive:  # если текущий элемент меньше минимального положительного, то присваиваем ему значение
        # минимального положительного
        min_positive = array[i]
        index_of_min_positive = i
array[index_of_max_positive] = min_positive  # меняем местами максимальный и минимальный положительные элементы
array[index_of_min_positive] = max_positive
print(*array)
