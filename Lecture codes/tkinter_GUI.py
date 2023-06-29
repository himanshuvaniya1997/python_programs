from tkinter import *    #here * means import all file of tkinter.
import mysql.connector
import tkinter.messagebox as msg

root = Tk()     #Tk() is a class of tkinter.

root.title("Himanshu's First GUI Application")
root.geometry("400x400")
root.resizable(width =False,height =False)    #for constant size of GUI.

def create_conn():
    return mysql.connector.connect(     #connect fun return connection object.
        host = "localhost",             #if databse on other pc then host = IP address of that pc.
        database = "python_2023",
        user = "root",
        password = ""
    )
print(create_conn())  #return hexadecimal address of connection object.

def insert_data():
    print("Insert Button clicked")
    if  e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mnum.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn = create_conn() 
        cursor = conn.cursor()
        query = "insert into student(fname,lname,email,mnum) values(%s,%s,%s,%s)"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mnum.get()) 
        cursor.execute(query,args) 
        conn.commit()
        conn.close() 
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mnum.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully") 
          
def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mnum.delete(0,'end')
    print("Search Button clicked") 
    if e_id.get()=="":
        msg.showinfo("Search Status","ID Is mandatory")
    else:
        conn = create_conn() 
        cursor = conn.cursor()
        query = "select * from student where id=%s"
        args = (e_id.get(),)     #comma is compulsory for args tuple. 
        cursor.execute(query,args)
        result = cursor.fetchall()
        print(result)
        if result:
            for item in result:
                e_fname.insert(0, item[1])
                e_lname.insert(0, item[2])
                e_email.insert(0, item[3])
                e_mnum.insert(0, item[4])
        else:
            msg.showinfo("Search Status","Id Not Found")        
        conn.close()    
       
def update_data():
    print("Update Button clicked")
    if  e_id.get()=="" or e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mnum.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn = create_conn() 
        cursor = conn.cursor()
        query = "update student set fname=%s,lname=%s,email=%s,mnum=%s where id=%s"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mnum.get(),e_id.get()) 
        cursor.execute(query,args) 
        conn.commit()
        conn.close() 
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mnum.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully") 
        
def delete_data():
    print("Delete Button clicked")  
    if  e_id.get()=="":
        msg.showinfo("Delete Status","ID Is Mandatory")
    else:
        conn = create_conn() 
        cursor = conn.cursor()
        query = "delete from student where id=%s"
        args = (e_id.get(),) 
        cursor.execute(query,args) 
        conn.commit()
        conn.close() 
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mnum.delete(0,'end')
        msg.showinfo("Delete Status","data Deleted Successfully") 
      
    
l_head = Label(root,text="PERSONAL DETAIL",font=("calibri",15,"bold"))
l_head.place(x=120,y=10)    #here x=row and y=column.

l_id = Label(root,text="ID",font=("Arial",15))
l_id.place(x=30,y=70)    #here x=row and y=column.

l_fname = Label(root,text="FIRST NAME",font=("Arial",15))
l_fname.place(x=30,y=120)    #here x=row and y=column.

l_lname = Label(root,text="LAST NAME",font=("Arial",15))
l_lname.place(x=30,y=170)    #here x=row and y=column.

l_email = Label(root,text="EMAIL",font=("Arial",15))
l_email.place(x=30,y=220)    #here x=row and y=column.

l_mnum = Label(root,text="MOBILE NO",font=("Arial",15))
l_mnum.place(x=30,y=270)    #here x=row and y=column.

e_id = Entry(root)
e_id.place(x=230,y=70)

e_fname = Entry(root)
e_fname.place(x=230,y=120)

e_lname = Entry(root)
e_lname.place(x=230,y=170)

e_email = Entry(root)
e_email.place(x=230,y=220)

e_mnum = Entry(root)
e_mnum.place(x=230,y=270)

insert = Button(root,text ="INSERT",font =("Arial",15),fg ="white",bg ="black",command =insert_data)
insert.place(x=10,y=320)

search = Button(root,text ="SEARCH",font =("Arial",15),fg ="white",bg ="black",command =search_data)
search.place(x=100,y=320)

update = Button(root,text ="UPDATE",font =("Arial",15),fg ="white",bg ="black",command =update_data)
update.place(x=198,y=320)

delete = Button(root,text ="DELETE",font =("Arial",15),fg ="white",bg ="black",command =delete_data)
delete.place(x=295,y=320)

root.mainloop()   #for continue run application.






