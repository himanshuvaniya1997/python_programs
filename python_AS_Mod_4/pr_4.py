#write a python program to read last n lines of a file.

n = int(input("Enter the num of lines you want to read from file: "))
n_file = open("textfile.txt","r")
lines = n_file.readlines()
for num in range(-n,0):
    print(lines[num])
n_file.close()    
