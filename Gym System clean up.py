import tkinter as tk
from tkinter import messagebox
import pickle
import re


#Classes will be defined here for the system Currently Staff and Customer 01/02/2025
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

#Defining the main menu functions for the main system

def main_menu():
    root = tk.Tk()
    root.title("Gym System")

    label = tk.Label(root, text="Welcome to the Gym System")
    label.pack()

    button_create_staff = tk.Button(root, text="Create Staff", command=create_staff)
    button_create_staff.pack()

    button_create_user = tk.Button(root, text="Create User", command=create_user)
    button_create_user.pack()

    button_create_staff = tk.Button(root, text="Search User", command=search_user)
    button_create_staff.pack()
    
    
    # button_create_edit_user = tk.Button(root, text="Edit User", command=create_edit_user)
    

    #button view user


    #delete user


def create_staff(): 
    root = tk.Tk()
    labelf = tk.Label(root, text = "first name")
    labelf.pack()
    entryf = tk.Entry(root)
    entryf.pack()

    labels = tk.Label(root, text = "second name")
    labels.pack()
    entrys = tk.Entry(root)
    entrys.pack()

    labelp = tk.Label(root, text = "phone")
    labelp.pack()
    entryp = tk.Entry(root)
    entryp.pack()

    labele = tk.Label(root, text = "email")
    labele.pack()
    entrye = tk.Entry(root)
    entrye.pack()

    labeldob = tk.Label(root, text = "dob")
    labeldob.pack()
    entrydob = tk.Entry(root)
    entrydob.pack()

    labelpass = tk.Label(root, text = "password")
    labelpass.pack()
    entrypass = tk.Entry(root, show="*")
    entrypass.pack()

    labelpass2 = tk.Label(root, text = "repeat password")
    labelpass2.pack()
    entrypass2 = tk.Entry(root, show="*")
    entrypass2.pack()

    buttonok = tk.Button(root, text = "save", command = lambda: save_staff(root, entryf, entrys, entryp, entrye, entrydob, entrypass, entrypass2 ))
    buttonok.pack()
    root.mainloop()

def create_user():
    root = tk.Tk()
    labelf = tk.Label(root, text="First Name")
    labelf.pack()
    entryf = tk.Entry(root)
    entryf.pack()

    labels = tk.Label(root, text="Second Name")
    labels.pack()
    entrys = tk.Entry(root)
    entrys.pack()

    labelp = tk.Label(root, text="Phone")
    labelp.pack()
    entryp = tk.Entry(root)
    entryp.pack()

    labele = tk.Label(root, text="Email")
    labele.pack()
    entrye = tk.Entry(root)
    entrye.pack()

    labeldob = tk.Label(root, text="Date of Birth")
    labeldob.pack()
    entrydob = tk.Entry(root)
    entrydob.pack()

    labelHI = tk.Label(root, text="Health Issues")
    labelHI.pack()
    entryHI = tk.Entry(root)
    entryHI.pack()

    buttonok = tk.Button(
        root,
        text="Save",
        command=lambda: save_user(root, entryf, entrys, entryp, entrye, entrydob, entryHI)
    )
    buttonok.pack()
    root.mainloop()

#Validation for the user and staff creation
def save_staff(root, entryf, entrys, entryp, entrye, entrydob, entrypass, entrypass2 ):
    pass1 = entrypass.get()
    pass2 = entrypass2.get()
    if pass1 == pass2:
        validate = True
        fname = entryf.get()
        sname = entrys.get()
        phone = entryp.get()
        email = entrye.get()
        dob = entrydob.get()

        # Validate first name
        if not fname.isalpha():
            validate = False
            messagebox.showerror("Invalid Input", "First name should contain only letters.") #Making sure that the first name is only letters if not then it will show an error message

        # Validate second name
        if not sname.isalpha():
            validate = False
            messagebox.showerror("Invalid Input", "Second name should contain only letters.") #Making sure that the second name is only letters if not then it will show an error message

        # Validate phone number to be 11 digits
        if not re.match(r'^\d{11}$', phone):
            validate = False
            messagebox.showerror("Invalid Input", "Phone number should be 11 digits.") #Making sure that the phone number is 11 digits if not then it will show an error message

        # Validate email insuring that it has a @ and a dot
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            validate = False
            messagebox.showerror("Invalid Input", "Invalid email format.") #Making sure that the email is in the correct format if not then it will show an error message

        # Validate date of birth to be int the format DD/MM/YYYY
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', dob):
            validate = False
            messagebox.showerror("Invalid Input", "Date of birth should be in DD/MM/YYYY format.") #Making sure that the date of birth is in the correct format if not then it will show an error message


        if validate == True:
            username = fname[0]+sname+phone[:2]
            id = username
            temp= Staff(id, username, pass1, fname, sname, phone, email, dob) #Creating a new staff member
            try:
                with open('Gym_Staff1.pkl', 'rb') as file: 
                    staff = pickle.load(file)
                staff.append(temp)
                with open('Gym_Staff1.pkl', 'wb') as file: 
                    pickle.dump(staff, file)
            except:
                staff = []
                staff.append(temp)
                with open('Gym_Staff1.pkl', 'wb') as file: 
                    pickle.dump(staff, file)
        for i in range(len(staff)):
            print(staff[i].username)
        messagebox.showinfo("Success", "Staff has been created successfully") #Showing a message box to show that the staff has been created successfully
    else:
        return

def save_user(root, entryf, entrys, entryp, entrye, entrydob, entrypass, entrypass2 ): #Creating a new user
    pass1 = entrypass.get()
    pass2 = entrypass2.get()
    if pass1 == pass2:
        validate = True
        fname = entryf.get()
        sname = entrys.get()
        phone = entryp.get()
        email = entrye.get()
        dob = entrydob.get()

        # Validate first name
        if not fname.isalpha():
            validate = False
            messagebox.showerror("Invalid Input", "First name should contain only letters.") #Same logic as the staff creation

        # Validate second name
        if not sname.isalpha():
            validate = False
            messagebox.showerror("Invalid Input", "Second name should contain only letters.") 

        # Validate phone number to be 11 digits
        if not re.match(r'^\d{11}$', phone):
            validate = False
            messagebox.showerror("Invalid Input", "Phone number should be 11 digits.") 

        # Validate email insuring that it has a @ and a dot
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            validate = False
            messagebox.showerror("Invalid Input", "Invalid email format.")

        # Validate date of birth to be int the format DD/MM/YYYY
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', dob):
            validate = False
            messagebox.showerror("Invalid Input", "Date of birth should be in DD/MM/YYYY format.")


        if validate == True:
            username = fname[0]+sname+phone[:2]
            id = username
            temp= Staff(id, username, pass1, fname, sname, phone, email, dob)
            try:
                with open('User_Gym.pkl', 'rb') as file:
                    staff = pickle.load(file)
                staff.append(temp)
                with open('User_Gym.pkl', 'wb') as file:
                    pickle.dump(staff, file)
            except:
                staff = []
                staff.append(temp)
                with open('User_Gym.pkl', 'wb') as file:
                    pickle.dump(staff, file)
        for i in range(len(staff)):
            print(staff[i].username)
        messagebox.showinfo("Success", "Staff has been created successfully")
    else:
        return
    
def search_user():
    def perform_search():
        username = entryu.get()
        customers = load_customers()
        for customer in customers:
            if customer.username == username:
                messagebox.showinfo("Success", f"User {username} found.")
                return
        messagebox.showerror("Error", "User not found.")

    root = tk.Tk()
    root.title("Search User")

    labelu = tk.Label(root, text="Username")
    labelu.pack()

    entryu = tk.Entry(root)
    entryu.pack()

    buttonok = tk.Button(root, text="Search", command=perform_search)
    buttonok.pack()

    root.mainloop()

def load_customers():
    try:
        with open("User_Gym.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def edit_user():
    customers = load_customers()
    if not customers:
        messagebox.showinfo("Info", "No users available to edit.")
        return
    
    root = tk.Tk()
    root.title("Edit User")
    
    label = tk.Label(root, text="Select a user to edit:")
    label.pack()

    user_list = tk.Listbox(root)
    user_list.pack()

    for customer in customers:
        user_list.insert(tk.END, customer.username)

    def edit():
        selected = user_list.curselection()
        if not selected:
            messagebox.showerror("Error", "No user selected.")
            return

        selected = selected[0]
        user = customers[selected]
        root.destroy()
        edit_user_form(user)

    button = tk.Button(root, text="Edit", command=edit)
    button.pack()

    root.mainloop()

    











#Login function for the system   
def login():
    
    root = tk.Tk()
    labelu = tk.Label(root, text = "username")
    labelu.pack()
    entryu = tk.Entry(root)
    entryu.pack()

    labelp = tk.Label(root, text = "password")
    labelp.pack()
    entryp = tk.Entry(root)
    entryp.pack()

    buttonok = tk.Button(root, text = "login", command = lambda: check_login(root, entryu, entryp))
    buttonok.pack()
    root.mainloop()

# If user names and passwords are correct, the user is logged in
def check_login(root, entryu, entryp):
    username = entryu.get()
    password = entryp.get()
    try:
        with open('Gym_Staff1.pkl', 'rb') as file:
            staff = pickle.load(file)
    except FileNotFoundError:
        staff = []

    user_found = False
    for member in staff:
        if member.username == username:
            user_found = True
            if member.password == password:
                messagebox.showinfo("Login", "Login Successful")
                message = "Welcome " + username
                messagebox.showinfo("Welcome", message)
                root.destroy()  # Close the login window
                main_menu()  # Open the main menu
                return
            else:
                messagebox.showerror("Login error", "Incorrect password")
                return
    
    if not user_found:
        messagebox.showerror("Login error", "Incorrect username and password")
        return
#login()
create_staff()
