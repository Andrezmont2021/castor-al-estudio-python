import os
from reto1 import reto_par
from reto2 import reto_mayor
from reto3 import pares
from reto4 import list_acum
from reto5 import lista_multiplos
from reto6 import inversa
continuar = True

while continuar:
    os.system("cls")
    print("""---------------- RETOS ----------------
    1. Evaluar si un número es par o impar
    2. Comparar 2 números y evaluar cuál es mayor
    3. Listar los números pares en un rango
    4. Lista de suma acumulada
    5. Tabla de multiplicar de un número
    6. Buscar palabras palíndromas en una lista
    7. Salir
    ---------------------------------------""")
    try:
        ret = int(input("Ingrese el número de reto que desea evaluar: "))
        if ret == 1:
            continuar = reto_par()
        elif ret == 2:
            continuar = reto_mayor()
        elif ret == 3:
            continuar = pares()
        elif ret == 4:
            continuar = list_acum()
        elif ret == 5:
            continuar = lista_multiplos()
        elif ret == 6:
            continuar = inversa()
        elif ret == 7:
            continuar = False
        input("Presione enter para continuar...")
    except:
        print("No ingresó un número, vuelva a intentar")
        input("Presione enter para continuar...")
        continuar = True