#write a python program to read first n lines of a file.

n = int(input("Enter the num of lines you want to read from file: "))
n_file = open("textfile.txt","r")
for num in range(n):
    print(n_file.readline())
n_file.close()    
