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


prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    item['taxes'] = item['price']*0.19
    return(item)

""" problemas con ref de memoria """
items_cp = items.copy()
new_items = list(map(add_taxes, items_cp))
print(new_items)
print(items_cp)