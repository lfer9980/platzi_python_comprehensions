try:
    print(0/0)
    assert 1 !=1, 'Uno no es igual que uno'
    age = 10 
    if age < 18:
        raise Exception('error de de edad')
    
except ZeroDivisionError as error:
    print('Error')
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('Hola')