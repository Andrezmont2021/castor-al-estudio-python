def pair_numbers():
    number = int(input("digita valor que quieres alcanzar...:"))
    try:
        numbers=[]
        goal = number
        print(goal)
        n = 0

        if(goal >= 0):
            while n <= goal:
                if(n % 2 == 0):
                    numbers.append(n)
                n+=1
        else:
            while n >= goal:
                if(n % 2 == 0):
                    numbers.append(n)
                n-=1

        print(numbers)

        input("Presiona enter para continuar")
        return ""

    except:
        print("el valor que ingresaste no es un número, hasta la proxima")
        input("Presiona enter para continuar")
        return ""
