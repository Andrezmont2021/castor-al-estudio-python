# Reto 4: Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, 
# una nueva lista donde el primer elemento es el mismo, # el segundo elemento es la suma del primero con el segundo, 
# el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente.
#  Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6]. 

def list_acum():
    num = input("Ingrese los números separados por espacio: ").split()

    numeros = []                    # Crea una lista vacía
    for item in num:
        numeros.append(int(item))   # Convierte los números ingresados en int y los agrega a la lista vacía

    acumulado = [numeros[0]]

    for x in range(len(numeros)-1):
        suma = acumulado[x] + numeros[x+1]
        acumulado.append(suma)

    print(acumulado)

    return True

