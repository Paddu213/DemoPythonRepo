#unordered collection of items.it has key_value pairs

dict_a={"name":"paddu",
        "age":21,
        "roll no":13}
result='name' in dict_a
print(result)
print(dict_a)
print(dict_a['name'])
print(dict_a.get('name'))



dict_a['city']="ap"
dict_a['country']="india"
print(dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())
dict_a['age']=22
del dict_a['age']
print(dict_a)



dict_a={"name":"paddu",
        "age":21,
        "roll no":13}
for key in dict_a.keys():
    print(dict_a[key])
print()
for key in dict_a.keys():
    print(key)



dict_a={"name":"paddu",
        "age":21,
        "roll no":13}
"""if 'name' in dict_a:
    print("True")"""
dict_a={"name":"paddu",
        "age":21,
        "roll no":13}
dict_a.clear()
print(dict_a)
print(len(dict_a))
for key,value in dict_a.items():
    pair="{} {}".format(key,value)
    print(pair)
for value in dict_a.values():
    print(value)
keys_list=list(dict_a.keys())
print(keys_list)


