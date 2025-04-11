
import tkinter as tk
import pickle
import random
import string
import os
from tkinter import messagebox

Class Customer:
    def __init__(self, userid, fname, sname, phone, email, dob, health_issues):
        self.userid = userid
        self.fname = fname
        self.sname = sname
        self.phone = phone
        phone = "12345678911"
        self.email = email
        self.dob = dob
        self.health_issues = health_issues

Class Staff:
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
        #validation need to validate phone numbers etc 
        if len(fname) == 0:
            validate = False

        if len(sname) ==0:
            validate = False

        if len(phone) == 0:
            validate = False

        if len(email) ==0:
            validate = False

        if len(dob) ==0:
            validate = False

        

        if validate == True:
            username = fname[0]+sname+phone[:2]
            id = username
            temp= Staff(id, username, pass1, fname, sname, phone, email, dob)
            try:
                with open('my_staff.pkl', 'rb') as file:
                    staff = pickle.load(file)
                staff.append(temp)
                with open('my_staff.pkl', 'wb') as file:
                    pickle.dump(staff, file)
            except:
                staff = []
                staff.append(temp)
                with open('my_staff.pkl', 'wb') as file:
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

    buttonok = tk.Button(root, text = "ok", command = lambda: check(root,entryu, entryp ))
    buttonok.pack()
    root.mainloop()
def check(root,entryu, entryp):
    username = entryu.get()
    password = entryp.get()
    with open('my_staff.pkl', 'rb') as file:
        staff = pickle.load(file)
    logged_in = False
    for i in range(len(staff)):
        if staff[i].username == username and staff[i].password == password:
            logged_in = True

    if logged_in == True:
        print("you are logged in")
    else:
        print("username or password not recognised")


def save_user(root, entryf, entrys, entryp, entrye, entrydob, entryHI):
    
    validate = True
    fname = entryf.get()
    sname = entrys.get()
    phone = entryp.get()
    email = entrye.get()
    dob = entrydob.get()
    health_issues = entryHI.get()

    if len(fname) == 0 or len(sname) == 0 or len(phone) == 0 or len(email) == 0 or len(dob) == 0:
        validate = False
        print("Validation failed: One or more fields are empty.")
    
    if validate:
        userid = fname[0] + sname + phone[:2]
        customer = Customer(userid, fname, sname, phone, email, dob, health_issues)

        try:
            with open('my_customers.pkl', 'rb') as file:
                customers = pickle.load(file)
            customers.append(customer)
        except FileNotFoundError:
            customers = [customer]

        with open('my_customers.pkl', 'wb') as file:
            pickle.dump(customers, file)

        print(f"Customer {fname} {sname} saved successfully!")
        root.destroy() 
    else:
        print("Error: Unable to save the customer.")

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

def load_customers():
    try:
        with open("my_customers.pkl", "rb") as file:
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

   
    def load_user_info(event):
        selected_index = user_listbox.curselection()
        if selected_index:
            selected_customer = customers[selected_index[0]]
            entryf.delete(0, tk.END)
            entryf.insert(0, selected_customer.fname)
            entrys.delete(0, tk.END)
            entrys.insert(0, selected_customer.sname)
            entryp.delete(0, tk.END)
            entryp.insert(0, selected_customer.phone)
            entrye.delete(0, tk.END)
            entrye.insert(0, selected_customer.email)
            entrydob.delete(0, tk.END)
            entrydob.insert(0, selected_customer.dob)
            entryHI.delete(0, tk.END)
            entryHI.insert(0, selected_customer.health_issues)

    
    def save_changes():
        selected_index = user_listbox.curselection()
        if selected_index:
            selected_customer = customers[selected_index[0]]
            selected_customer.fname = entryf.get().strip()
            selected_customer.sname = entrys.get().strip()
            selected_customer.phone = entryp.get().strip()
            selected_customer.email = entrye.get().strip()
            selected_customer.dob = entrydob.get().strip()
            selected_customer.health_issues = entryHI.get().strip()
            save_customers(customers)
            messagebox.showinfo("Success", "User information updated successfully.")
            root.destroy()

    
    user_listbox = tk.Listbox(root)
    for customer in customers:
        user_listbox.insert(tk.END, f"{customer.userid}: {customer.fname} {customer.sname}")
    user_listbox.pack()
    user_listbox.bind("<<ListboxSelect>>", load_user_info)

 
    tk.Label(root, text="First Name").pack()
    entryf = tk.Entry(root)
    entryf.pack()

    tk.Label(root, text="Second Name").pack()
    entrys = tk.Entry(root)
    entrys.pack()

    tk.Label(root, text="Phone").pack()
    entryp = tk.Entry(root)
    entryp.pack()

    tk.Label(root, text="Email").pack()
    entrye = tk.Entry(root)
    entrye.pack()

    tk.Label(root, text="Date of Birth").pack()
    entrydob = tk.Entry(root)
    entrydob.pack()

    tk.Label(root, text="Health Issues").pack()
    entryHI = tk.Entry(root)
    entryHI.pack()

    # Button to save changes
    tk.Button(root, text="Save Changes", command=save_changes).pack()

    root.mainloop()

def delete_user():
    # Load customers from the pickle file
    try:
        with open("my_customers.pkl", "rb") as f:
            customers = pickle.load(f)
    except FileNotFoundError:
        print("No customer file found.")
        return
    except EOFError:
        print("Customer file is empty.")
        return

    user_id_to_delete = input("Enter the User ID to delete: ")

    # Filter the list to remove the customer with the specified ID
    updated_customers = [customer for customer in customers if customer.userid != user_id_to_delete]

    if len(updated_customers) < len(customers):  # If any record was removed
        # Save the updated list back to the pickle file
        with open("my_customers.pkl", "wb") as f:
            pickle.dump(updated_customers, f)
        print(f"User with ID {user_id_to_delete} deleted successfully.")
    else:
        print(f"No user found with ID {user_id_to_delete}.")

def read_customers():
    try:
        with open("my_customers.pkl", "rb") as f:
            customers = pickle.load(f)
        for customer in customers:
            print(
                f"User ID: {customer.userid}, Name: {customer.fname} {customer.sname}, "
                f"Phone: {customer.phone}, Email: {customer.email}, DOB: {customer.dob}, "
                f"Health Issues: {customer.health_issues}"
            )
    except FileNotFoundError:
        print("No customer file found.")
    except EOFError:
        print("Customer file is empty.")

# Example usage:
print("Deleting a user...")


print("Reading the updated customer list...")



#create_staff()
#login()
#edit_user()
#create_user()
#delete_user()
#read_customers()
