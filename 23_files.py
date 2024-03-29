file = open('./text.txt')
#print(file.read())
""" print(file.readline())
print(file.readline())
print(file.readline())
print(file.readlines()) """

""" una forma de ahorrar memoria """
for line in file: 
    print(line)

""" es necesario cerrar los archivos despues de usarlos para liberar memoria """
file.close()

""" sintaxis mas amigable para abrir y cerrar archivos """
with open('./text.txt') as file:
    for line in file:
        print(line)