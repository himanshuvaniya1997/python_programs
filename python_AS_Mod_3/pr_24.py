#WAP to unzip a list of tuples into individual list.

list_of_tup = [(1,2,3),(4,5,6),(7,8,9)]
individual_list = []    

for item in list_of_tup:
    for i in range(len(item)):
        individual_list.append(item[i])
print(individual_list)    
    
                  #or
indi_list = [item for tuple in list_of_tup for item in tuple]   #list comprehension.
print(indi_list)
