#write a python code to count the number of lines in a text file.

def count_lines(file):
    count = 1
    lines = file.readlines()
    for line in lines:
        if line.endswith("\n"):
            count = count + 1
    return count

filename = open("textfile.txt","r")
total_lines = count_lines(filename)
print("Total Number Of Lines In a Text File: ",total_lines)        
filename.close()              
