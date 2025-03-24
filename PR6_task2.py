def hole(A, B, C, D, E):
    hole_sz = sorted([A, B])
    brick_sz = sorted([C, D, E])

    if brick_sz[0] <= hole_sz[0] and brick_sz[1] <= hole_sz[1]:
        return True
    return False

A, B = map(float, input("Введите размеры отверстия: ").split('x'))
C, D, E = map(float, input("Введите размеры кирпича: ").split('x'))

if hole(A, B, C, D, E):
    print("Да")
else:
    print("Нет")
