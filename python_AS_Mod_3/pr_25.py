#WAP to convert a list of tuples into a dictionary.

list_of_tup = [(10,20,30),(40,50,60),(70,80,90),(100,110,120)]
indi_list = [item for tuple in list_of_tup for item in tuple]   #list comprehension.

my_dict = {}
for i in range(len(indi_list)): 
   my_dict[i] = indi_list[i]
print(my_dict)
