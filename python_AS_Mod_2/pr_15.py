#code for add 'ing' at the end of given string(length should be atleast 3).
#if a given string already ends with 'ing' then add 'ly',if str len of given str is less than 3 than unchanged.

my_str = input("enter the string: ")
print("length of given string: ",len(my_str))

if len(my_str) < 3:
    print("unchanged string")
elif my_str.endswith("ing"):
    my_str = my_str + "ly"
elif len(my_str) >= 3:
    my_str = my_str + "ing"
        
print(my_str)    
