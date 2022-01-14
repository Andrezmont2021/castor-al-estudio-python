def duplicate_values():
    number = input("digita la lista de números separados por puto y coma ; ...:")
    try:
        numbers= number.split(";")
        unique_numbers = set(numbers)
        repeated = []
        
        if(len(numbers) == len(unique_numbers)):
            print("No hay números reptidos en la lista")
        else:
            for number in unique_numbers:
                if(numbers.count(number)>1):
                    repeated.append(number)
            print(f"Los números repetidos en la lista son..: {repeated}")
        
        input("Presiona enter para continuar")
        return ""

    except:
        print("Uno de los valores que ingresaste no es un número, hasta la proxima")
        input("Presiona enter para continuar")
        return ""