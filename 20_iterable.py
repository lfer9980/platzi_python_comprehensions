my_iter = iter(range(1,11))
print(my_iter)

""" con los iteradores puedes controlar la forma en que se ejecutan los iteradores """

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

""" hacer esto es muy bueno para la memoria, no se crea todo un vector, solo se itera lo que se necesita """