def all_divisors(number):
    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    divisors.sort()
    return divisors

numbers = [23436, 190187200, 380457890232]

for number in numbers:
    divisors = all_divisors(number)
    print("Делители числа", number, ":", divisors)
