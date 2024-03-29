numbers = [1,2,3,4]

new_numbers = []

for i in numbers:
    new_numbers.append(i * 2)

numbers_map = list(map(lambda i: i *2, numbers))

print(new_numbers)
print(numbers_map)


""" map hace cosas bien chidas """
numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)