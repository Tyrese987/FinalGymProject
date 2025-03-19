import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Customer:
    def __init__(self, userid, fname, sname, phone, email, dob, health_issues):
        self.userid = userid
        self.fname = fname
        self.sname = sname
        self.phone = phone
        self.email = email
        self.dob = dob
        self.health_issues = health_issues

class Staff:
    def __init__(self, userid, username, password, fname, sname, phone, email, dob):
        self.userid = userid
        self.username = username
        self.password = password
        self.fname = fname
        self.sname = sname
        self.phone = phone
        self.email = email
        self.dob = dob
#Validation for my Staff Login page 
def validate_login():
    userid = username_entry.get()
    password = password.entry.get()

    if userid =="Staff" and password == "Staff":
        messagebox.showinfo("Login Successful", "welcome"+ sname + "!")
    else:
        messagebox.showerror("Login Error", "Incorrect Username or Password")

#Main window
root = tk.Tk()
root.title("Gym System Login")

username_label = tk.Label(root, text="Username")
username_label.pack()

username_entry =tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack()

root.mainloop()