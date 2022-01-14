# Advent of code, day 2, part 1. Calcular la posición x y y considerando los movimientos 
# hechos por el submarino

with open('c:/cursoP1/advent_calendar/datos_d2.txt', 'r') as f:
    x = f.read().split("\n")        #Lee el archivo de entrada y separa las lineas en strings
    data = []

    for i in x:
        data.append(i)              #Agrega cada linea del archivo a la lista data como un string
    #print(data)

    lista_sep = []
    x = 0
    y = 0

    for i in data:
        i = i.split()               #Toma cada string de data y la separa en dos string separados
        lista_sep.append(i)         #Cada string de data queda en una lista anidada dentro de la lista data

        if i[0] == "forward":
            x += int(i[1])
        elif i[0] == "down":
            y += int(i[1])
        else:
            y -= int(i[1])
    
    #print(lista_sep)
    print(f"el valor de x es: {x}")
    print(f"el valor de y es: {y}")
    print(f"el valor del producto es: {x*y}")