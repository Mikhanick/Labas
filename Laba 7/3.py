# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 7, задание 3
array = input().split()
max_word = ''
max_cnt = 0
for i in array:
    cnt = 0
    for letter in "AEIOUYaeioyu": # будем заменять все гласные буквы англицкого алфавита
        cnt += i.count(letter)
    if cnt>max_cnt:
        max_word = i
        max_cnt = cnt

if max_word == '':
    print("Нет слов, содержащих гласные буквы")
else:
    print(max_word)
