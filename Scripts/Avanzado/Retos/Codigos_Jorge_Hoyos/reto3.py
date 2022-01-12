# Reto 3: Listar los números pares del 10 al 20

#Forma 1: indicando los incrementos en el rango

from reto5 import lista_multiplos


def pares():
    num1 = int(input("Ingrese el primer número del rango: "))
    num2 = int(input("Ingrese el segundo número del rango: "))
    lista_pares = []
    for num in range(num1,num2,2):
        lista_pares.append(num)
    print(lista_pares)
    return True


#Forma 2: Usando condicional dentro del bucle
#for numero in range(10, 21):
#    if numero % 2 == 0:
#        print(numero)