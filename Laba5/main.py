while True:
    x = float(input('Введите значение аргумента: '))
    if x > 0:
        break
    else:
        print('Введено некорректное значение! Аргемент должен быть положительным.')
while True:
    accuracy = float(input('Введите необходимую точность ряда: '))
    if accuracy > 0:
        break
    else:
        print('Введено некорректное значение! Точность ряда должна быть положительна.')

while True:
    max_iter = int(input('Введите максимальное количество итераций: '))
    if max_iter > 1:
        break
    else:
        print('Введено некорректное значение! Максимальное значение итераций должно быть больше единицы.')

while True:
    step_print = int(input('Введите шаг печати: '))
    if step_print >= 1:
        break
    else:
        print('Введено некорректное значение! Шаг печати должен быть больше либо равен единицы.')

# y = x/1 + x^2/2 + x^n/n
y = 0
flag = True
print('+' + '-' * 36 + '+')
print('| № Итерации |     t     |     s     |')
print('+' + '-' * 36 + '+')
for n in range(1, max_iter + 1):
    f = x ** n / n
    y = y + f
    if (n - 1) % step_print == 0:
        print(f'| {n:<10.5g} | {f:^9.5g} | {y:^9.5g} |')
    if f < accuracy:
        break
else:
    if f >= accuracy:
        flag = False
print('+' + '-' * 36 + '+')
if flag:
    print(f'Сумма бесконечного ряда - {y:.7g}. вычислена за {n} итераций.')
else:
    print(f'Достигнуто максимальное количество итераций. Сумма бесконечного ряда: {y:7g}')
