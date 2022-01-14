def bigger_number():
    print("Ingresa los números que deseas evaluar")
    number1 = int(input("digita el primer número que deseas evaluar...:"))
    number2 = int(input("digita el segundo número que deseas evaluar...:"))
    try:
        if(number1 > number2):
            print(f"el número {number1} es el mayor")
        elif(number2 > number1):
            print(f"el número {number2} es el mayor")
        else:
            print("ambos números son iguales")

        input("Presiona enter para continuar")
        return ""
    except:
        print("el valor que ingresaste no es un número, hasta la proxima")
        input("Presiona enter para continuar")
        return ""