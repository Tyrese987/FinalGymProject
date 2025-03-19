import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle

class BookingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Booking System")
        
        # Define days and time slots
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.times = ["12", "2PM", "4PM", "6PM", "8PM"]
        
        # Create a dictionary to hold booking data:
        # bookings[day][time] is a list of bookings (each a dict with user_id and name)
        self.bookings = { day: { time: [] for time in self.times } for day in self.days }
        
        # Build the grid
        self.create_grid()
    
    def create_grid(self):
        # First row: Time slot headers
        tk.Label(self, text="Day/Time", borderwidth=2, relief="ridge", width=12).grid(row=0, column=0)
        for col, time in enumerate(self.times, start=1):
            tk.Label(self, text=time, borderwidth=2, relief="ridge", width=12).grid(row=0, column=col)
        
        # Create each row for days and add buttons for time slots
        for row, day in enumerate(self.days, start=1):
            tk.Label(self, text=day, borderwidth=2, relief="ridge", width=12).grid(row=row, column=0)
            for col, time in enumerate(self.times, start=1):
                # Each cell is a button that calls book_slot when clicked.
                btn = tk.Button(self, text="Book", bg="lightblue", width=12,
                                command=lambda d=day, t=time: self.book_slot(d, t))
                btn.grid(row=row, column=col, padx=1, pady=1)
        
        # Add a button to remove a user by user ID
        remove_btn = tk.Button(self, text="Remove User", command=self.remove_user)
        remove_btn.grid(row=len(self.days)+1, column=0, columnspan=len(self.times)+1, pady=10)

        # Add a button to edit a booking slot name
        edit_btn = tk.Button(self, text="Edit Booking", command=self.edit_bookings_slot_name)
        edit_btn.grid(row=len(self.days)+2, column=0, columnspan=len(self.times)+1, pady=10)
    
    def book_slot(self, day, time):
        """Allows staff to add a booking to the specified slot."""
        current_bookings = self.bookings[day][time]
        booking_list = "\n".join(f"{b['user_id']}: {b['name']}" for b in current_bookings) or "No bookings yet."
        prompt = (f"Bookings for {day} at {time} (max 15):\n{booking_list}\n\n"
                  "Enter new booking as 'user_id,name':")
        result = simpledialog.askstring("New Booking", prompt, parent=self)
        
        if result:
            try:
                user_id, name = result.split(",")
                user_id, name = user_id.strip(), name.strip()
            except ValueError:
                messagebox.showerror("Input Error", "Format must be: user_id,name")
                return
            
            if len(current_bookings) >= 15:
                messagebox.showerror("Full Slot", "This slot already has 15 bookings!")
                return
            
            # Add the booking and notify the user
            current_bookings.append({"user_id": user_id, "name": name})
            messagebox.showinfo("Success", f"Booking added for {name} at {day} {time}.")
    
    def remove_user(self):
        """Removes all bookings for the specified user ID."""
        user_id = simpledialog.askstring("Remove User", "Enter user ID to remove:", parent=self)
        if user_id:
            user_id = user_id.strip()
            removed = False
            for day in self.days:
                for time in self.times:
                    original = len(self.bookings[day][time])
                    self.bookings[day][time] = [b for b in self.bookings[day][time] if b['user_id'] != user_id]
                    if len(self.bookings[day][time]) < original:
                        removed = True
            
            if removed:
                messagebox.showinfo("User Removed", f"All bookings for user ID '{user_id}' have been removed.")
            else:
                messagebox.showinfo("Not Found", f"No bookings found for user ID '{user_id}'.")

    def edit_bookings_slot_name(self):
        """Edit the name of a booking in a specified slot."""
        day = simpledialog.askstring("Edit Booking", "Enter the day of the booking:", parent=self)
        time = simpledialog.askstring("Edit Booking", "Enter the time of the booking:", parent=self)
        user_id = simpledialog.askstring("Edit Booking", "Enter the user ID to edit:", parent=self)
        new_name = simpledialog.askstring("Edit Booking", "Enter the new name for the booking:", parent=self)

        if not (day and time and user_id and new_name):
            messagebox.showerror("Input Error", "All fields are required.")
            return

        if day not in self.bookings or time not in self.bookings[day]:
            messagebox.showerror("Input Error", "Invalid day or time.")
            return

        for booking in self.bookings[day][time]:
            if booking['user_id'] == user_id:
                booking['name'] = new_name
                messagebox.showinfo("Success", f"Booking for user ID '{user_id}' has been updated to '{new_name}'.")
                return

        messagebox.showerror("Not Found", f"No booking found for user ID '{user_id}' at {day} {time}.")

if __name__ == "__main__":
    app = BookingApp()
    app.mainloop()
