import math


def integer_log_base_2(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    count = 0
    while n > 1:
        n = n // 2
        count += 1

    return count


# Пример использования:
n = 16
result = integer_log_base_2(n)
print(result)  # Вывод: 4, так как 2^4 = 16


# Эта функция также имеет логарифмическую сложность O(logn),
# поскольку на каждом шаге количество рассматриваемых элементов делится на 2.