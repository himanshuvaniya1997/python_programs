#wirte a python program to generate and print list of first 5 and last 5 elements from generated list.
#where the elements value are square of numbers b/w 1-30.

my_list = [i**2 for i in range(1,31)]   #here used list comprehension.
print(my_list)

New_list =  my_list[:5] + my_list[-5:]
print("First 5 & last 5 elements: ",New_list)
