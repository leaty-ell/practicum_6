import math

def carpet(arena_radius, A, B):
    diameter = 2 * arena_radius
    diagonal = math.sqrt(A**2 + B**2)
    return diagonal <= diameter

arena_radius = 6.5
size_input = input("Введите размеры ковра: ")
A, B = map(float, size_input.split('x'))

if carpet(arena_radius, A, B):
    print("Да")
else:
    print("Нет")