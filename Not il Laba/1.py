''' дана матрица Б 8х8 содержащая 0 и 1,
 причем с каждой единицей (в строке или с толбце) расположены только 2 единицы
таким образом, циклическая последовательность единиц ограничивае область из одних нолей, такйти количество нулей в
области
также могут быть горизонтальные или вертикальные линии и одинокие единицы
'''

# matrixB = [
#     [1, 1, 1, 0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 1, 0, 1, 0],
#     [1, 1, 1, 0, 1, 0, 1, 0],
#     [1, 1, 1, 1, 0, 0, 1, 0],
#     [0, 0, 0, 1, 0, 0, 1, 0],
#     [0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0]
# ]

matrixB = [
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]


def diagonal_search_and_mark(matrix, i, j):
    mx = max(2, matrix[i - 1][j - 1], matrix[i - 1][j + 1], matrix[i - 1][j], matrix[i][j - 1])

    if matrix[i][j] == 0: matrix[i][j] = mx + 1


change = 1
while change:
    change = 0
    for i in range(8):
        for j in range(8):
            if (i == 0 or j == 0 or i == 7 or j == 7) and matrixB[i][j] == 0:
                matrixB[i][j] = -1
            elif matrixB[i][j] == 0 and (
                    matrixB[i - 1][j] == -1 or matrixB[i][j - 1] == -1 or matrixB[i + 1][j] == -1 or matrixB[i][
                j + 1] == -1):
                matrixB[i][j] = -1
                change = 1

for line in matrixB:
    for el in line:
        print(f'{el:3.3g}', end=' ')
    print()

for i in range(8):
    for j in range(8):
        if matrixB[i][j] == 0:
            diagonal_search_and_mark(matrixB, i, j)

out_mx = 0
for line in matrixB:
    for el in line:
        out_mx = max(out_mx, el)

print(out_mx - 1)

for line in matrixB:
    for el in line:
        print(f'{el:3.3g}', end=' ')
    print()
