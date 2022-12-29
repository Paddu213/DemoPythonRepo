list_a=list(map(int,input()))
for i in list_a:
    if str(i).isdigit()==True:
        continue
    else:
        list_a.remove(i)
print(list_a)


list_a=list(input())
list_b=[]
for i in list_a:
    if i.isdigit()==True:
        list_b.append(i)
    else:
        break
print(list_b)

list_a=list(map(str,input()))
list_b=[]
for i in list_a:
    if str(i).isdigit()==True:
        list_b.append(i)
print(list_b)


