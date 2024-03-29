import random
countries = ['col', 'mex', 'bol', 'pe']

population = {country: random.randint(1,100) for country in countries}
print(population)

result = { country:pob for (country, pob) in population.items() if pob >= 20 }
print(result)


text = 'Hola, soy Luis'

unique = { c:c.upper() for c in text if c in 'aeiou'}
print(unique)