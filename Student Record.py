import mysql.connector
from tkinter import *
import tkinter as tk
import random
import time
import datetime
from mysql.connector import Error
from tkinter import messagebox
from tkinter import PhotoImage
import smtplib
import re
from datetime import date




connection = mysql.connector.connect(
            host="localhost",          # e.g., "localhost"
            user="root",      # e.g., "root"
            password="Sql@2025",  # your MySQL password
            database="StudentRecordBT"   # the database name where your table is stored
        )
Cursor = connection.cursor()
#Cursor.execute("CREATE TABLE Student_Record(Name VARCHAR(35),DOB INT,Gender VARCHAR(15),Age INT,Address VARCHAR(200),Contactnum VARCHAR(20),Mailid VARCHAR(10),CourseEnrolled VARCHAR(10),Experience VARCHAR(10),Fresher VARCHAR(10),DegreeName VARCHAR(300),Yearofpass VARCHAR(20),PreviousCompany VARCHAR(300),TotalWorkExperience INT,Message VARCHAR(100),DOJ INT,Total_fee INT)")
#insert_query = "INSERT INTO records (name, age, email) VALUES (%s, %s, %s)"
#Cursor.execute(insert_query, (query_Name, query_DOB, query_gender))
#messagebox.showinfo("Success", "Record added successfully!")
    

    #cursor.execute("CREATE DATABASE StudentRecordBT")

         # Optionally create the table if it does not exist
    #Cursor.execute("CREATE TABLE Student_Record(Name VARCHAR(35),DOB INT,Gender VARCHAR(15),Age INT,Address VARCHAR(200),Contactnum VARCHAR(20),Mailid VARCHAR(10),CourseEnrolled VARCHAR(10),Experience VARCHAR(10),Fresher VARCHAR(10),Degree_Name VARCHAR(100),Year_of_pass(20),Previous_company VARCHAR(300),Total_work_experience INT,Message VARCHAR(500),DOJ INT,Total_fee INT)")
        
        # Insert the record into the table using parameterized query
    #insert_query = "INSERT INTO records (name, age, email) VALUES (%s, %s, %s)"
    #Cursor.execute(insert_query, (query_Name, query_DOB, query_gender))
        #connection.commit()
#rename_query = "ALTER TABLE Student_Record CHANGE COLUMN `Comments` `Message` VARCHAR(255)"

#rename_query="ALTER TABLE Student_Record CHANGE COLUMN Comments Message VARCHAR(255)"
#Cursor.execute("ALTER TABLE Student_Record CHANGE COLUMN Comments Message VARCHAR(200)")
#try:
 #   Cursor.execute(rename_query)
 #   connection.commit()
  #  print("column changed successfully")
#except Exception as e:
 #   print("Error:",e)
#altering column datatype
alter_queries = [
    #"ALTER TABLE student_record MODIFY COLUMN Contactnum BIGINT;",  # Change contact to BIGINT
    "ALTER TABLE student_record CHANGE COLUMN DOB DOB DATE;",

    #"ALTER TABLE student_record MODIFY COLUMN DOB DATE;",  # Change year column type
    "ALTER TABLE student_record MODIFY COLUMN Yearofpass YEAR;",
    "ALTER TABLE student_record MODIFY COLUMN Mailid VARCHAR(255);",
    "ALTER TABLE student_record ADD UNIQUE (Mailid);",

    "ALTER TABLE student_record MODIFY COLUMN DOJ DATETIME;",   # Change date column type
    "ALTER TABLE student_record MODIFY COLUMN Total_fee BIGINT;",  # Example for large numbers
    "ALTER TABLE student_record MODIFY COLUMN CourseEnrolled VARCHAR(255);",

]
for query in alter_queries:
    Cursor.execute(query)
print("Column data types updated successfully!")

def add_record():
    # Retrieve values from entry widgets
    #should be column name which we created for sql
    Name = str(query_entry.get().strip())
    DOB=query_entryDOB.get().strip()
    Gender=query_entrygender.get().strip()
    Age=query_entryage.get().strip()
    Address=query_entryadd.get().strip()
    Contactnum =query_entryno.get().strip()
    MailID=query_entryid.get().strip()
    CourseEnrolled=query_entrycourse.get().strip()
    Experience=query_entryexp.get().strip()
    fresher=query_entryfre.get().strip()
    DegreeName=query_entryDN.get().strip()
    YearOfpass=query_entryYP.get().strip()
    PreviousCompany=query_entryPC.get().strip()
    TotalWorExperience=query_entryTW.get().strip()
    Message=query_entrymessage.get().strip()
    DOJ=query_entryDOJ.get().strip()
    Total_Fee=query_entryfee.get().strip()

    if not Name or not DOB or not Gender or not Age or not Address or not Contactnum or not MailID or not CourseEnrolled or not Experience or not fresher or not DegreeName or not YearOfpass or not PreviousCompany or not TotalWorExperience or not Message or not DOJ or not Total_Fee:
        messagebox.showerror("Input Error", "All fields are required")
        return

    try:
        global connection
        # Connect to the MySQL database (update with your own credentials)
        connection = mysql.connector.connect(
            host="localhost",          # e.g., "localhost"
            user="root",      # e.g., "root"
            password="Sql@2025",  # your MySQL password
            database="studentrecordbt"   # the database name where your table is stored
        )

        print(f"Name:{Name} (type:{type(Name)})")
        print(type(Name))
        cursor = connection.cursor()
        
        # Optionally create the table if it does not exist
        '''create_table_query = 
            CREATE TABLE IF NOT EXISTS records (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                email VARCHAR(255)
            )
        '''
        #cursor.execute(create_table_queryN
        #print(f"name:{Name}(Type:{type(Name)})")
        # Insert the record into the table using parameterized query
        #print(Name, DOB, Gender, Age, Address, CNUM, MailID, course, Experience, fresher, DegreeName, YOP, PreviousCompany, TotalWorExp, comments, DOJ, TotalFee)
        connection.autocommit = True
        cursor.execute("INSERT INTO student_record (Name,DOB,Gender,Age,Address,Contactnum,MailID,CourseEnrolled,Experience,fresher,DegreeName,Yearofpass,PreviousCompany,TotalWorkExperience,Message,DOJ,Total_Fee) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (Name,DOB,Gender,Age,Address,Contactnum,MailID,CourseEnrolled,Experience,fresher,DegreeName,YearOfpass,PreviousCompany,TotalWorExperience,Message,DOJ,Total_Fee))#,
        #cursor.execute(insert_query, (Name))#, age, email))
        #connection.commit()
        #connection.close()
        
        messagebox.showinfo("Success", "Record added successfully!")
        connection.commit()
        connection.close()
        print("Before Clearing:", query_entry.get(), query_entryDOB.get())
        query_entry.delete(0, tk.END)
        query_entryDOB.delete(0, tk.END)
        query_entrygender.delete(0,tk.END)
        query_entryage.delete(0,tk.END)
        query_entryadd.delete(0,tk.END)
        query_entryno.delete(0,tk.END)
        query_entryid.delete(0,tk.END)
        query_entrycourse.delete(0,tk.END)
        query_entryexp.delete(0,tk.END)
        query_entryfre.delete(0,tk.END)
        query_entryDN.delete(0,tk.END)
        query_entryYP.delete(0,tk.END)
        query_entryPC.delete(0,tk.END)
        query_entryexp.delete(0,tk.END)
        query_entryTW.delete(0,tk.END)
        query_entryDOJ.delete(0,tk.END)
        query_entryfee.delete(0,tk.END)
        query_entrymessage.delete(0,tk.END)
        print("After Clearing:", query_entry.get(), query_entryDOB.get())  # Should print empty
         #   entry_email.delete(0, tk.END)
        
    except Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Clear the entries after adding the record
            

def delete_record():
    # Retrieve values from entry widgets
    Name = str(query_entry.get().strip())
    DOB=query_entryDOB.get().strip()
    Gender=query_entrygender.get().strip()
    Age=query_entryage.get().strip()
    Address=query_entryadd.get().strip()
    Contactnum =query_entryno.get().strip()
    MailID=query_entryid.get().strip()
    CourseEnrolled=query_entrycourse.get().strip()
    Experience=query_entryexp.get().strip()
    fresher=query_entryfre.get().strip()
    DegreeName=query_entryDN.get().strip()
    YearOfpass=query_entryYP.get().strip()
    PreviousCompany=query_entryPC.get().strip()
    TotalWorExperience=query_entryTW.get().strip()
    Message=query_entrymessage.get().strip()
    DOJ=query_entryDOJ.get().strip()
    Total_Fee=query_entryfee.get().strip()
    

    if not Name:#or not DOB: #or not age or not email:
        messagebox.showerror("Input Error", "Please enter the name to delete")
        return

    try:
        # Connect to the MySQL database (update with your own credentials)
        connection = mysql.connector.connect(
            host="localhost",          # e.g., "localhost"
            user="root",      # e.g., "root"
            password="Sql@2025",  # your MySQL password
            database="studentrecordbt"   # the database name where your table is stored
        )

       # print(f"Name:{Name} (type:{type(Name)})")
        #print(type(Name))
        cursor = connection.cursor()
        
        # Optionally create the table if it does not exist
        '''create_table_query = 
            CREATE TABLE IF NOT EXISTS records (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                email VARCHAR(255)
            )
        '''
        #cursor.execute(create_table_queryN
        #print(f"name:{Name}(Type:{type(Name)})")
        # Insert the record into the table using parameterized query
        cursor.execute("DELETE FROM student_record WHERE Name=%s",(Name,)) 
        #cursor.execute(insert_query, (Name))#, age, email))
        connection.commit()
        
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", f"Record '{Name}' deleted successfully!")
              # Should print empty
         #   entry_email.delete(0, tk.END)
        else:
            messagebox.showwarning("Not Found", f"No record found for '{Name}'.")
        query_entry.delete(0, tk.END)
       
        
    except Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Clear the entries after adding the record
          
         #   entry_age.delete(0, tk.END)
         #   entry_email.delete(0, tk.END)
def view_record():
    Name = query_entry.get().strip() 
    DOB=query_entryDOB.get().strip()
    Gender=query_entrygender.get().strip()
    Age=query_entryage.get().strip()
    Address=query_entryadd.get().strip()
    Contactnum =query_entryno.get().strip()
    MailID=query_entryid.get().strip()
    CourseEnrolled=query_entrycourse.get().strip()
    Experience=query_entryexp.get().strip()
    fresher=query_entryfre.get().strip()
    DegreeName=query_entryDN.get().strip()
    YearOfpass=query_entryYP.get().strip()
    PreviousCompany=query_entryPC.get().strip()
    TotalWorExperience=query_entryTW.get().strip()
    Message=query_entrymessage.get().strip()
    DOJ=query_entryDOJ.get().strip()
    Total_Fee=query_entryfee.get().strip() # Get Name from entry field

    if not Name:
        messagebox.showerror("Input Error", "Please enter a Name to search.")
        return

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sql@2025",
            database="studentrecordbt"
        )
        cursor = connection.cursor()

        # Query to fetch student details
        cursor.execute("SELECT Name,DOB,Gender,Age,Address,Contactnum,MailID,CourseEnrolled,Experience,fresher,DegreeName,Yearofpass,PreviousCompany,TotalWorkExperience,Message,DOJ,Total_Fee from student_record WHERE Name = %s", (Name,))
        record = cursor.fetchone()  # Fetch one matching record

        # Clear the Text Box before inserting new data
        query_entry.delete(0, tk.END)

        if record:
            result_text.insert(tk.END, f"Name: {record[0]}\nDOB: {record[1]}\nGender: {record[2]}\nAge: {record[3]}\n "
                                           f"Address: {record[4]}\nContact: {record[5]}\nMail: {record[6]}\nCourse: {record[7]}\n "
                                           f"Experience: {record[8]}\nFresher: {record[9]}\nDegree: {record[10]}\n Year of Pass: {record[11]}\n "
                                           f"Previous Company: {record[12]}\nWork Experience: {record[13]}\nComments: {record[14]}\n "
                                           f"DOJ: {record[15]}\nTotal Fee: {record[16]}\n")
        else:
            result_text.insert(tk.END, "No record found.")

    except Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


'''# Update record in database
        cursor.execute("UPDATE student_record SET Name = %s, DOB = %s,Gender=%s,Age=%s,Address=%s,CNUM=%s,MailID=%s,course=%s,Experience=%s,fresher=%s,DegreeName=%s,YOP=%s,PreviousCompany=%s,TotalWorExp=%s,Message=%s,DOJ=%s,TotalFee=%s WHERE Name = %s", 
                       (query_entry,query_DOB,))
        connection.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Record updated successfully!")
        else:
            messagebox.showwarning("Not Found", "No record found for this Name.")

    except Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()'''
#def validate_email(email):
Cursor=connection.cursor()
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)
    #email = email_entry.get()
    #message = message_entry.get("1.0", tk.END)
def send_mail():    
    MailID=query_entryid.get().strip()
    Message = query_entrymessage.get().strip()  # ✅ No arguments needed

    
    if not validate_email(MailID):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    try:
        # SMTP Server Setup (Gmail Example)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        EMAIL = "jeevithacse14@gmail.com"  # Replace with your email
        PASSWORD = "wvid rrdc bmri pefr"  # Use an App Password instead of the real password
        server.login(EMAIL, PASSWORD)

        server.sendmail(EMAIL, MailID, Message)
        server.quit()
        
        messagebox.showinfo("Success", "Email Sent Successfully!")

        # Insert into Database (Make sure `Cursor` and `connection` are defined)
        Cursor.execute("INSERT INTO emails (email, message) VALUES (%s, %s)", (MailID, Message))
        connection.commit()
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

        '''server.login("jeevithacse14@gmail.com", "zeur gtcp pdqt doqr")
        server.sendmail("jeevithacse14@gmail.com", MailID, Message)
        server.quit()
        
        messagebox.showinfo("Success", "Email Sent Successfully!")
        
        # Insert into Database
        Cursor.execute("INSERT INTO emails (email, message) VALUES (%s, %s)", (MailID,Message))
        connection.commit()
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")
'''
#creates main window
root = tk.Tk()
root.title("STUDENT DATABASE")
#label frame (lable + frame)
from tkinter import *
root.geometry("1000x1000")
frame = tk.Frame(root, bg='#333333')
frame.pack(fill='both', expand=True)
#winco = tk.Label(frame, text="Welcome", bg='#333333', fg="white", font=("Arial", 16))
#winco.pack(pady=20)

#root.configure(bg='black')
labelf = LabelFrame(root, text="BESANT TECHNOLOGY STUDENT RECORD", 
                    labelanchor="n",  # Positions label at the top center
                    font=("Arial", 20, "bold"),  # Font family, size, and weight
                    fg="blue",bg='#333333')  # Font color
labelf.pack(fill=BOTH,expand=YES)
#label=Label(labelf,text='STUDENT RECORD')
#label.grid(row=0,column=0)
#labelf.pack(side=TOP, fill=X, padx=10, pady=10)
#label=Label(labelf,text='inside lable frame')
#label.pack()
#Creates widgets
query_Name = Label(labelf, text="Name",bg='#333333')
query_entry = Entry(labelf, width=50)
query_DOB = Label(labelf, text="DOB",bg='#333333').grid(row=1)
query_entryDOB = Entry(labelf, width=50)
query_gender = Label(labelf, text="Gender",bg='#333333').grid(row=2)
query_entrygender = Entry(labelf, width=50)
query_entryage = Label(labelf, text="Age",bg='#333333').grid(row=3)
query_entryage = Entry(labelf, width=50)
query_entryadd = Label(labelf, text="Address",bg='#333333').grid(row=4)
query_entryadd = Entry(labelf, width=50)
query_entryno = Label(labelf, text="Contact No:",bg='#333333').grid(row=5)
query_entryno = Entry(labelf, width=50)
query_entryDOJ = Label(labelf, text="DOJ",bg='#333333').grid(row=6)
query_entryDOJ = Entry(labelf, width=50)
query_entrycourse = Label(labelf, text="Course Enrolled",bg='#333333').grid(row=7)
query_entrycourse = Entry(labelf, width=50)
query_entryexp = Label(labelf, text="Experience",bg='#333333').grid(row=8)
query_entryexp = Entry(labelf, width=50)
query_entryfre = Label(labelf, text="Fresher",bg='#333333').grid(row=9)
query_entryfre = Entry(labelf, width=50)
query_entryDN = Label(labelf, text="Degree Name",bg='#333333').grid(row=10)
query_entryDN = Entry(labelf, width=50)
query_entryYP = Label(labelf, text="Year of Pass",bg='#333333').grid(row=11)
query_entryYP = Entry(labelf, width=50)
query_entryPC = Label(labelf, text="Previous Company",bg='#333333').grid(row=12)
query_entryPC = Entry(labelf, width=50)
query_entryTW = Label(labelf, text="Total Work Experience",bg='#333333').grid(row=13)
query_entryTW = Entry(labelf, width=50)
query_entryfee = Label(labelf, text="Total Fees",bg='#333333').grid(row=14)
query_entryfee = Entry(labelf, width=50)
query_entryid = Label(labelf, text="Mail id",bg='#333333').grid(row=15)
query_entryid = Entry(labelf, width=50)
query_entrymessage = Label(labelf, text="Message",bg='#333333').grid(row=16)
query_entrymessage = Entry(labelf, width=50)
result_getdetails = tk.Label(labelf, text="Student Details",bg='#333333')
result_text = tk.Text(labelf,  width=50)

# Arrange widgets using grid layout
result_getdetails.grid(row=17, column=0, padx=5, pady=5)
result_text.grid(row=17, column=1, columnspan=2, padx=15, pady=15)
query_Name.grid(row=0, column=0, padx=5, pady=5)
query_entry.grid(row=0, column=1, padx=5, pady=5)
query_entryDOB.grid(row=1, column=1, padx=5, pady=5)
query_entrygender.grid(row=2, column=1, padx=5, pady=5)
query_entryage.grid(row=3, column=1, padx=5, pady=5)
query_entryadd.grid(row=4, column=1, padx=5, pady=5)
query_entryno.grid(row=5, column=1, padx=5, pady=5)
query_entryDOJ.grid(row=6, column=1, padx=5, pady=5)
query_entrycourse.grid(row=7, column=1, padx=5, pady=5)
query_entryexp.grid(row=8, column=1, padx=5, pady=5)
query_entryfre.grid(row=9, column=1, padx=5, pady=5)
query_entryDN.grid(row=10, column=1, padx=5, pady=5)
query_entryYP.grid(row=11, column=1, padx=5, pady=5)
query_entryPC.grid(row=12, column=1, padx=5, pady=5)
query_entryTW.grid(row=13, column=1, padx=5, pady=5)
query_entryfee.grid(row=14, column=1, padx=5, pady=5)
query_entryid.grid(row=15, column=1, padx=5, pady=5)
query_entrymessage.grid(row=16, column=1, padx=5, pady=5)
#execute_button = tk.Button(root, text="Execute", command=execute_query)
#result_label = tk.Label(root, text="Result:")
#result_text = tk.Text(root, height=10, width=50)
#root.configure(background="black")

root.geometry("500x500")
def addrecord():
    messagebox.showinfo("ADD","Do you want to Add the Record?")
button=Button(root,text="ADD",width=5,height=2,bg="green",fg="black",font="bold",command=add_record)
button.place(x=500,y=50)
def deleterecord():
    messagebox.showinfo("DELETE","Do you want to Delete the Record?")
button=Button(root,text="DELETE",width=7,height=2,bg="green",fg="black",font="bold",command=delete_record)
button.place(x=500,y=250)
def viewrecord():
    messagebox.showinfo("VIEW","Do you want to View the Record?")
button=Button(root,text="VIEW",width=7,height=2,bg="green",fg="black",font="bold",command=view_record)
button.place(x=500,y=150)
def sendemail():
    messagebox.showinfo("Success","Email Sent Successfully!")
button=Button(root,text="SEND MAIL",width=10,height=3,bg="green",fg="black",font="bold",command=send_mail)
button.place(x=500,y=350)
#button.place(x=500,y=350)




'''image = PhotoImage(file="IT.png")  # Replace with your image file path
image_label = tk.Label(root, image=image)
image_label.grid(row=0, column=8, columnspan=3, pady=10)  # Position the image'''
from PIL import Image, ImageTk  # Import PIL for image handling


# 🖼️ **Load the Background Image**
bg_image = Image.open(r"D:\for python\ITT.png")  # Replace with your image path
from PIL import Image, ImageTk

bg_image = bg_image.resize((800, 700), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing

bg_photo = ImageTk.PhotoImage(bg_image)

# **Set the Image as Background**
bg_label = tk.Label(root, image=bg_photo)
#bg_label.place(relwidth=1, relheight=1)  # Cover entire window

bg_label.place(x=700,y=50)  # Fill entire window'''

#root = tk.Tk()
#root.title("SMTP Email Sender")
#root.geometry("400x300")
#query_Name = Label(labelf, text="Name",bg='#333333')


#email=Label(labelf, text="Email:")
#email.place(x=5,y=5)
#query_Name = Label(labelf, text="Name",bg='#333333')
#query_Name.grid(row=0, column=0, padx=5, pady=5)
'''email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Message:").pack()
message_entry = tk.Text(root, height=5, width=40)`
message_entry.pack()

def validate_email(email


):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def send_email():
    email = email_entry.get()
    message = message_entry.get("1.0", tk.END)
    
    if not validate_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    try:
        # SMTP Server Setup (Gmail Example)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("jeevithacse14@gmail.com", "zeur gtcp pdqt doqr")
        server.sendmail("jeevithacse14@gmail.com", email, message)
        server.quit()
        
        messagebox.showinfo("Success", "Email Sent Successfully!")
        
        # Insert into Database
        #cursor.execute("INSERT INTO emails (email, message) VALUES (%s, %s)", (email, message))
        #connection.commit()
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

tk.Button(root, text="Send Email", command=send_email).pack()
'''

def send_email():
    MailID=query_entryid.get().strip()
    Message=query_entrymessage.get().strip()
    
''' if not MailID or not Message:
        messagebox.showerror("Input Error", "Please enter a Name to search.")
        return

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sql@2025",
            database="studentrecordbt"
        )
        cursor = connection.cursor()'''

        

connection.close()


root.mainloop()