# Write a function named capital_indexes. The function takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]

def capital_indexes(string):
    stri = list(string)
    upper_ind = []
    index = 0
    for i in stri:
        if i.isupper() == True:
            upper_ind.append(index)
        index += 1
    
    print(upper_ind)
    return(upper_ind)
    

capital_indexes("HeLLoGeOrGIE")