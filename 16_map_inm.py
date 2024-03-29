items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'jeans',
        'price': 200
    }
]


""" prices = list(map(lambda item: item['price'], items))
print(prices) """

""" problemas con ref de memoria """
def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price']*0.19
    return new_item

new_items = list(map(add_taxes, items))
print(items)
print(new_items)
