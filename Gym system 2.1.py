import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import re
import random
import os
import datetime



# Classes will be defined here for the system Currently Staff and Customer 
from datetime import datetime

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

BOOKING_NAMES = [
    "Karate", 
    "MMA", 
    "Boxing", 
    "Weight Lifting", 
    "Yoga", 
    "Functional Training"
]

class Booking:
    def __init__(self, row, column, max_capacity=15):
        self.row = row
        self.column = column
        self.max_capacity = max_capacity
        self.booked_users = []
        # Set default booking name based on time slot
        self.booking_name = BOOKING_NAMES[column % len(BOOKING_NAMES)]
        
    @property
    def display_name(self):
        return f"{self.booking_name}\n{len(self.booked_users)}/{self.max_capacity}"
    
# Global lists for day/time names
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["12am", "2pm", "4pm", "6pm", "8pm"]


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
                messagebox.showerror("Login error", "Incorrect password")
                return

    if not user_found:
        messagebox.showerror("Login error", "Incorrect username and password")
        return

def booking_function():
    def create_grid():
        grid_window = tk.Toplevel(root)
        grid_window.title("Create New Booking Grid")
        
        tk.Label(grid_window, text="Enter week starting date (DD/MM/YYYY):").pack(pady=5)
        date_entry = tk.Entry(grid_window)
        date_entry.pack(pady=5)
        
        tk.Label(grid_window, text="Enter filename to save:").pack(pady=5)
        filename_entry = tk.Entry(grid_window)
        filename_entry.pack(pady=5)

        def save_grid():
            filename = filename_entry.get().strip()
            if not filename:
                messagebox.showerror("Error", "Filename cannot be empty")
                return
                
            if not filename.endswith('.pkl'):
                filename += '.pkl'
                
            try:
                # Validate date format
                start_date = date_entry.get()
                if len(start_date) != 10 or start_date[2] != '/' or start_date[5] != '/':
                    raise ValueError("Invalid date format")
                    
                # Create booking matrix with booking names
                days_count = 7  # Monday-Sunday
                time_slots = 5  # 12am, 2pm, 4pm, 6pm, 8pm
                matrix = [[Booking(row, col) for col in range(time_slots)] for row in range(days_count)]
                         
                with open(filename, "wb") as f:
                    pickle.dump({
                        'start_date': start_date,
                        'bookings': matrix
                    }, f)
                    
                messagebox.showinfo("Success", f"New booking grid for week {start_date} saved")
                grid_window.destroy()
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create grid: {str(e)}")

        tk.Button(grid_window, text="Save", command=save_grid).pack(pady=10)
        tk.Button(grid_window, text="Cancel", command=grid_window.destroy).pack(pady=5)

    root = tk.Tk()
    root.title("Gym Booking System")
    
    tk.Label(root, text="Booking Management", font=('Arial', 14)).pack(pady=10)
           
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)
    
    tk.Button(button_frame, text="Create New Week", command=create_grid).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="View/Edit Bookings", command=create_booking).pack(side=tk.LEFT, padx=10)
    tk.Button(root, text="Close", command=root.destroy).pack(pady=10)
             
    root.mainloop()

def create_booking():
    # Get all booking files
    try:
        files = [f for f in os.listdir() if f.endswith('.pkl')]
        if not files:
            messagebox.showinfo("Info", "No booking files found. Create one first.")
            return
            
        select_window = tk.Toplevel()
        select_window.title("Select Booking Week")
        
        tk.Label(select_window, text="Select a booking week:").pack(pady=10)
                
        file_listbox = tk.Listbox(select_window, width=40, height=10)
        file_listbox.pack(pady=10)
        
        for f in files:
            try:
                with open(f, 'rb') as file:
                    data = pickle.load(file)
                    file_listbox.insert(tk.END, f"{f} (Week starting: {data['start_date']})")
            except:
                file_listbox.insert(tk.END, f"{f} (DO NOT OPEN!!!)")
                
        def on_select():
            selected = file_listbox.curselection()
            if selected:
                filename = files[selected[0]]
                select_window.destroy()
                show_booking_grid(filename)
                
        tk.Button(select_window, text="Select", command=on_select).pack(pady=10)
                 
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load bookings: {str(e)}")

def show_booking_grid(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            bookings = data['bookings']
                    
        win = tk.Toplevel()
        win.title(f"Bookings - Week starting {data['start_date']}")
        
        # Header with times
        tk.Label(win, text="Time →", font=('Arial', 10)).grid(row=0, column=0)
        for col, time in enumerate(times, 1):
            tk.Label(win, text=time, font=('Arial', 10), 
                    borderwidth=1, relief='solid', width=20).grid(row=0, column=col)
        
        # Rows with bookings
        for row, day in enumerate(days, 1):
            tk.Label(win, text=day, font=('Arial', 10), 
                    borderwidth=1, relief='solid', width=15).grid(row=row, column=0)
                    
            for col in range(len(times)):
                booking = bookings[row-1][col]
                btn = tk.Button(
                    win, 
                    text=booking.display_name, 
                    width=20, 
                    height=3,
                    command=lambda r=row-1, c=col: book_slot(win, r, c, filename),
                    bg='#90EE90' if len(booking.booked_users) < booking.max_capacity else '#FFB6C1'
                )
                btn.grid(row=row, column=col+1, padx=2, pady=2)
                
                # Edit booking name button
                edit_btn = tk.Button(
                    win, 
                    text="Edit Booking", 
                    width=10,
                    command=lambda r=row-1, c=col: edit_booking_name(win, r, c, filename),
                    bg='#ADD8E6'
                )
                edit_btn.grid(row=row, column=col+len(times)+1, padx=2, pady=2)
                
    except Exception as e:
        messagebox.showerror("Error", f"Failed to display bookings: {str(e)}")

def book_slot(parent, row, col, filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            bookings = data['bookings']
            booking = bookings[row][col]
            
        # Check capacity
        if len(booking.booked_users) >= booking.max_capacity:
            messagebox.showwarning("Full", "This session is fully booked!")
            return
            
        # Load customers
        with open('User_Gym.pkl', 'rb') as f:
            customers = pickle.load(f)
            
        select_window = tk.Toplevel(parent)
        select_window.title("Select Member")
        
        tk.Label(select_window, text=f"Book {booking.booking_name}").pack(pady=10)
                
        search_frame = tk.Frame(select_window)
        search_frame.pack(pady=5)
        
        tk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        search_entry = tk.Entry(search_frame)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        def update_list():
            search_term = search_entry.get().lower()
            user_listbox.delete(0, tk.END)
            for customer in customers:
                if (search_term in customer.fname.lower() or 
                    search_term in customer.sname.lower() or
                    search_term in customer.userid.lower()):
                    user_listbox.insert(tk.END, f"{customer.userid}: {customer.fname} {customer.sname}")
        
        search_entry.bind('<KeyRelease>', lambda e: update_list())
        
        user_listbox = tk.Listbox(select_window, width=50, height=15)
        user_listbox.pack(pady=10)
        update_list()
        
        def confirm_booking():
            selected = user_listbox.curselection()
            if not selected:
                messagebox.showwarning("Error", "Please select a member")
                return
                
            customer_id = user_listbox.get(selected[0]).split(':')[0].strip()
            
            # Check if the user is already booked in another slot
            for day in bookings:
                for slot in day:
                    if customer_id in slot.booked_users:
                        messagebox.showwarning("Error", "This user is already booked in another slot!")
                        return
            
            # Add user to booked_users
            if customer_id not in booking.booked_users:
                booking.booked_users.append(customer_id)
                            
            # Save changes
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
                
            messagebox.showinfo("Success", f"Booked {customer_id} for {booking.booking_name}")
            select_window.destroy()
            parent.destroy()
            show_booking_grid(filename)
            
        tk.Button(select_window, text="Confirm Booking", command=confirm_booking).pack(pady=10)
                 
    except Exception as e:
        messagebox.showerror("Error", f"Booking failed: {str(e)}")

def edit_booking_name(parent, row, col, filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            bookings = data['bookings']
            booking = bookings[row][col]
        
        edit_window = tk.Toplevel(parent)
        edit_window.title("Edit Booking Name")
        edit_window.geometry("300x150")
        
        main_frame = ttk.Frame(edit_window, padding=20)
        main_frame.pack(fill='both', expand=True)

        ttk.Label(main_frame, text="Select Booking Name:").pack(pady=5)
        
        booking_combo = ttk.Combobox(main_frame, values=BOOKING_NAMES)
        booking_combo.set(booking.booking_name)
        booking_combo.pack(pady=5, fill='x')

        def save_changes():
            new_booking_name = booking_combo.get()
            if new_booking_name not in BOOKING_NAMES:
                messagebox.showerror("Error", "Invalid booking name selected!")
                return
            
            booking.booking_name = new_booking_name
            
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
            
            messagebox.showinfo("Success", "Booking name updated!")
            edit_window.destroy()
            parent.destroy()
            show_booking_grid(filename)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Save", command=save_changes).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Cancel", command=edit_window.destroy).pack(side='left', padx=5)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to edit booking name: {str(e)}")


if __name__ == "__main__":
    login()