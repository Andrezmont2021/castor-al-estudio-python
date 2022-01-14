# Reto 5: Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10.
# Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

def lista_multiplos():
    num = int(input("Ingrese un número: "))
    multiplos = []                              # Lista vacía 

    x = 1                                       # Iterador

    for i in range (1, 11):
        mult = x * num
        multiplos.append(mult)
        x += 1

    print(multiplos)
    return True
