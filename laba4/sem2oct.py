import math

LENGTH = 60
MAX_AMPLITUDE = 30
X_SCALE = 0.4
Y_SCALE = 1.8
FUNCTION = '(x)**0.5'
FUNCTION2 = '-(x)**0.5'


def make_matrix(x: int, y: int, empty_value='   ') -> list[list]:
    arr = []
    for i in range(x):
        arr.append([empty_value] * (y * 2))
    return arr


def draw_function(matrix: list[list], length=40, max_amplitude=20, x_scale=1.0, y_scale=1.0, function='math.sin(x)',
                  graphic_symbol='мяу', leave_extra_dots=True) -> list[list]:
    if leave_extra_dots:
        for i in range(length):
            x = i * x_scale
            # func = (math.exp(x)-math.exp(-x))/2
            try:
                func = eval(function)
                # print(func)
                func = func * y_scale
                # print(max(-max_amplitude, min(max_amplitude, round(func))) + max_amplitude - 1)
                matrix[i][max(-max_amplitude, min(max_amplitude, round(func))) + max_amplitude - 1] = graphic_symbol
            except ZeroDivisionError:
                pass
    else:
        for i in range(length):
            x = i * x_scale
            # func = (math.exp(x)-math.exp(-x))/2
            try:
                func = eval(function)
                # print(func)
                func = func * y_scale
                # print(max(-max_amplitude, min(max_amplitude, round(func))) + max_amplitude - 1)
                if abs(func) <= max_amplitude:
                    matrix[i][round(func) + max_amplitude - 1] = graphic_symbol
            except Exception:
                pass

    return matrix


def print_matrix(matrix: list[list]):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[j][-i - 1], end='')
        print('\n', end='')
    # print(matrix)


if __name__ == '__main__':
    graphic = make_matrix(LENGTH, MAX_AMPLITUDE)
    print(len(graphic))
    graphic = draw_function(graphic, x_scale=X_SCALE, y_scale=Y_SCALE, function=FUNCTION, leave_extra_dots=False,
                            length=LENGTH, max_amplitude=MAX_AMPLITUDE, graphic_symbol='гав')
    graphic = draw_function(graphic, x_scale=X_SCALE, y_scale=Y_SCALE, function=FUNCTION2, leave_extra_dots=False,
                            length=LENGTH, max_amplitude=MAX_AMPLITUDE, graphic_symbol='гав')
    print_matrix(graphic)
