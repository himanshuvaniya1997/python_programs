#write code for convert a list of characters into string.

my_list = [1,2,3,'vaniya',5,6,8]
str_list = str([str(i) for i in my_list])      #here used list comprehension.
print(str_list)
