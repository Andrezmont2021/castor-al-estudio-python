# -*- coding: utf-8 -*-
from menu import print_menu
from choice1 import par_impar
from choice2 import bigger_number
from choice3 import pair_numbers
from choice4 import accumulated_numbers
from choice5 import multiplication_table
from choice6 import palindromos
from choice7 import duplicate_values

choice = ""
while choice.upper() != "Q":
    print_menu()
    choice = input("Por favor elije tu opción ")
    if(choice == "1"):
        choice = par_impar()
    elif(choice == "2"):
        choice = bigger_number()
    elif(choice == "3"):
        choice = pair_numbers()
    elif(choice == "4"):
        choice = accumulated_numbers()
    elif(choice == "5"):
        choice = multiplication_table()
    elif(choice == "6"):
        choice = palindromos()
    elif(choice == "7"):
        choice = duplicate_values()
