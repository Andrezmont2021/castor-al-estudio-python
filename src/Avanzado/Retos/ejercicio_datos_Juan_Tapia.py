#programa para importar datos y analizar los cambios
close=[]
lista1=[]
with open("data1.txt", "r") as archivo:
    lista1=((archivo.readlines()))
    for line in lista1:
        close.append(line.split(",")[0])
lista1=[int(i) for i in lista1]      #cambiar a numero en lista 

#print(lista1) 
#print(len(lista1))
incre=0
decre=0
for n in range(1,len(lista1)):
    if lista1[n]>lista1[n-1]:
        incre=incre+1
#    else:
#        decre=decre+1
print ("numero de veces que incrementa: " , (incre))
#print ("numero de veces que disminuye: " , (decre))



