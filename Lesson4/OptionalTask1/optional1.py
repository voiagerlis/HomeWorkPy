def decimal_to_base(num: int, base: int) -> str:
    result = ""
    while num > 0:
        ost= num % base
        result = str(ost) + result
        num = num // base
    return result
number = int(input("Введите целое число: "))

binary = decimal_to_base(number, 2)
print(f"Двоичное представление числа {number}:", binary)

octal = decimal_to_base(number, 8)
print(f"Восьмеричное представление числа {number}:", octal)

print("Проверка двоичного представления числа:", bin(number))
print("Проверка восьмеричного представления числа:", oct(number))
