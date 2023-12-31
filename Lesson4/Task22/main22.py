#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def find_common_elements(n, m):
    set1 = set()
    set2 = set()

    print("Введите элементы первого множества:")
    for _ in range(n):
        num = int(input())
        set1.add(num)

    print("Введите элементы второго множества:")
    for _ in range(m):
        num = int(input())
        set2.add(num)

    common_elements = set1.intersection(set2)

    print("Общие элементы, в порядке возрастания:")
    for num in sorted(common_elements):
        print(num)

n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))
find_common_elements(n, m)
