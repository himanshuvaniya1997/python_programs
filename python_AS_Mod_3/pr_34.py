#WAP to print all unique values in a dictionary.

my_dict = {'a':10,'b':20,'c':10,'d':30,'e':20}
unique_values = set(my_dict.values())
print(unique_values)
                        #or
print(my_dict.values())
uniq = []
for i in my_dict.values():
    if i not in  uniq:
        uniq.append(i)
print(uniq)
