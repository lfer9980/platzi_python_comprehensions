price = 100

def increment(price):
    price = 200
    result = price + 10
    print(result)
    return result

print(price)
price_2 = increment(price)
print(price_2)