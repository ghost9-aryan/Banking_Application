import tkinter as tk
from tkinter import messagebox
import mysql.connector as con
import datetime as dt
import random
import re

def create_account():
    def show_warning_box():
        messagebox.showwarning("Warning", "Record Already Exists !!")

    def check_existing(ach_name, ad_num):
        try:
            dbcon = con.connect(host='localhost', user='root', passwd='GHOST', charset='utf8', database='ip_proj')
            cursor = dbcon.cursor()
            query = "SELECT * FROM user_data WHERE username = %s AND aadhaar_number = %s"
            cursor.execute(query, (ach_name, ad_num))
            existing_record = cursor.fetchone()
            if existing_record:
                return True
            else:
                return False
        except con.Error as error:
            print(f"Error: {error}")
            return False
        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    def submit(ach_name, ad_num, address, state, phone_num):
        ach_name = re.sub(r'\s+', ' ', ach_name)
        address = re.sub(r'\s+', ' ', address)
        state = re.sub(r'\s+', ' ', state)

        current_date = dt.datetime.now()
        cur_date = current_date.strftime("%Y-%m-%d")

        def generate_random_unique_number(length):
            if length > 13:
                raise ValueError("Error")

            digits = list(range(10))
            random.shuffle(digits)
            unique_number = ''.join(map(str, digits))

            if len(unique_number) < length:
                unique_number += ''.join(map(str, random.choices(range(10), k=length - len(unique_number))))

            return unique_number[:length]

        length = 13  # Number of digits in the unique number
        account_num = generate_random_unique_number(length)
        print('Acc_Number : ', account_num)

        if ach_name and ad_num:
            record_exists = check_existing(ach_name, ad_num)
            if record_exists:
                show_warning_box()
            else:
                try:
                    dbcon = con.connect(host='localhost', user='root', passwd='GHOST', charset='utf8', database='ip_proj')
                    cursor = dbcon.cursor()
                    if state.strip() == '' or address.strip() == '':
                        print('Address and State Fields are Required')
                        messagebox.showerror('Error', 'Address and State Fields are Required !!')
                    else:
                        query = "INSERT INTO user_data (username, aadhaar_number, address, state_name, phone_number, date_of_issue, account_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(query, (ach_name, ad_num, address, state, phone_num, cur_date, account_num))
                        dbcon.commit()
                        print("Account Created!!")
                        messagebox.showinfo("Success", "Account Created Successfully !!")
                except con.Error as error:
                    if "chk_aadhaar_length" in str(error):
                        print(f"Error: {error}")
                        messagebox.showinfo("Problem", "Invalid Aadhaar Number !!")
                    elif "chk_phone_number_length" in str(error):
                        print(f"Error: {error}")
                        messagebox.showinfo("Problem", "Invalid Phone Number !!")
                    else:
                        print(f"Error: {error}")
                        messagebox.showinfo("Problem", f"Error: {error}")
                finally:
                    if dbcon.is_connected():
                        cursor.close()
                        dbcon.close()
                        account_holder_name.set("")
                        aadhaar_number.set("")
                        phone_number.set("")
                        address_entry.delete(0, tk.END)
                        state_entry.delete(0, tk.END)

    def exit_app():
        main.destroy()
    
    
    bgc = 'grey'
    main = tk.Tk()
    main.title("Create Account")
    main.state('zoomed')
    main.config(bg=bgc)

    Bank_name = tk.Label(main, text="HDFC Bank", font=("OCR A", 45), fg='red', bg=bgc)
    Bank_name.place(x=500, y=25)

    account_holder_name = tk.StringVar()
    aadhaar_number = tk.StringVar()
    address = tk.StringVar()
    state_name = tk.StringVar()
    phone_number = tk.StringVar()

    ach_name = tk.Label(main, text="Account Holder's Name :", font=('Arial', 35), bg=bgc)
    ach_name.place(x=200, y=180)
    ah_entry = tk.Entry(main, font=('Arial', 20), textvariable=account_holder_name)
    ah_entry.place(x=850, y=193)
    ah_entry_clear = tk.Button(main, text='Clear', command=lambda: account_holder_name.set(""), font=("Arial", 10), bg='white', fg='black')
    ah_entry_clear.place(x=1250, y=193)

    aadhar_label = tk.Label(main, text="Aadhaar Number :", font=('Arial', 35), bg=bgc)
    aadhar_label.place(x=200, y=250)
    aadhar_entry = tk.Entry(main, font=('Arial', 20), textvariable=aadhaar_number)
    aadhar_entry.place(x=850, y=263)
    aadhar_entry_clear = tk.Button(main, text='Clear', command=lambda: aadhaar_number.set(""), font=("Arial", 10), bg='white', fg='black')
    aadhar_entry_clear.place(x=1250, y=263)

    phone_label = tk.Label(main, text="Phone Number :", font=('Arial', 35), bg=bgc)
    phone_label.place(x=200, y=320)
    phone_entry = tk.Entry(main, font=('Arial', 20), textvariable=phone_number)
    phone_entry.place(x=850, y=333)
    phone_entry_clear = tk.Button(main, text="Clear", command=lambda: phone_number.set(""), font=("Arial", 10), bg='white', fg='black')
    phone_entry_clear.place(x=1250, y=333)

    address_label = tk.Label(main, text="Address :", font=('Arial', 35), bg=bgc)
    address_label.place(x=200, y=390)
    address_entry = tk.Entry(main, font=('Arial', 20), textvariable=address)
    address_entry.place(x=850, y=403)
    address_entry_clear = tk.Button(main, text="Clear", command=lambda: address.set(""), font=("Arial", 10), bg='white', fg='black')
    address_entry_clear.place(x=1250, y=403)

    state_label = tk.Label(main, text="State :", font=('Arial', 35), bg=bgc)
    state_label.place(x=200, y=470)
    state_entry = tk.Entry(main, font=('Arial', 20), textvariable=state_name)
    state_entry.place(x=850, y=476)
    state_entry_clear = tk.Button(main, text='Clear', command=lambda: state_name.set(""), font=("Arial", 10), bg='white', fg='black')
    state_entry_clear.place(x=1250, y=476)

    sub = tk.Button(main, text="SUBMIT", command=lambda: submit(account_holder_name.get(), aadhaar_number.get(), address_entry.get(), state_entry.get(), phone_number.get()), font=("Arial", 42), bg='green', fg='white')
    sub.place(x=1050, y=600)

    ext = tk.Button(main, text="Exit", command=exit_app, font=("Arial", 32), bg='white', fg='black')
    ext.place(x=30, y=630)

    main.mainloop()                  
    
create_account()