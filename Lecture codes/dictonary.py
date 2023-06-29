mydict = {908:"meet",765:"sagar",545:"kuldip",235:"uttam"}   #{keys:value}

print(mydict)
print(mydict[765])
mydict[545] = "jigar"   #add element in dictionary.
print(mydict)
mydict[111] = "kuldip"  #add element in dictionary.
print(mydict)

for i in mydict:
    print(i,":",mydict[i])    #print dictionary keys and its dictionary values.
    
#library functions of dictionary.

print(mydict.get(111))       #print value of key(111).
print(mydict.items())        #print or get all keys and its values of dictionary.
print(mydict.keys())         #print all keys of dictionary.
print(mydict.values())       #print all values of dictionary.
print(mydict.pop(545))       #remove or pop given keys and its value.
print(mydict) 
print(mydict.popitem())      #remove or pop last item.
print(mydict) 

mydict1 = {545:"jigar",111:"kuldip",222:"jeet",333:"himanshu"}
mydict.update(mydict1)       #add new dictionary at the end of previous dictionary. 
print(mydict)