
s1=input()
s2=input()
print(s1[:3]==s2[:3])

n1=input()
n2=input()
print(n1[0]<n2[-1])

n=list(map(int,input()))
m=input()
s=n*int(m)
print(s)

m=int(input())
p=int(input())
c=int(input())
if(m>=70 and p>=60 and c>=80 and (m+p+c)>=180):
    print("satisfied")
else:
    print("not satisfied")

    m = int(input())
    p = int(input())
    c = int(input())
    if (m >= 70 or p >= 60 and c >= 80 or (m + p + c) >= 180):
        print("satisfied")
    else:
        print("not satisfied")

    m = int(input())
    p = int(input())
    c = int(input())
    if (m >= 70 or p >= 60 or c >= 80 or (m + p + c) >= 180):
        print("satisfied")
    else:
        print("not satisfied")

        str1 = input()
        print(str1.swapcase())







list_a = list(map(int, input().split(' ')))
set_a = set(list_a)
print(type(set_a))
list_b = list(set_a)