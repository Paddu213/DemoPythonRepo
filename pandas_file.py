import pandas as pd

#df_csv=pd.read_csv('pokemon_data.csv')
df_csv=pd.read_csv("C:/Users/user735/PycharmProjects/pythonProject/Pandas_project/pokemon_data.csv")

print(df_csv)
print(df_csv.head(5))
print(df_csv.tail(5))
print(df_csv["HP"])
print(df_csv["Type 1"])
df_csv["total"]=df_csv["HP"]+df_csv["Defense"]+df_csv["Attack"]
print(df_csv)
df_csv=df_csv.drop(columns=["total"])
print(df_csv)
print(df_csv["Type 2"])


#filling empty space in Type 2 column  with "hi"
print(df_csv)
df_csv["Type 2"].fillna('hi',inplace=True)
print(df_csv.to_string())
#modifieng the csv
df_csv.to_csv('E:\\modified1.csv',index=True)


df_csv["add_num"]=df_csv["HP"]+df_csv["Defense"]
df_csv["add_str"]=df_csv["Type 1"]+df_csv["Type 2"]
print(df_csv)
df_csv.to_csv('E:\\modified2.csv',index=True)

df_csv["Odd_sum"]=df_csv["Attack"]+df_csv["Defense"]+df_csv["Speed"]
#df_csv["Odd_sum"]=df_csv.iloc[1::2,[False,False,False,False,False,True,True,False,False,True,False,False,False,False,False]].sum(axis=1)

#Index odd sum
df_csv["Odd_sum"]=df_csv.iloc[1::2,[5,6,9]].sum(axis=1)
print(df_csv)

#interchanging Type 1, Type 2
df_csv["Type 1"],df_csv["Type 2"]=df_csv["Type 2"],df_csv["Type 1"]
print(df_csv)

#col_list=list(df_csv.columns)
#print(col_list)
import numpy as np

li_a=df_csv.loc[df_csv["Name"].str.startswith("A")]
print(li_a)

#A column has index number (change it to date)
print(df_csv)
df_csv["dates"] = pd.date_range("20000101", periods=800)
df_csv.set_index("dates",inplace=True)
print(df_csv)

#Group by Type 1(numeric values)

print(df_csv.groupby(["Type 1"]).sum())







