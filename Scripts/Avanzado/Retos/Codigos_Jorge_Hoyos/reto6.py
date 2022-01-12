# Escribe una función llamada "inversa" que busque todas las palabras inversas de una lista.
# Ejemplo de palabras inversas: radar, oro, rajar, rallar, salas, somos, etc...

def inversa():
    pal = input("Ingrese las palabras separadas por espacio: ").split()
    palabras = []

    for item in pal:
        palabras.append(item)
    
    for x in palabras:
        lista1 = list(x)                    # Convierte la palabra en lista de letras
        lista_inv = lista1[::-1]            # Crea una lista invertida a partir de la anterior
        if lista1 == lista_inv:             # Compara las dos listas creadas
            palind = ''.join(lista_inv)     # Si las listas son iguales, las vuelva string y la imprime
            print(palind)

    return True
