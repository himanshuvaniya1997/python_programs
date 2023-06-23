#write a python code to replace last value of tuples in a list.

old_list = [(1,2,3),(4,5,6),(7,8,9)]
print(old_list)
new_list = [(li[0],li[1],li[2]+10) for li in old_list]   #list comprehension.
print(new_list)
