my_file = open("numbers.txt", "r")
content_list = my_file.readlines()
final_list = list(enumerate(content_list))
count = 0
for index, item in final_list:
    if(index!=0):
        previousItem=str(final_list[index-1][1])
        if(int(item.strip())>int(previousItem.strip())):
            count+=1    
print(count)

#1692