def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'

result = find_volume(1,2,3)

print(result[2])