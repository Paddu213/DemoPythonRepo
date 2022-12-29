list_a=list(map(int,input().split(' ')))
set_a=set(list_a)
list_b=list(set_a)
print(list_b)


set_a=set(input())
set_b=set(input())
diff=set_a-set_b
print(diff)

set_a=set(input())
set_b=set(input())
print(set_a & set_b)


list_a=list(map(int,input()))
for i in list_a:
    if i.isdigit:
     continue
    else:
     list_a.remove(i)

print(list_a)


