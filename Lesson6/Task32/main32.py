# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

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
