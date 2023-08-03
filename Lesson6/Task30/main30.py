def fill_progres():

    a1 = int(input("Введите первый элемент прогрессии: "))
    d = int(input("Введите разность прогрессии: "))
    n = int(input("Введите количество элементов: "))
    progres = []

    for i in range(n):
        progres.append(a1 + i * d)

    return progres

result = fill_progres()
print("Массив элементов прогрессии:")
print(result)
