def count_expression(expression, sym):
    if sym == '^':
        return f'{int(float(expression) ** 2)}'
    else:
        return f'{int(float(expression) ** 0.5)}'


def find_arithmetics(line):
    array_to_replace = []
    expression = ''
    start = 0
    flag_new = 0
    for index_sym, sym in enumerate(line):
        if sym in '1234567890' and expression == '':
            start = index_sym
            expression = sym
            flag_new = 1
        elif sym in '1234567890' and flag_new:
            expression += sym
        elif sym in '^#' and expression!='':
            flag_new = False
            expression = count_expression(expression, sym)
        elif sym == ' ':
            pass
        else:
            if expression != '':
                array_to_replace.append([line[start:index_sym], expression])
                expression = ''
            if sym in '1234567890':
                expression = sym
                start = index_sym

    if expression != '':
        array_to_replace.append([line[start:], expression])
    return array_to_replace


def arithmetical(text: list[str]):
    for line in range(len(text)):
        array = find_arithmetics(text[line])
        for item in array:
            print(item)
            text[line] = text[line].replace(item[0], item[1], 1)
    return text


def print_text(text: list[str]):  # вывод текста
    print()
    for line in text:
        print(line)
    print()


def main():
    from text import text
    print_text(text)
    text = arithmetical(text)
    print('##############')
    print_text(text)


if __name__ == '__main__':
    main()
