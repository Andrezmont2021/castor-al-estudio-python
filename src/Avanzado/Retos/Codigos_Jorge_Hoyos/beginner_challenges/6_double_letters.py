# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. 
# For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
# Define a function named double_letters that takes a single parameter. The parameter is a string. 
# Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(string):
    data = list(string)
    yes = 0
    for i in range(0,len(data)-1):
        if data[i] == data[i+1]:
            yes += 1
    if yes != 0:
        print(True)
        return True
    else:
        print(False)
        return False

double_letters("Hello")