with open("C:/CursoP1/cursoP1/retos-calendario/datosdia-1.txt", "r") as f: 
    contents = f.readlines()
    lista=[]
    for i in contents:
        lista.append(int(i))
    print(len(lista))

    incremento=0
    disminucion=0

    for i in range (1, len(lista)):
        if lista[i]> lista[i-1]:
            incremento+=1
        else:
            disminucion+=1

    print(f"Hay: {incremento} incrementos")
    print(f" Hay: {disminucion} disminuciones")