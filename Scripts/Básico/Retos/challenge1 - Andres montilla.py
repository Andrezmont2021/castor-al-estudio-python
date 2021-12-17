# Request an input from the user
value = int(input("Enter a integer number to verify if it's pair: "))
# Calculate if the input is pair
if(value % 2 == 0):
    print("The number is pair")
else:
    print("The number is not pair")