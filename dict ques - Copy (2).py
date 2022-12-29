#update value of particular key

dict_a={'name':'paddu',
        'age':22,
        'place':'mrkp'}
print(dict_a)
dict_a['name']='padmavathi'
print(dict_a)


#remove a key
dict_a={'name':'paddu',
        'age':22,
        'place':'mrkp'}
print(dict_a)
del dict_a['name']
print(dict_a)

#pre filled code will contain dictionary..
dict_a={'name':'paddu',
        'age':22,
        'place':'mrkp'}
key=input()
dict_a[key]='hello'
print(dict_a)


#squares of keys
dict_a={}
M=int(input())
for i in range(1,M+1):
        key=i
        value=i*i
        dict_a[key]=value
print(dict_a)


list_1=list(map(str,input().split()))
list_2=list(map(str,input().split()))
n=len(list_1)
count=0
for i in range(n):
        m=list_2[0]
        list_2.remove(m)
        list_2.append(m)
        if list_1!=list_2:
                count=count+1

print(count)




