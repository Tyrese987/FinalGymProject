import tkinter as tk
from tkinter import messagebox
import pickle
import re
import random
import os
import datetime
from datetime

class Customer:
    def __init__(self, userid, fname, sname, phone, email, dob, health_issues):
        self.userid = userid
        self.fname = fname
        self.sname = sname
        self.phone = phone
        self.email = email
        self.dob = dob
        self.health_issues = health_issues

    def get_age_group(self):
        # Parse the DOB string into a datetime object
        dob_date = datetime.strptime(self.dob, "%d/%m/%Y")
        today = datetime.today()
        
        # Calculate the age
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        
        # Determine the age group
        if 14 <= age <= 16:
            return "Junior"
        elif 17 <= age <= 50:
            return "Normal"
        elif 51 <= age <= 90:
            return "Unc"
        else:
            return "Unknown"

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

class Booking:
      def __init__(self, row, column, customer_id):
            self.row = row
            self.column = column
            self.customer_id = customer_id        
#------
# Defining the main menu functions for the main system
def main_menu():
    root = tk.Tk()
    root.title("Gym System")

    label = tk.Label(root, text="Welcome to the Gym System")
    label.pack()

    button_create_staff = tk.Button(root, text="Create Staff", command=create_staff)
    button_create_staff.pack()

    button_create_booking = tk.Button(root, text="Create Booking", command=booking_function)
    button_create_booking.pack()

    button_create_user = tk.Button(root, text="Create User", command=create_user)
    button_create_user.pack()

    button_search_user = tk.Button(root, text="Search User", command=search_user)
    button_search_user.pack()

    button_edit_user = tk.Button(root, text="Edit User", command=edit_user)
    button_edit_user.pack() 

    button_quick_create_user = tk.Button(root, text="Create Booking", command= create_booking)
    button_quick_create_user.pack()

    button_delete_user = tk.Button(root, text="Delete User", command=delete_user)
    button_delete_user.pack()



    root.mainloop()

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

def create_user(): # creates user function for the system taking the inputs same thing with staff creation however doesn't need a password for the user 
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
def save_staff(root, entryf, entrys, entryp, entrye, entrydob, entrypass, entrypass2):
    pass1 = entrypass.get()
    pass2 = entrypass2.get()
    validate = True

    if pass1 != pass2:
        validate = False
        messagebox.showerror("Invalid Input", "Passwords don't match")

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

    # Validate email format
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        validate = False
        messagebox.showerror("Invalid Input", "Invalid email format.")

    # Validate date of birth (DD/MM/YYYY format)
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', dob):
        validate = False
        messagebox.showerror("Invalid Input", "Date of birth should be in DD/MM/YYYY format.")

    if validate:
        username = fname[0] + sname + phone[:2]  # Generate a username
        staff_id = username

        # Create the Staff object
        temp = Staff(staff_id, username, pass1, fname, sname, phone, email, dob)

        # Try to load existing staff data and append the new staff member
        try:
            with open('Gym_Staff1.pkl', 'rb') as file:
                staff = pickle.load(file)
        except FileNotFoundError:
            staff = []

        staff.append(temp)

        # Save the updated staff list back to the file
        with open('Gym_Staff1.pkl', 'wb') as file:
            pickle.dump(staff, file)

        # Show success message
        messagebox.showinfo("Success", "Staff has been created successfully")

        messagebox.showinfo("welcome",username)

    else:
        return  # Exit the function if validation fails


def save_user(root, entryf, entrys, entryp, entrye, entrydob, entryHI):
    fname = entryf.get()
    sname = entrys.get()
    phone = entryp.get()
    email = entrye.get()
    dob = entrydob.get()
    HI = entryHI.get()
    root.destroy()

    validate = True

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

    # Validate email format
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        validate = False
        messagebox.showerror("Invalid Input", "Invalid email format.")

    # Validate date of birth (DD/MM/YYYY format)
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', dob):
        validate = False
        messagebox.showerror("Invalid Input", "Date of birth should be in DD/MM/YYYY format.")

    if validate:
        username = fname[0] + sname + phone[:2]
        id = username
        temp = Customer(id, fname, sname, phone, email, dob, HI)
        
        # Get the age group
        age_group = temp.get_age_group()
        
        try:
            with open('User_Gym.pkl', 'rb') as file:
                customers = pickle.load(file)
            customers.append(temp)
            with open('User_Gym.pkl', 'wb') as file:
                pickle.dump(customers, file)
        except FileNotFoundError:
            customers = []
            customers.append(temp)
            with open('User_Gym.pkl', 'wb') as file:
                pickle.dump(customers, file)
        
        messagebox.showinfo("Success", f"User has been created successfully. Age Group: {age_group}")
        messagebox.showinfo("welcome", username)
    else:
        return

def load_customers(): #function to load the customer from the files 
    try:
        with open('User_Gym.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []



def search_user():
    def perform_search():
        userid = entryu.get()  
        customers = load_customers()
        for customer in customers:
            if customer.userid == userid:
                # Display customer data
                age_group = customer.get_age_group()
                messagebox.showinfo("Success", 
                    f"User Found:\n"
                    f"Name: {customer.fname} {customer.sname}\n"
                    f"Phone: {customer.phone}\n"
                    f"Email: {customer.email}\n"
                    f"DOB @ {customer.dob}\n"
                    f"Health Issues:{customer.health_issues}\n"
                    f"Age Group: {age_group}"
                )
                return
        messagebox.showerror("Error", "User not found.")

    root = tk.Tk()
    root.title("Search User")

    # Only search by userid
    tk.Label(root, text="User ID").pack()
    entryu = tk.Entry(root)
    entryu.pack()

    tk.Button(root, text="Search", command=perform_search).pack()
    root.mainloop()

def edit_user():
    customers = load_customers()
    if not customers:
        messagebox.showinfo("Info", "No users available to edit.")
        return

    root = tk.Tk()
    root.title("Edit User")

    # Create the listbox for customers
    user_listbox = tk.Listbox(root)
    for customer in customers:
        user_listbox.insert(tk.END, f"{customer.userid}: {customer.fname} {customer.sname}")
    user_listbox.pack()

    # Create entry widgets for editing the user information
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




    # Define the callback to load customer info when an item is selected
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

    user_listbox.bind("<<ListboxSelect>>", load_user_info)

    def validate_input(fname, sname, phone, email, dob): #double validation incase of poteinal errors being created
        if not fname.isalpha():
            messagebox.showerror("Invalid Input", "First name should contain only letters.")
            return False
        if not sname.isalpha():
            messagebox.showerror("Invalid Input", "Second name should contain only letters.")
            return False
        if not re.match(r'^\d{11}$', phone):
            messagebox.showerror("Invalid Input", "Phone number should be 11 digits.")
            return False
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messagebox.showerror("Invalid Input", "Invalid email format.")
            return False
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', dob):
            messagebox.showerror("Invalid Input", "Date of birth should be in DD/MM/YYYY format.")
            return False
        return True

    def save_changes():
        selected_index = user_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            selected_customer = customers[idx]
            fname = entryf.get().strip()
            sname = entrys.get().strip()
            phone = entryp.get().strip()
            email = entrye.get().strip()
            dob = entrydob.get().strip()
            health_issues = entryHI.get().strip()

            if validate_input(fname, sname, phone, email, dob):
                # Update the customer's information
                selected_customer.fname = fname
                selected_customer.sname = sname
                selected_customer.phone = phone
                selected_customer.email = email
                selected_customer.dob = dob
                selected_customer.health_issues = health_issues
                save_customers(customers)

                # Update the listbox display for the modified customer
                user_listbox.delete(idx)
                user_listbox.insert(idx, f"{selected_customer.userid}: {fname} {sname}")
                messagebox.showinfo("Success", "User information updated successfully.")

    def save_customers(customers):
        with open('User_Gym.pkl', 'wb') as file:
            pickle.dump(customers, file)

    tk.Button(root, text="Save Changes", command=save_changes).pack()
    root.mainloop()

#-----------

def delete_user():
    customers = load_customers()
    if not customers:
        messagebox.showinfo("Info", "No users available to delete.")
        return

    root = tk.Tk()
    root.title("Delete User")

    # Listbox to show users
    user_listbox = tk.Listbox(root)
    for customer in customers:
        user_listbox.insert(tk.END, f"{customer.userid}: {customer.fname} {customer.sname}")
    user_listbox.pack()

    def confirm_delete():
        selected_index = user_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            selected_customer = customers[idx]

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete {selected_customer.fname} {selected_customer.sname}?"
            )

            if confirm:
                del customers[idx]
                save_customers(customers)
                user_listbox.delete(idx)
                messagebox.showinfo("Success", "User deleted successfully.")

    def save_customers(customers):
        with open('User_Gym.pkl', 'wb') as file:
            pickle.dump(customers, file)

    tk.Button(root, text="Delete Selected User", command=confirm_delete).pack()

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
                messagebox.showerror("Login error", "Incorrect password") #shows an error message if the password is incorrect
                return

    if not user_found:
        messagebox.showerror("Login error", "Incorrect username and password")
        return

def booking_function():
    # Create another week for booking
    def create_grid():
        # Create a new window for entering the filename
        grid_window = tk.Toplevel(root)
        grid_window.title("Create New Booking Grid")

        tk.Label(grid_window, text="Enter the name of the new file:").pack(pady=5)
        filename_entry = tk.Entry(grid_window, width=30)
        filename_entry.pack(pady=5)

        def save_grid():
            filename = filename_entry.get().strip()
            if not filename:
                messagebox.showerror("Error", "Filename cannot be empty.")
                return

            day_name, time_slot = 8, 6
            matrix = [[0 for _ in range(time_slot)] for _ in range(day_name)]
            for row in range(day_name):
                for column in range(time_slot):
                    matrix[row][column] = Booking(row, column, "None")

            try:
                with open(filename, "wb") as f:
                    pickle.dump(matrix, f)
                messagebox.showinfo("Success", f"New booking grid saved to {filename}")
                grid_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save booking grid: {e}")

        tk.Button(grid_window, text="Save", command=save_grid).pack(pady=10)
        tk.Button(grid_window, text="Cancel", command=grid_window.destroy).pack(pady=5)

    # Create the main booking function window
    root = tk.Tk()
    root.title("Booking Function")

    tk.Label(root, text="Booking Function").pack(pady=10)

    tk.Button(root, text="Create New Booking Grid", command=create_grid).pack(pady=10)

    tk.Button(root, text="Close", command=root.destroy).pack(pady=10)

    root.mainloop()

def create_booking():

    filename = input("enter name of the file to open")
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            booking = pickle.load(f)
    else:
            return
    days = ["null","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    times = ["null","12am", "2pm", "4pm", "6pm", "8pm"]
    win = tk.Tk()
    tk.Label(win, text=filename, borderwidth=2, relief="ridge", width=12).grid(row=0, column=0)
    for col in range(len(times)):
            tk.Label(win, text=times[col], borderwidth=2, relief="ridge", width=12).grid(row=0, column=col)
        
    for row in range(1, len(days)):
            tk.Label(win, text=days[row], borderwidth=2, relief="ridge", width=12).grid(row=row, column=0)
            for col in range(1, len(times)):
                # Each cell is a button that calls book_slot when clicked.
                btn = tk.Button(win, text=booking[row][col].customer_id, bg="lightblue", width=12,
                                command=lambda d=row, t=col: book_slot(win, d, t, filename))
                btn.grid(row=row, column=col, padx=1, pady=1)
    win.mainloop()

def book_slot(win, d, t, filename):
    # Load customers from file
    try:
        with open('User_Gym.pkl', 'rb') as file:
            customers = pickle.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No customers found.")
        return

    # Create a new window for selecting a customer
    slot_window = tk.Toplevel(win)
    slot_window.title("Select Customer")

    tk.Label(slot_window, text=f"Booking Slot: Day {d}, Time {t}").pack(pady=5)

    # Create a Listbox to display customers
    user_listbox = tk.Listbox(slot_window, width=50, height=20)
    user_listbox.pack(pady=10)

    for customer in customers:
        user_listbox.insert(tk.END, f"{customer.userid}: {customer.fname} {customer.sname}")

    # Define the callback for selecting a customer
    def on_select_user(event):
        selected_index = user_listbox.curselection()
        if selected_index:
            userindex = selected_index[0]
            customer_id = customers[userindex].userid
            messagebox.showinfo("User ID", f"Selected User ID: {customer_id}")
            update_booking(d, t, customer_id, filename)
            slot_window.destroy()

    user_listbox.bind("<<ListboxSelect>>", on_select_user)

    # Add a close button
    tk.Button(slot_window, text="Close", command=slot_window.destroy).pack(pady=10)

def update_booking(row, col, customer_id, filename):
    try:
        with open(filename, "rb") as f:
            booking = pickle.load(f)

        # Update the booking slot
        booking[row][col].customer_id = customer_id

        # Save the updated booking back to the file
        with open(filename, "wb") as f:
            pickle.dump(booking, f)

        messagebox.showinfo("Success", "Booking updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update booking: {e}")


#login()
#create_user()
#edit_user()
#search_user()
#delete_user()
#create_staff()
#main_menu()
#create_booking()
#booking_function()
#create_booking()
