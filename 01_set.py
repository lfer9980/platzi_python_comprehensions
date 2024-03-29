set_countries = {'col', 'mex', 'bol', 'col'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,1,2,3,4,5}
print(set_numbers)

set_types = {1,'hola', False}
print(set_types)


set_from_string = set('hooola')
print(set_from_string)

set_from_tuple = set(('abf', 'dsad', 'asd'))
print(set_from_tuple)

numbers = [1,2,3,4,5,5,6,1,2,1]
set_numbers_list = set(numbers)
print(set_numbers_list)

""" convertir de conjunto a otro objeto """

unique_numbers = list(set_numbers_list)
print(unique_numbers)
