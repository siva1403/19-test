names=[]
numbers=[]
list=['bharath',23,'ravi',45,'raju',78]
for i in list:
    if type(i)==str:
        names.append(i)
    if type(i)==int:
        numbers.append(i) 
print("separation of names are:",names)
print("separation of numbers are:",numbers)
