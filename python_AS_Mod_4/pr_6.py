#write a python program to read a file line by line and store it into a variable.

filename = "textfile.txt"
lines = []
with open(filename) as file:
    for line in file:
        lines.append(line.strip())
print(lines)        
var1 = lines[0]
var2 = lines[1]

for i in range(2):
    print("var",i+1,":-",lines[i])
file.close()    
