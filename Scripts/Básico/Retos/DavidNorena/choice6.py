from menu import print_menu

def palindromos():
    more_words = "S"
    words = []
    palindromos = []
    no_palindromos = []
    while more_words.upper() == "S":
        print_menu()
        print(words)
        words.append(input("Digita la palabra que deseas validar..:"))
        more_words = input("Deseas agregar mas palabras? s/n..:").upper()
    
    for word in words:
        if str(word) == str(word)[::-1]:
            palindromos.append(word)
        else:
            no_palindromos.append(word)
    
    print(f"""
    Las palabras palindromas son..:
    {palindromos}

    Las palabras no palindromas son..:
    {no_palindromos}
    
    """)
    input("presiona una tecla para conitnuar")
    return ""
