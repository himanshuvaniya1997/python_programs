#WAP to find the highest 3 values in a dictionary.

my_dict = {'a':10,'b':50,'c':30,'d':20,'e':100}
print(my_dict.values())
sort_dict = sorted(my_dict.values())
print(sort_dict)
highest_3_values = sort_dict[-1:-4:-1]
print("Highest 3 values: ",highest_3_values)
