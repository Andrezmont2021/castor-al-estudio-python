# Advent of code, day 1, part 2

with open('c:/cursoP1/advent_calendar/datos_d1.txt', 'r') as f:
    linea = f.readlines()
    lista = []
    for i in linea:
        lista.append(int(i))
    #print(lista)
    #print(len(lista))
    #print(lista.__class__)

    # En la lista de datos original, empieza a agrupar de a 3 valores y los suma hasta que ya no se puedan
    #formar más grupos de 3 y luego hace la comparación de valores para saber donde hay aumentos respecto
    #al valor anterior (siendo el valor anterior la suma de 3 números)
    incr = 0
    dec = 0
    list_sumas = []
    for x in range(len(lista)-2):
        suma = lista[x] + lista[x+1] + lista[x+2]
        list_sumas.append(suma)

        if list_sumas[x] > list_sumas[x-1]:
            incr += 1
        else:
            dec += 1
    print(f"Hay {incr} incrementos")
    print(f"Hay {dec} disminuciones")