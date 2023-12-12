def seven(text):
    mn_k = -1
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбюёЁ-'
    # функция по обнаружению и удалению необходимого предложения

    position_of_sentence = list()
    start_of_this_sentence = [0, 0]
    min_len_word_in_sentence = -1
    len_word = 0
    for index_line, line in enumerate(text):
        for sym in range( len(line)):
            if line[sym] in letters:
                len_word += 1
            else:
                if min_len_word_in_sentence == -1 or len_word < min_len_word_in_sentence:
                    min_len_word_in_sentence = len_word
                    len_word = 0
            if line[sym] == '.':
                if min_len_word_in_sentence < mn_k or mn_k == -1:
                    position_of_sentence = [start_of_this_sentence, [index_line, sym]]
                    mn_k = min_len_word_in_sentence
                    min_len_word_in_sentence = -1
                start_of_this_sentence = [index_line, sym+1]  # ищем позицию начала и конца предложения с максимальным
    # количеством слов, начинающихся на заданную букву
    if not position_of_sentence:  # если не было найдено предложение ничего не делаем
        print('Необходимое предложение не найдено')
        return text

    else:  # выводим и вырезаем предложения удовлетворяющие условию
        for line in range(position_of_sentence[0][0], position_of_sentence[1][0] + 1):
            if line != position_of_sentence[0][0] and line != position_of_sentence[1][0]:
                print(text[line])
                text[line] = ''
            else:
                if position_of_sentence[0][0] == position_of_sentence[1][0]:
                    print(text[line][position_of_sentence[0][1]:position_of_sentence[1][1] + 1])
                    text[line] = text[line][:position_of_sentence[0][1]] + text[line][position_of_sentence[1][1] + 1:]
                elif line == position_of_sentence[0][0]:
                    print(text[line][position_of_sentence[0][1]:])
                    text[line] = text[line][:position_of_sentence[0][1]]
                else:
                    print(text[line][:position_of_sentence[1][1] + 1])
                    text[line] = text[line][position_of_sentence[1][1] + 1:]
        return text
text = ['На краю дороги стоял дуб. Вероятно в десять раз старше берез, составлявших лес, он был в десять раз толще и',
        'в два раза выше каждой березы. Это был огромный в два обхвата дуб с обломанными, давно видно, суками и с',
        'обломанной корой, заросшей старыми болячками. С огромными своими неуклюжими,',
        'несимметрично-растопыренными !привет , меня зовут',
        'корявыми руками и пальцами, он старым, сердитым и презрительным уродом стоял между',
        'улыбающимися березами. Только он один не хотел подчиняться обаянию весны',
        'и не хотел видеть ни весны, ни солнца. 4+++3-- 3 -3+4- 3+-6 -+ 8-6',
        '-1+1 a -1-2 a 1--1 a 1---1 a 1 -+ 1',
        '1 +- 1 a 1 - 1 +++ 1 - 1',
        '--1-+1+-1++1']
print(text)
print(seven(text))