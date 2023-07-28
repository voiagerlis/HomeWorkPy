import random
import time

def check_expression():
    X = random.choice([True, False])
    Y = random.choice([True, False])
    Z = random.choice([True, False])

    result_left = not (X or Y or Z)
    result_right = not X and not Y and not Z

    return result_left == result_right

start_time = time.time()

for _ in range(100):
    num_predicates = random.randint(3, 15)
    predicates = [random.choice([True, False]) for _ in range(num_predicates)]

    expression_result = not any(predicates)
    formula_result = check_expression()

    if expression_result != formula_result:
        print("Найдено неверное утверждение!")
        print("Предикаты:", predicates)
        break

end_time = time.time()
total_time = end_time - start_time

print("Время выполнения:", total_time)
