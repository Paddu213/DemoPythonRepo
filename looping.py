
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










 str="11-11-00"
 str=str.replace("-","/")
 print(str)


 str1=input()
 str2=str1[::-1]
 print(str2==str1)

 password=input()
 n=len(password)
 for i in range (n):
     if(upp=0)
         pass


     

 #sum of n natural  numbers

 n=int(input())
 sum=0
 for i in range(n):
     sum=sum+i
     i=i+1
 print(sum)



 #sum of given numbers
 n=input()
 sum=0
 for i in n:
     sum=sum+int(i)

 print(sum)

 #product of given numbers

 n1=int(input())
 n2=int(input())
 print(n1*n2)

 #print solid square
 n=int(input())
 for i in range(n):
     for j in range(n):
         print("*",end=" ")
     print()


     #print right angle triangle

 n=int(input())
 for i in range(n):
     for j in range(n):
         if(j<=i):
             print("*",end=" ")
     print()


#print solid rectangle
 n1=int(input())
 n2=int(input())
 for i in range(n1):
     for j in range(n2):
            print("*",end=" ")
     print()
 print("\n")

#reverse right angle triangle

n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

  #reverse right angle triangle
    n = int(input())
    for i in range(n):
        for j in range(n - i):
            print(" ", end=" ")
            if(i+j>=n-1):
                print("*",end=" ")
            if (i + j >= n - 1):
                print("*", end=" ")
        print()

    set_c=set([1,2,3])
    print(set_c)
    print(type(set_c))

    list_a=list(map(int,input().split(' ')))
    set_a=set(list_a)
    print(type(set_a))

    list_b=list(set_a)
    print(list_b)





