def rascheska_sort(array):
    n = len(array)
    cnt = 0
    step = n
    flag = 0
    while step > 1 or flag:
        if step > 1:
            step = int(step/1.28)
        i = 0
        flag = 0
        while i + step <n:
            if array[i] > array[i+step]:
                temp_el = array[i]
                array[i] = array[i+step]
                array[i+step] = temp_el
                cnt+=1
                flag = 1
                #print(array)
            i+=step
    return array, cnt

def bubble_sort(array):
    n = len(array)
    cnt = 0
    flag = 1
    while flag:
        flag = 0
        for i in range (0,n-1):
            if array[i]>array[i+1]:
                temporary_elem = array[i]
                array[i] = array[i+1]
                array[i+1] = temporary_elem
                cnt+=1
                flag = 1
                if i+2 == n:
                    n-=1
                # print(array)
    return array, cnt

def binary_search(array: list, elem: float, start: int = 0, end: int = 0) -> int:  # бинарный поиск
    if end == 0:  # если конец не задан, то задаем его
        end = len(array)
    if elem < array[start]:  # если элемент меньше первого, то возвращаем первый индекс
        return start
    elif elem >= array[end - 1]:  # если элемент больше последнего, то возвращаем последний индекс
        return end
    index = end // 2
    if array[index] == elem:  # если элемент равен элементу по индексу, то возвращаем индекс
        return index + 1
    elif array[index] > elem:  # если элемент больше элемента по индексу, то сдвигаем конец
        high_index = index
        low_index = start
    else:
        high_index = end - 1
        low_index = index
    while high_index - low_index != 1:  # пока разница между индексами не равна 1
        index = (high_index + low_index) // 2
        array_by_index = array[index]
        if array_by_index > elem:
            high_index = index
        elif array_by_index < elem:
            low_index = index
        else:
            return index + 1
    return high_index

def gnome_sort(array):
    cnt = 0
    i = 0
    size = len(array)-1
    while i < size:
        if array[i]<=array[i+1]:
            i+=1
        else:
            temp_elem = array[i]
            array[i] = array[i+1]
            array[i+1] = temp_elem
            cnt+=1
            # print(array)
            if i>0:i-=1
    return array, cnt


def simply_insert_sort(array):
    cnt = 0
    ln = len(array)-1
    for edge in range(ln):
        new_element = array[edge+1]
        j = edge
        while j>=0 and array[j]>new_element:
            array[j+1] = array[j]
            array[j] = new_element
            cnt+=1
            # print(array)
            j-=1
    return array, cnt

def barrier_insert_sort(array):
    array = [0]+array
    cnt = 0
    ln = len(array)-1
    for edge in range(ln):
        array[0] = array[edge+1]
        j = edge
        while array[j]>array[0]:
            array[j+1] = array[j]
            array[j] = array[0]
            cnt+=1
            # print(array)
            j-=1
    del array[0]
    return array, cnt


def shell_sort(array):
    ln = len(array)
    delta = int(ln * 0.618)
    cnt = 0
    while delta > 0:

        for i in range(delta, ln):
            k = 1
            while i - k*delta>=0:
                j = i - delta
                if array[i] < array[j]:
                    temp_elem = array[j]
                    array[j] = array[i]
                    array[i] = temp_elem
                    cnt += 1
                i = j
                k += 1
        delta = int(delta*0.618)

    return array, cnt



def insert_binary_sort(array: list) -> tuple[list, int]:  # сортировка вставками
    cnt = 0
    ln = len(array)-1
    for barier in range(ln):  # перебираем элементы
        new_element = array[barier + 1]
        new_index = binary_search(array, new_element, end=barier + 1)
        for i in range(barier + 1, new_index, -1):  # сдвигаем элементы
            cnt += 1
            temporary_elem = array[i]
            array[i] = array[i - 1]
            array[i - 1] = temporary_elem
        array[new_index] = new_element
    return array, cnt