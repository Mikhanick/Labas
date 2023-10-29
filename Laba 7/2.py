# Саватеев Михаил группа ИУ7-16Б
# Лабораторная работа номер 7, задание 2
array = [int(i) for i in input().split()]
len_array = len(array)
adds = 0
for i in array:
    if i%2==0:
        adds += 1

array+=[None]*adds
add_i = len_array
for i in range(len_array):
    if array[i]%2==0:
        array[add_i] = array[i]*2
        add_i+=1

print(*array)
add_i = len_array
last_change = False
for i in range(len(array)):
    if ((add_i-len_array)==0) and (array[i]%2!=0):
        continue
    if array[i]%2==0 and ((add_i-len_array)==0) or array[i]%2==0 and last_change==False:
        add_i+=1
        last_change = True
        # array[len_array],array[add_i-1] = array[add_i-1],array[len_array]
    else:
        last_change = False
    if not(i> len_array):
        array[i+1],array[add_i-1] = array[add_i-1],array[i+1]

    print(*array)
    print('  '*i+'^')
