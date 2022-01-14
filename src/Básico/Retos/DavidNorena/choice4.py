def accumulated_numbers():
    number = input("digita la lista de números separados por puto y coma ; ...:")
    try:
        numbers= number.split(";")
        accumulated = []
        n = len(numbers)
        p = 0
        while p < n:
            if(p == 0):
                accumulated.append(int(numbers[p]))
            else:
                accumulated.append(int(numbers[p])+int(numbers[p-1]))

            p+=1

        print(f"la lista de numeros ingresada fue: {numbers}")
        print(f"la lista de numeros acumulada es: {accumulated}")
        input("Presiona enter para continuar")
        return ""

    except:
        print("el valor que ingresaste no es un número, hasta la proxima")
        input("Presiona enter para continuar")
        return ""
