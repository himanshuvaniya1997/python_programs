#create or open text file  and write mode at python folder.
file = open("demofile.txt","w")
file.write("this is a demo text file create using python")
file.close()
print("............file written successfully in PYTHON PROGRAMS...........")

#create or open text file and write mode at d drive.
file = open("D:\\demofile1.txt","w")
file.write("this is a demo text file create using python")
file.close()
print("............file written successfully in D drive...........")

#open file in read mode. read mode only if file was already exist.
file = open("demofile.txt","r")
print(file.read())
file.close()

#open file in append mode. append data at last of the file content.
file = open("demofile.txt","a")
file.write("\nNow this file is appended")
file.close()
file = open("demofile.txt","r")
print(file.read())
file.close()

#open file in w+(write and read) mode. 
file = open("demofile.txt","w+")
file.write("this is w+ mode using python.") #here cursor is at last index but cursor read left to right so it nor able to read data. 
print("current file position: ",file.tell())
file.seek(0)                      #move cusor at starting.
print("current file position after seek(0): ",file.tell())
print("file data: ",file.read())
file.close()

#open file in r+(read and write) mode.use this mode only if file is already exist.
file = open("demofile.txt","r+")
print(file.read())
file.write("this is r+ mode using python.")
print("current file position: ",file.tell())
file.seek(0)                      #move cusor at starting position.
print("current file position after seek(0): ",file.tell())
print(file.read())
file.close()










