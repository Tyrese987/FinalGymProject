import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os


class BookingSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gym Booking System")

        # Days and time slots for booking
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.times = ["12am", "2pm", "4pm", "6pm", "8pm"]

        # Load bookings and user data
        self.bookings = self.load_data("bookings.pkl", default={day: {time: [] for time in self.times} for day in self.days})
        self.users = self.load_data("my_customer.pkl", default={})

        # Create booking interface
        self.create_grid()

    def load_data(self, filename, default):
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                return pickle.load(f)
        return default

    def save_data(self, filename, data):
        with open(filename, "wb") as f:
            pickle.dump(data, f)

    def create_grid(self):
        tk.Label(self, text="Day/Time", borderwidth=2, relief="ridge", width=12).grid(row=0, column=0)

        for col, time in enumerate(self.times, start=1):
            tk.Label(self, text=time, borderwidth=2, relief="ridge", width=12).grid(row=0, column=col)

        for row, day in enumerate(self.days, start=1):
            tk.Label(self, text=day, borderwidth=2, relief="ridge", width=12).grid(row=row, column=0)
            for col, time in enumerate(self.times, start=1):
                btn = tk.Button(self, text="Book", bg="lightblue", width=12,
                                command=lambda d=day, t=time: self.book_slot(d, t))
                btn.grid(row=row, column=col, padx=1, pady=1)

    def authenticate_user(self):
        user_id = simpledialog.askinteger("User ID", "Enter your User ID:")
        if user_id is None or user_id not in self.users:
            messagebox.showerror("Error", "Invalid User ID.")
            return None, None

        user_name = simpledialog.askstring("User Name", f"Confirm your name ({self.users[user_id]}):")
        if user_name != self.users[user_id]:
            messagebox.showerror("Error", "Name does not match registered User ID.")
            return None, None

        return user_id, user_name

    def book_slot(self, day, time):
        user_id, user_name = self.authenticate_user()
        if user_id is None:
            return

        current_bookings = self.bookings[day][time]
        if len(current_bookings) < 15:
            current_bookings.append({"user_id": user_id, "name": user_name})
            self.save_data("my_customer.pkl", self.bookings)
            messagebox.showinfo("Success", f"Booked {day} at {time} for {user_name}.")
        else:
            messagebox.showerror("Error", "This slot is fully booked.")

    def cancel_booking(self):
        user_id, user_name = self.authenticate_user()
        if user_id is None:
            return

        user_bookings = [(day, time) for day in self.days for time in self.times 
                         if any(b["user_id"] == user_id for b in self.bookings[day][time])]

        if not user_bookings:
            messagebox.showinfo("No Bookings", "You have no bookings to cancel.")
            return

        choice = simpledialog.askstring("Cancel Booking", f"Your bookings: {user_bookings}\nEnter one to cancel (e.g., 'Monday 4pm'):")
        if choice:
            day, time = choice.split()
            if day in self.days and time in self.times:
                self.bookings[day][time] = [b for b in self.bookings[day][time] if b["user_id"] != user_id]
                self.save_data("bookings.pkl", self.bookings)
                messagebox.showinfo("Cancelled", f"Booking for {choice} has been cancelled.")
            else:
                messagebox.showerror("Error", "Invalid day or time.")

    def edit_booking_name(self):
        user_id, user_name = self.authenticate_user()
        if user_id is None:
            return

        user_bookings = [(day, time) for day in self.days for time in self.times 
                         if any(b["user_id"] == user_id for b in self.bookings[day][time])]

        if not user_bookings:
            messagebox.showinfo("No Bookings", "You have no bookings to edit.")
            return

        choice = simpledialog.askstring("Edit Booking", f"Your bookings: {user_bookings}\nEnter one to edit (e.g., 'Monday 4pm'):")
        if choice:
            try:
                day, time = choice.split()
                if day in self.days and time in self.times:
                    new_name = simpledialog.askstring("New Name", "Enter the new name:")
                    if new_name:
                        for booking in self.bookings[day][time]:
                            if booking["user_id"] == user_id:
                                booking["name"] = new_name
                        self.save_data("bookings.pkl", self.bookings)
                        messagebox.showinfo("Success", f"Booking name updated to {new_name}.")
                    else:
                        messagebox.showerror("Error", "Name cannot be empty.")
                else:
                    messagebox.showerror("Error", "Invalid booking selection.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input format. Use 'Day Time' (e.g., 'Monday 4pm').")


if __name__ == "__main__":
    app = BookingSystem()
    tk.Button(app, text="Cancel Booking", command=app.cancel_booking, bg="black", fg="white", width=15).grid(row=len(app.days) + 2, column=0, columnspan=len(app.times))
    tk.Button(app, text="Edit Booking Name", command=app.edit_booking_name, bg="green", fg="white", width=15).grid(row=len(app.days) + 3, column=0, columnspan=len(app.times))
    app.mainloop()
