# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 7, задание 4
array = input().split()
for i in range(len(array)):
    for letter in 'aeiouy':
        array[i] = array[i].replace(letter,letter.upper())

print(*array)