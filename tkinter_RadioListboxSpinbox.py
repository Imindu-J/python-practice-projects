from tkinter import *

window = Tk()
window.title('GUI program')
window.minsize(width=500, height=300)

my_label = Label(text='label', font=('Arial', 24, 'bold'))
my_label.config(text='new label')
my_label.pack()

def clicked():
    new_text = entry.get()
    my_label.config(text=new_text)
    
button = Button(text='Click me', command=clicked)
button.pack()

entry = Entry(width=40)
entry.insert(END, string = 'entry')
entry.pack()

text = Text(height = 5, width = 50)
text.insert(END, 'text, it is a multy line entry')
text.focus()
text.pack()

print(text.get('1.0', END))

def spin():
    print(spinbox.get())
    
spinbox = Spinbox(from_=0, to=10, width=10, command=spin)
spinbox.pack()

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

def check_used():
    print(check_state.get())

check_state = IntVar()
check_button = Checkbutton(text='Is on?', variable=check_state, command=check_used)
check_state.get()
check_button.pack()

def radio_used():
    print(radio_state.get())
          
radio_state = IntVar()
radiobutton1 = Radiobutton(text='option1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='option2', value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))
    
listbox = Listbox(height=4)
fruits = ['Apples', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()


window.mainloop()





