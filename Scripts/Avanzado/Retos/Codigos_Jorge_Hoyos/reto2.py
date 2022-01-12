# Reto 2: Dados dos números, decir cuál es mayor o si son iguales

def reto_mayor():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if num1 > num2:
        print("%s es mayor que %s" %(num1, num2))
    elif num1 < num2:
        print("%s es mayor que %s" %(num2, num1))
    else:
        print("Los números son iguales")
    return True
