#write a python program to copy the contents of a file to another file.

my_file = open("myfile.txt","r")
contents = my_file.read()
print("my_file contents: ",contents)
my_file.close()

my_filecopy = open("myfilecopy.txt","w")
my_filecopy.write(contents)
my_filecopy.close()

my_filecopy = open("myfilecopy.txt","r")
new_contents = my_filecopy.read()
print("my_filecopy contents:",new_contents)
my_filecopy.close()
