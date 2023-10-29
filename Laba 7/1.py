# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 7, задание 1
# 3 2 1 6 - варианты
array = [int(i) for i in input().split()]
ind = 0
delete = 0
l = len(array)
is_last_0 = 0
while True:
    if array[ind]==0:
        delete+=1
    else:
        array[ind-delete] = array[ind]
        #print(ind,"|",delete,"|",*array)
    ind+=1
    if ind>=l:
        break
print(*array[:l-delete])

