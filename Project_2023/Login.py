from tkinter import messagebox
import mysql.connector as con
import tkinter as tk


    
    

def create_login():

    

            
    LOGIN = tk.Tk()
    LOGIN.title("Login") 
    LOGIN.state('zoomed')
    LOGIN.config(bg='#22aa66')


    user_name_entry=tk.StringVar()
    account_number_=tk.StringVar()

    def log_in():
        username = username_entry.get()
        account_number = account_number_entry.get()

        try:
            dbcon = con.connect(host='localhost', user='root', passwd='GHOST', charset='utf8', database='ip_proj')
            cursor = dbcon.cursor()
            query = "SELECT * FROM user_data WHERE username = %s AND account_number = %s"
            cursor.execute(query, (username, account_number))
            existing_record = cursor.fetchone()
            if existing_record:
                messagebox.showinfo('Yess',existing_record)
                LOGIN.destroy()  # Close login window
                      
    
        except con.Error as error:
            print(f"Error: {error}")
            messagebox.showinfo("Problem", f"Error: {error}")
        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

            else:
                messagebox.showerror("Login Failed", "Invalid credentials")

    username_label = tk.Label(LOGIN, text="Username :" , font=("Arial",32) ,bg='#22aa66')
    username_label.place(x=250,y=250)

    username_entry = tk.Entry(LOGIN , font=("Arial",29), textvariable=user_name_entry)
    username_entry.place(x=650,y=250)

    username_entry_clear = tk.Button(LOGIN, text="Clear", command=lambda: user_name_entry.set(""), font=("Arial", 10), bg='white', fg='black')
    username_entry_clear.place(x=1200, y=260)

    account_number_label = tk.Label(LOGIN, text="Account Number :", font=("Arial",32) , bg='#22aa66')
    account_number_label.place(x=250,y=400)

    account_number_entry = tk.Entry(LOGIN, font=("Arial",29), textvariable=account_number_)
    account_number_entry.place(x=650,y=400)

    account_entry_clear = tk.Button(LOGIN, text="Clear", command=lambda: account_number_.set(""), font=("Arial", 10), bg='white', fg='black')
    account_entry_clear.place(x=1200, y=410)

    

    login_ = tk.Button(LOGIN, text = 'LOGIN' , command = log_in ,font=("Arial",29) ,bg='red')
    login_.place(x=600,y=600)


    LOGIN.mainloop()

create_login()