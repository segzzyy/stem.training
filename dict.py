from typing import ItemsView


mydict={
        "book":"dynamic",
        "publisher" : "longhorn",
        "year": "2001",
        "authors":["john,milke,dan"]}


#accessing item
x=mydict["year"]
print(x)

#accesing using get()
y=mydict["year"]
print(y)


#all keys
x=mydict.keys()
print(x)

#all values
x=mydict.Items