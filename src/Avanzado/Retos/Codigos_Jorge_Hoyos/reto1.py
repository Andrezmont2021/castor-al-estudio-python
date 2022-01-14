# Reto 1: Verificar si un número pasado por parámetro es par o impar

def reto_par():   
    num = int(input("Ingrese el número que desea evaluar: ")) 
    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
    return True
