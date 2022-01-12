# Toma datos de un archivo .txt y compara cada valor con el anterior

with open('c:/cursoP1/advent_calendar/datos_d1.txt', 'r') as f:
    linea = f.readlines()       #Lee las lineas y genera una lista de strings
    lista = []
    for i in linea:
        lista.append(int(i))
    #print(linea)
    #print(lista)
    #print(len(lista))
    #print(lista.__class__)
    
    incr = 0                    #Contador de aumentos, comparando cada valor con el anterior
    dec = 0
    for x in range(1,len(lista)):
        if lista[x] > lista[x-1]:
            incr += 1
        else:
            dec += 1
    print(f"Hay {incr} incrementos")
    print(f"Hay {dec} disminuciones")