def multiplication_table():
    number = input("digita el número al que deseas calcular la tabla...:")
    table = []
    try:
        for n in range(10):
            table.append(int(number)*(n+1))

        print(f"para el número {number}, la tabla de multiplicar es:")
        print(table)
        input("Presiona enter para continuar")
        return ""
    except:
        print("el valor que ingresaste no es un número, hasta la proxima")
        input("Presiona enter para continuar")
        return ""
