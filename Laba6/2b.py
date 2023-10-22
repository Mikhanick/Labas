print('Введите список:')
a = list(map(int, input().split()))
print('Введите индекс:')
i = int(input())
for j in range(i, len(a) - 1):
    a[j] = a[j + 1]
a.pop()
print(a)