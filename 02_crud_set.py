set_countries = {'col', 'mex', 'bol', 'col'}

size = len(set_countries)
print(size)

print('col' in set_countries)

#add 
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)


#remove
set_countries.remove('ar')
print(set_countries)

"""set_countries.remove('bol')"""
set_countries.discard('us')
print(set_countries)

set_countries.clear()
print(set_countries)
