name  = ["Meet","Kuldip","Sagar","Uttam","Jeet","Himanshu"]
birth_year = [1999,2000,2000,2003,1998,1997]

zip_result = zip(name,birth_year)
print(list(zip_result))            #type casting = iterator object to list.
#print(dict(zip_result))


#set function for set in order.
a = [5,4,2,1,3]
print("Set in order: ",set(a))

#set function for set in order with remove duplicate.
a = [5,4,1,2,3,1,3]
print("Set in order with remove duplicate: ",set(a))