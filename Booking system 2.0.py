import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os

class Booking(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Booking System")
        # Days and time slots for booking
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.times = ["12am", "2pm", "4pm", "6pm", "8pm"]
        # The bookings dictionary will store the bookings for each day and time
        self.bookings = self.load_bookings()
        self.create_grid()

    def load_bookings(self):
        if os.path.exists("User_Gym.pkl"):
            with open("User_Gym.pkl", "rb") as f:
                return pickle.load(f)
        else:
            messagebox.showerror("Error", "Bookings file not found.")
            return { day: { time: [] for time in self.times } for day in self.days }

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

    def book_slot(self, day, time):
        # Getting and validating the user ID
        user_id = simpledialog.askinteger("User ID", "Enter your user ID:")
        if user_id is None:
            return
        # Book for specific slot
        current_bookings = self.bookings[day][time]
        booking_list = "\n".join(f"{b['user_id']}: {b['name']}" for b in current_bookings) or "No bookings yet."
        prompt = (f"Bookings for {day} at {time} (max 15):\n{booking_list}\n\n"
                  "Enter your name to book this slot:")
        user_name = simpledialog.askstring("User Name", prompt)
        if user_name:
            if len(current_bookings) < 15:
                current_bookings.append({"user_id": user_id, "name": user_name})
                self.save_bookings()
                messagebox.showinfo("Success", f"Booked {day} at {time} for {user_name}.")
            else:
                messagebox.showerror("Error", "This slot is fully booked.")

    def save_bookings(self):
        with open("User_Gym.pkl", "wb") as f:
            pickle.dump(self.bookings, f)

# Create and run the booking system
if __name__ == "__main__":
    app = Booking()
    app.mainloop()