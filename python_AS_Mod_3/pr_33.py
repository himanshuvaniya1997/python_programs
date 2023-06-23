#write a python program to combine two dictionary adding values for common keys.
#d1 = {'a':100,'b':200,'c':300} , d2 = {'a':300,'b':200,'d':400}
#sample output = Counter({'a':400,'b':400,'d':400,'c':300})

d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}

combine_dict = {}
for key in d1:
    if key in d2:
        print(key,"Exists in my_dictionary")
        combine_dict[key] = d1[key] + d2[key]
    else:
        for key1 in d2:
            if key1 not in d1:
                combine_dict[key1] = d2[key1]
        print(key,"Does not exists in my_dictionary")
        combine_dict[key] = d1[key]
print(combine_dict)        

                     #or
from collections import Counter
comb_dict = {}
comb_dict  = Counter(d1) + Counter(d2)
print(comb_dict)
