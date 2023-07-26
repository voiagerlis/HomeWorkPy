# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def print_degree_square(n):
    count = 0
    current_two = 1
    while current_two <= n:
        print(current_two)
        count += 1
        current_two = 2 ** count

num = int(input("Введите число N: "))
print_degree_square(num)
