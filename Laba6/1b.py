
# Создаем массив
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Вводим индекс
index = int(input('Введите индекс: '))
# Вводим элемент
element = int(input('Введите элемент: '))
# Создаем новый array
new_list = []
# Перебираем array
for i in range(len(array)):
    # Если индекс равен индексу введенному пользователем
    if i == index:
        # Добавляем элемент в новый array
        new_list.append(element)
    # Добавляем элемент из старого списка в новый
    new_list.append(array[i])
# Выводим новый array
print(new_list)
