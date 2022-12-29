def greet(arg_1,arg_2):
    return arg_1,arg_2
print(greet(arg_1="paddu",arg_2=213))


def fun(arg1):
    msg=arg1+'HCL'
    return msg
print(fun(arg1='welcome '))


def squarefun(str_a):
    list_str=list(str_a)
    list_1=[]
    for i in list_str:
        if i.isdigit():
            list_1.append(int(i)**2)
    return list_1
n=input()
s=squarefun(n)
print(s)


def isdiv(n):
    if n%7==0:
        return True
    else:
        return False
n=int(input())
check=isdiv(n)
print(check)


def area(l):
    area=l*l
    return area
def perimeter(l):
    per=4*l
    return per
l=int(input())
ar=area(l)
pe=perimeter(l)
print(ar)
print(pe)


#second value in string
def sec():
    list_str=list(str_a)
    return list_str[1]
str_a=input()
print(sec())



#lower and upper
def lower():
    n=0
    for i in str_a:
        if i.islower():
            n=n+1
    return n
def upper():
    m=0
    for i in str_a:
        if i.isupper():
            m=m+1
    return m
str_a=input()
print(lower())
print(upper())




#sum,minimum,maximum
def sum():
    sum=0
    for i in list_a:
        sum=sum+int(i)
    return sum
def min():
    min=list_a[0]
    for i in range(len(list_a)):
        if min>list_a[i]:
            min=list_a[i]
    return min
def max():
    max=list_a[0]
    for i in range(len(list_a)):
        if max<list_a[i]:
            max=list_a[i]
    return max
str_a=input()
list_1=list(str_a)
list_a=[]
for i in list_1:
    if str(i).isdigit()==True:
        list_a.append(i)
print(sum())
print(min())
print(max())




#factorial
def fact(p):
    if p==1:
        return 1
    elif p==0:
        return 1
    else:
        p=p*fact(p-1)
        return p
p=int(input())
print(fact(p))



#remove occurances of N in list

def occur(N):
    for i in list_a:
        if i==N:
            list_a.remove(i)
    return list_a
list_a=list(map(int,input()))
N=int(input())
print(occur(N))



# macro polo
def div(n):
    if n%3==0 and n%5==0:
        return "MacroPolo"
    elif n%5==0:
        return "Polo"
    elif n%3==0:
        return "Macro"
    else:
        return "no"
n=int(input())
print(div(n))



def result():
    win=wins*4
    draw=draws*2
    loss=losses*(-1)
    return ("wins are :"+str(win)+", draws are :"+str(draw)+", losses are :"+str(loss))
wins=int(input())
draws=int(input())
losses=int(input())
print(result())



#discount amount

def dis(bill):
    if