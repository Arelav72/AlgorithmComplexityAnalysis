def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Пример использования:
result = sum_list([1, 2, 3, 4, 5])
print(result)  # Вывод: 15

# Эта функция имеет линейную сложность  𝑂(𝑛),
# так как количество операций (в данном случае, сложений) прямо пропорционально
# размеру входного списка numbers.