array = [1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 7, 6, 5, 6, 7, 8]
index_of_extremum = 0
wanted_index = int(input("Введите номер экстремума, который хотите найти: "))
for i in range(1, len(array) - 1):  # ищем экстремум
    if array[i - 1] < array[i] > array[i + 1] or array[i - 1] > array[i] < array[
            i + 1]:  # если элемент больше обоих соседних или меньше них, то он экстремум
        index_of_extremum += 1
    if wanted_index == index_of_extremum:  # если номер экстремума равен номеру текущего экстремума, то выводим его
        print(array[i])
        break
else:
    print("Такого экстремума нет!")
