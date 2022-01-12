# Advent of code, day 3, part 1. Calcular las variables gamma y epsilon considerando los binarios 
# Considering only the first bit of each number, there are five 0 bits and seven 1 bits. 
# Since the most common bit is 1, the first bit of the gamma rate is 1.
#The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
# So, the gamma rate is the binary number 10110, or 22 in decimal
#The epsilon rate is calculated in a similar way; rather than use the most common bit, 
# the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. 
# Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

with open('c:/cursoP1/advent_calendar/datos_d3.txt', 'r') as f:
    x = f.read().split("\n")       #Lee el archivo de entrada y lo organiza en lista de strings
    data = []

    for i in x:
        i = list(i)             #Transforma cada número en una lista
        data.append(i)

gamma = ""
epsilon = ""

for b in range(0, len(data[0])):
    one = 0
    zero = 0
    for c in range(0,len(data)):
        if data[c][b] == "0":
            zero +=1
        else:
            one +=1
    if zero > one:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
    
g = int(gamma, 2)
e = int(epsilon, 2)
print(f"Gamma is {gamma}")
print(f"Epsilon is {epsilon}")
print(f"Gamma = {g}")
print(f"Epsilon = {e}")
print(f"Part 1: {g *e}")
