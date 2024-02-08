def escoger_genero(genero):
    if genero == 'F':
        return 'F (Femenino)'
    elif genero == 'M':
        return 'M (Masculino)'
    else:
        return 'Género equivocado'

genero = input('Ingrese el género (F o M): ')
print(escoger_genero(genero))