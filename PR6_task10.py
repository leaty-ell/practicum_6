def rectangle_position(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 < x3 or x4 < x1 or y2 > y3 or y4 > y1:
        return "Прямоугольники лежат вне друг друга, не касаясь"
    if x2 == x3 or x4 == x1 or y2 == y3 or y4 == y1:
        return "Прямоугольники имеют касание"
    if x1 < x4 and x2 > x3 and y1 > y4 and y2 < y3:
        return "Прямоугольники имеют пересечение"
    if x1 >= x3 and x2 <= x4 and y1 <= y3 and y2 >= y4:
        return "Один прямоугольник лежит внутри другого, не касаясь"
    if x3 >= x1 and x4 <= x2 and y3 <= y1 and y4 >= y2:
        return "Один прямоугольник лежит внутри другого, не касаясь"
    return "Прямоугольники имеют пересечение"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

result = rectangle_position(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)