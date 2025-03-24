import math

def circle_position(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    sum_radii = r1 + r2
    diff_radii = abs(r1 - r2)


    if distance > sum_radii:
        return "Окружности лежат одна вне другой, не касаясь"
    elif distance == sum_radii:
        return "Окружности имеют внешнее касание"
    elif distance < sum_radii and distance > diff_radii:
        return "Окружности пересекаются"
    elif distance == diff_radii:
        return "Окружности имеют внутреннее касание"
    else:
        return "Одна окружность лежит внутри другой, не касаясь"


x1 = float(input())
y1 = float(input())
r1 = float(input())

x2 = float(input())
y2 = float(input())
r2 = float(input())

result = circle_position(x1, y1, r1, x2, y2, r2)
print(result)
