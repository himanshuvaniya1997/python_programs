#write a python program to append text to a file and display the text.

txt_file = open("textfile.txt","r+")
print(txt_file.read())
txt_file.write("\n_____THIS IS A DEMO OF APPENDED TEXT INTO THE EXIST FILE____")
print(txt_file.read())
txt_file.close()
                   #or           
t_file = open("textfile.txt","a")                 
t_file.write("\nAPPENDED TEXT INTO THE EXIST FILE USING 'a'=append MODE")
t_file = open("textfile.txt",mode = "r")
print(t_file.read())
t_file.close()
