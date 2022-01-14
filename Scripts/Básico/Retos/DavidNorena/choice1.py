def par_impar():
    number = int(input("digita el número que deseas evaluar...:"))
    try:
        if(abs(number) % 2 == 0):
            print("el número es par")
        else:
            print("El número es impar")

        input("Presiona enter para continuar")
        return ""
    except:
        print("el valor que ingresaste no es un número, hasta la proxima")
        input("Presiona enter para continuar")
        return ""
