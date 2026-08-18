thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "brand": "For",
}
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

thisdict = dict(name = "john", age = 36, country = "Norway")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020
}
x = thisdict["model"]
print(x)
thisdict.update({"year":1964})
print(thisdict)
thisdict.update({"color": "red"})
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

thisdict = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
}
mydict = thisdict.copy()
print(mydict)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)

child1 = {
    "name": "Emil",
    "year": 2004 
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
}
print(myfamily)
print(myfamily["child2"] ["name"])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2024
}
print(thisdict["model"])

thisdict.update({"color": "red"})
print(thisdict)
thisdict.pop("brand")
print(thisdict)
print(thisdict)



    



























     
