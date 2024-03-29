""" 
numbers = []

for element in range(1,11):
    numbers.append(element*2)
print(numbers)

#list comprehensions
numbers_list = [element*2 for element in range(1,11)]
print(numbers_list) 
"""

numbers = []

for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i*2)
    
print(numbers)

#list comprehensions
numbers_list = [i*2 for i in range(1,11) if i %2 == 0]
print(numbers_list)