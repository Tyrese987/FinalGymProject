import tkinter as tk   
import pickle   
from tkinter import messagebox
import re

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
    entrypass = tk.Entry(root)
    entrypass.pack()

    labelpass2 = tk.Label(root, text = "repeat password")
    labelpass2.pack()
    entrypass2 = tk.Entry(root)
    entrypass2.pack()



    buttonok = tk.Button(root, text = "save", command = lambda: save(root, entryf, entrys, entryp, entrye, entrydob, entrypass, entrypass2 ))
    buttonok.pack()
    root.mainloop()

def save(root, entryf, entrys, entryp, entrye, entrydob, entrypass, entrypass2 ):
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
            messagebox.showerror("Invalid Input", "First name should contain only letters.")

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
                with open('Gym_Staff.pkl', 'rb') as file:
                    staff = pickle.load(file)
                staff.append(temp)
                with open('Gym_Staff.pkl', 'wb') as file:
                    pickle.dump(staff, file)
            except:
                staff = []
                staff.append(temp)
                with open('Gym_Staff.pkl', 'wb') as file:
                    pickle.dump(staff, file)
        for i in range(len(staff)):
            print(staff[i].username)

    else:
        return
    
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

    tkWindow = tk.Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('Login Form')

# If user names and passwords are correct, the user is logged in
def check_login(root, entryu, entryp):
    username = entryu.get()
    password = entryp.get()
    try:
        with open('Gym_Staff.pkl', 'rb') as file:
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
                root.destroy()
                return
            else:
                messagebox.showerror("Login error", "Incorrect password")
                return

    if not user_found:
        messagebox.showerror("Login error", "Incorrect username and password")
        def main_menu():
            root = tk.Tk()
            root.title("Gym System")

            label = tk.Label(root, text="Welcome to the Gym System")
            label.pack()

            button_create_staff = tk.Button(root, text="Create Staff", command=create_staff)
            button_create_staff.pack()

            button_login = tk.Button(root, text="Login", command=login)
            button_login.pack()

            root.mainloop()

        if __name__ == "__main__":
            main_menu()


login()
#create_staff()







