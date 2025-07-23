from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def create_password():
     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

     nr_letters = random.randint(8, 10)
     nr_symbols = random.randint(2, 4)
     nr_numbers = random.randint(2, 4)

     pass_letters = [random.choice(letters) for char in range(nr_letters)]
     pass_symbols = [random.choice(symbols) for char in range(nr_symbols)]
     pass_numbers = [random.choice(numbers) for char in range(nr_numbers)]

     password_list = pass_letters + pass_symbols + pass_numbers
     random.shuffle(password_list)
     password = ''.join(password_list)

     passEntry.insert(0, password)
     pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entry():
     webEntry.delete(0, END)
     passEntry.delete(0, END)

def add_to_file():
     website = webEntry.get()
     email = emailEntry.get()
     password = passEntry.get()
     data_dict = {
          website: {
               'email': email,
               'password': password,
          }
     }

     if len(website)==0 or len(email)==0 or len(password) == 0:
          messagebox.showinfo(title='Invalid entry', message='Entries cannot be empty.')
          return

     is_ok = messagebox.askokcancel(title=website, message=f'Click Ok  to save {website}, {email} and {password}.')
     if is_ok:
          try:
               with open('data.json', 'r') as data_file:
                   data = json.load(data_file)
                   data.update(data_dict)
          except FileNotFoundError:
               data = data_dict
          finally:
               with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)

          clear_entry()
          messagebox.showinfo(message='Your data has been saved.')

'''Search for data in file'''
def search_data():
     website = webEntry.get()
     try:
          with open('data.json', 'r') as data_file:
               data = json.load(data_file)
               if website in data:
                    email = data[website]['email']
                    password = data[website]['password']
                    messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
               else:
                    messagebox.showinfo(title=website, message='Data not found')
     except FileNotFoundError:
          messagebox.showinfo(title=website, message='Data file not found')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

websiteLbl = Label(text='Website:')
websiteLbl.grid(row=1,column=0)

emailLbl = Label(text='Email/Username:')
emailLbl.grid(row=2,column=0)

passwordLbl = Label(text='Password:')
passwordLbl.grid(row=3,column=0)

webEntry = Entry(width=30)
webEntry.grid(row=1, column=1)
webEntry.focus()

emailEntry = Entry(width=48)
emailEntry.grid(row=2, column=1, columnspan=2)
emailEntry.insert(0, 'example@email.com')

passEntry = Entry(width=30)
passEntry.grid(row=3, column=1)

generateBtn = Button(text='Generate Password', width=14, command=create_password)
generateBtn.grid(row=3, column=2)

addBtn = Button(text='Add', width=36, command=add_to_file)
addBtn.grid(row=4, column=1, columnspan=2)

searchBtn = Button(text='Search', width=14, command=search_data)
searchBtn.grid(row=1, column=2)


window.mainloop()