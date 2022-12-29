list_a=list(map(int,input()))
k=int(input())
n=len(list_a)
list_b=[]
for i in range(n):
    for j in range(n):
        if(i!=j):
            if(list_a[i]+list_a[j])==k:
                p=tuple(set((str(list_a[i]), str(list_a[j]))))
                if p not in list_b:
                    print(p)
                    list_b.append(p)


list_a=list(map(int,input()))
n=len(list_a)
k=int(input())
list_b=[]
for i in range(n):
    for j in range(i+1,n):
        if(list_a[i])+(list_a[i+1])==k:
            list_c=[list_a[i],list_a[i+1]]
            list_b.append(list_c)
            print(list_b)