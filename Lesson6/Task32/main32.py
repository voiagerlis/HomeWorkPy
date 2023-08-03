import random

def find_index(lst, minimum, maximum):
    indices = []

    for i, value in enumerate(lst):
        if minimum <= value <= maximum:
            indices.append(i)

    return indices

lst = [random.randint(-100, 100) for _ in range(10)]

min = 33
max = 200

indices = find_index(lst, min, max)

print("Оригинальный список:")
print(lst)
print("Минимум:", min)
print("Максимум:", max)
print("Индексы элементов, принадлежащих заданному диапазону:")
print(indices)
