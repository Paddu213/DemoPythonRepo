
#matrix

M=int(input())
N=int(input())
list_a=[]
for i in range(M):
    r=input().split()
    for j in r:
        list_a.append(j)
print(list_a)
list_a.sort()
k=0
for i in range(M):
    for j in range(N):
        print(list_a[k],end=" ")
        k=k+1
    print()


