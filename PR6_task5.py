def move_valid(move):
    start, end = move.split('-')

    start_col_char = start[0].lower()
    end_col_char = end[0].lower()

    if start_col_char == 'a':
        start_col = 1
    elif start_col_char == 'b':
        start_col = 2
    elif start_col_char == 'c':
        start_col = 3
    elif start_col_char == 'd':
        start_col = 4
    elif start_col_char == 'e':
        start_col = 5
    elif start_col_char == 'f':
        start_col = 6
    elif start_col_char == 'g':
        start_col = 7
    elif start_col_char == 'h':
        start_col = 8
    else:
        return "ошибка"

    if end_col_char == 'a':
        end_col = 1
    elif end_col_char == 'b':
        end_col = 2
    elif end_col_char == 'c':
        end_col = 3
    elif end_col_char == 'd':
        end_col = 4
    elif end_col_char == 'e':
        end_col = 5
    elif end_col_char == 'f':
        end_col = 6
    elif end_col_char == 'g':
        end_col = 7
    elif end_col_char == 'h':
        end_col = 8
    else:
        return "ошибка"

    start_row = int(start[1])
    end_row = int(end[1])

    col_diff = abs(start_col - end_col)
    row_diff = abs(start_row - end_row)


    if ((col_diff == 2 and row_diff == 1) or
            (col_diff == 1 and row_diff == 2)):
        return "верно"
    else:
        return "ошибка"


move = input("Введите ход коня: ")
result = move_valid(move)
print(result)