
# Задача 36: Напишите функцию вывода таблицы умножения print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы


def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows+1):
        for column in range(1, num_columns+1):
            result = operation(row, column)
            print(f'{result}\t', end='')
        print()

print_operation_table(lambda x, y: x * y)
