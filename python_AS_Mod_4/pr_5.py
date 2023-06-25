#write a python program to read a file line by line and store it into a list.

list_of_text = []
n_file = open("textfile.txt","r")  
for line in n_file:
    list_of_text.append(line)
print(list_of_text)
n_file.close()
                  #or
n_file = open("textfile.txt","r")                  
new_list = []
new_list = n_file.readlines()
print(new_list)
n_file.close()

