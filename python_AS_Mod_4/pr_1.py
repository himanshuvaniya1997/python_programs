#write a python program to read an entire text file.

txt_file = open("textfile.txt","r")
read = txt_file.read()
print(read)
txt_file.close()
