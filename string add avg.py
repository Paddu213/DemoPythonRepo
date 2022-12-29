str_a=input()
l=len(str_a)
sum=0
avg=0
count=0
for i in range(l):
    if str_a[i].isdigit()==True:
        sum=sum+int(str_a[i])
        count=count+1
avg=sum/count
print(sum)
print(avg)
