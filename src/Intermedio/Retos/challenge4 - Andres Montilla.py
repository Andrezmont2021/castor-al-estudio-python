# Define a function that get a number list and return the sum of all the numbers in the list.
def sumAcumList(list):
    finalList=[list[0],list[0]+list[1]]
    for i in range(2,len(list)):
        finalList.append(finalList[i-1]+list[i]) 
    return finalList

list = [1,2,3,4,5]
finalList = sumAcumList(list)
print(finalList)