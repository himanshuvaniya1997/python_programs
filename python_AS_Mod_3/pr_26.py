#Write a python script to sort(ascending,descending) a dictionary by value. 

rand_dict = {1:70,2:10,3:50,4:20,5:40}
print(rand_dict)

ascending_dict = dict(sorted(rand_dict.items(),key = lambda item:item[1]))
descending_dict = dict(sorted(rand_dict.items(),key = lambda item:item[1],reverse=True))
print(ascending_dict)
print(descending_dict)
