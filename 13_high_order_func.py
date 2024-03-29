def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)


value = high_ord_func(10, increment)

print(value)


