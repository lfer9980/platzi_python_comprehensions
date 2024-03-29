def sum_with_range(min, max):
    print(min, max)
    sum = 0 
    for x in range(min,max):
        sum += x
    return sum

suma_1 = sum_with_range(1,15)
print(suma_1)

suma_2 = sum_with_range(suma_1, suma_1 + 10)

print(suma_2)