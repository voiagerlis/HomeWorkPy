number = float(input("Введите вещественное или целое число: "))

sum_of_digits = 0
if number < 0:
 number = abs(number)

if number.is_integer():
 while number >= 1:
  digit = number % 10
  sum_of_digits += int(digit)
  number = number // 10
else:
 while number - int(number) != 0:
  number *= 10
while number >= 1:
 digit = number % 10
 sum_of_digits += int(digit)
 number = number // 10

print("Результат сложения цифр числа:", sum_of_digits)
