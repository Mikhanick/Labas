# Саватеев Михаил ИУ7-16Б
# Лабораторная работа номер 2 "Нахождение корней квадратного уравнения"
from typing import Tuple


def input_abc() -> tuple[float, float, float]:  # Блок программы с вводом данных
    while True:  # Цикл, пока пользователь не введет достоверные данные
        try:  # обрабатываем некорректный ввод пользователя
            a = float(input('Введите коэффициент a: '))  # счтываем a,b,samo_chislo
            b = float(input('Введите коэффициент b: '))
            c = float(input("Введите коэффициент samo_chislo: "))
            break  # выход из цикла при корректном вводе
        except ValueError:  # обработка исключения при некорректном вводе
            print('\033[31m\033[1mПроизошла ошибка, повторите ввод!\033[0m')  # вывод на экран сообщения об ошибке
    return a, b, c


def main(a: float, b: float, c: float) -> str:  # основной блок программы
    if a == 0:  # проверка условия на а
        if c == 0:  # проверка условия на b
            if b == 0:  # проверка условия на с
                out = 'X - любое число'
            else:
                out = 'X = 0'
        else:
            if b == 0:
                out = 'Корней нет'
            else:
                out = f'X = {convert_to_string(-c / b)}'
    else:
        D = b ** 2 - 4 * a * c  # рассчет Дискриминанта (D)
        if D > 0:

            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)

            out = f'X1 = {convert_to_string(x1)}\nX2 = {convert_to_string(x2)}'
        else:
            if D == 0:
                out = f'X = {convert_to_string(-b / (2 * a))}'
            else:
                out = 'Корней нет'
    return out


def convert_to_string(value: float) -> str:
    return f'{value:.7g}'  # привод числа к требуемому виду


def formatted_print(value: str):
    print()
    print(f'\033[32m\033[4m{value}\033[0m')  # вывод ответа с зеленым цветом шрифта и подчеркиванием


if __name__ == '__main__':
    while True:
        a, b, c = input_abc()
        answer = main(a, b, c)
        formatted_print(answer)
        if input('Введите любой символ чтобы выйти, нажмите Enter чтобы продолжить: ') != '':
            break
