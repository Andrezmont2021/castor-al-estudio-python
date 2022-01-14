with open("C:/CursoP1/cursoP1/retos-calendario/datosdia-1.txt", "r") as f: 
    contents = f.readlines()
    lista=[]
    for i in contents:
        lista.append(int(i))
    print(len(lista))

    lista_suma=[]
    for i in range(0, len(lista)-2):
        x=lista[i]+lista[i+1]+ lista[i+2]
        lista_suma.append(x)
    


    incremento=0
    disminucion=0

    for i in range (1, len(lista_suma)):
        if lista_suma[i]> lista_suma[i-1]:
            incremento+=1
        else:
            disminucion+=1

    print(f"Hay: {incremento} incrementos")
    print(f" Hay: {disminucion} disminuciones")