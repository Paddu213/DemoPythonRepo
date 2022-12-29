str_1=input()
str_2=input()
list_1=list(str_1)
list_2=list(str_2)
count=0
while(True):
    count=count+1
    m=list_2[0]
    list_2.remove(m)
    list_2.append(m)
    if list_1==list_2:
        break
print(count)
