from tkinter import messagebox
import mysql.connector as con
from acc_creation import *
import tkinter as tk

def create_login_page():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x150")

    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()

    username_entry = tk.Entry(login_window)
    username_entry.pack()

    account_number_label = tk.Label(login_window, text="Account Number:")
    account_number_label.pack()

    account_number_entry = tk.Entry(login_window)
    account_number_entry.pack()

    def login():
        username = username_entry.get()
        account_number = account_number_entry.get()

        try:
            dbcon = con.connect(host='localhost', user='root', passwd='GHOST', charset='utf8', database='ip_proj')
            cursor = dbcon.cursor()
            query = "SELECT * FROM user_data WHERE username = %s AND account_number = %s"
            cursor.execute(query, (username, account_number))
            existing_record = cursor.fetchone()
            if existing_record:
                login_window.destroy()  # Close login window
                
            else:
                messagebox.showerror("Login Failed", "Invalid credentials")
        except con.Error as error:
            print(f"Error: {error}")
            messagebox.showinfo("Problem", f"Error: {error}")
        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack()

    login_window.mainloop()
