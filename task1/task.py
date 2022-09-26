# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# ​Пример:​[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]​
numbers = [1, 2, 3, 5, 1, 5, 3, 10]
list1 = []
for i in numbers:
    if numbers.count(i) < 2 and i not in list1:
        list1.append(i)

print(list1)