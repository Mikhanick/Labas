# # Саватеев Михаил группа ИУ7-16Б
# # Лабораторная работа номер 7, задание 2




# array = [int(i) for i in input().split()]
# len_array = len(array)
# adds = 0
# for i in array:
#     if i%2==0:
#         adds += 1
#
# array+=[None]*adds
# add_i = len_array
# for i in range(len_array):
#     if array[i]%2==0:
#         array[add_i] = array[i]*2
#         add_i+=1
#
# print(*array)
# # add_i = len_array
# # last_change = False
# # for i in range(len(array)-1):
# #     if ((add_i-len_array)==0) and (array[i]%2!=0):
# #         continue
# #     if array[i]%2==0 and ((add_i-len_array)==0) or array[i]%2==0 and last_change==False:
# #         add_i+=1
# #         last_change = True
# #         #array[len_array],array[add_i-1] = array[add_i-1],array[len_array]
# #     else:
# #         last_change = False
# #     if not(i> len_array and 0):
# #         array[i+1],array[add_i-1] = array[add_i-1],array[i+1]
# #
# #     print(*array)
# #     print('  '*i+'^')
# for i in range(len(array),-1,-1):
#
# array = [int(i) for i in input("Введите список, разделяя элементы пробелом: ").split()]
#
# len_a = len(array)
#
# if array==[]:
#     print("Ошибка, массив пуст")
# else:
#     adds = 0
#     for i in array:
#         if i%2==0:
#             adds += 1
#
#     array+=[None]*adds
#
#     for i in range(len_a - 1, -1, -1):
#         if array[i] % 2 == 0:
#             array[i + adds] = array[i] * 2
#             array[i + adds - 1] = array[i]
#             adds -= 1
#     else:
#         array[i + adds] = array[i]
#
#     print(*array)
#
#





array = [int(i) for i in input("Введите список: ").split()]

len_a = len(array)

if array==[]:
    print('Список должен содержать хотя бы 1 элемент.')
else:
    adds = 0
    for i in array:
        if i%2==0:
            adds += 1

    array+=[None]*adds #расширяем длину масива чтобы мы могли изменять массив, на необходимую

    for i in range(len_a - 1, -1, -1): # перебираем элементы массива с конца
        if array[i] % 2 == 0: # в конец добавляем элементы из списка и их удвоенные, если числа четные
            array[i + adds] = array[i] * 2
            array[i + adds - 1] = array[i]
            adds -= 1 #сдвигаем конец последовательности
        else:
            array[i + adds] = array[i]
print(*array) #выводим массив