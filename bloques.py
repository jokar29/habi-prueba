def ordenar_bloques(myArray):
    resultado = []
    bloque = []

    for num in myArray:
        if num != 0:
            bloque.append(num)
        else:
            if bloque:
                resultado.append(''.join(sorted([str(num) for num in bloque])))
            else:
                resultado.append('X')
            bloque = []

    # Ultimo bloque si no termina con cero
    if bloque:
        resultado.append(''.join(sorted([str(num) for num in bloque])))

    return ' '.join(resultado)

# aplicacion
myArray = (1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1)
resultado_bloques = ordenar_bloques(myArray)
print(resultado_bloques)