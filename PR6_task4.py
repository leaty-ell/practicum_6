def color(cell):
    column_letter = cell[0].lower()
    if column_letter == 'a':
        column = 1
    elif column_letter == 'b':
        column = 2
    elif column_letter == 'c':
        column = 3
    elif column_letter == 'd':
        column = 4
    elif column_letter == 'e':
        column = 5
    elif column_letter == 'f':
        column = 6
    elif column_letter == 'g':
        column = 7
    elif column_letter == 'h':
        column = 8
    else:
        return "неверные координаты"

    row = int(cell[1])

    if (column + row) % 2 == 0:
        return "черный"
    else:
        return "белый"

cell = input("Введите координаты клетки: ")
color = color(cell)
print(color)