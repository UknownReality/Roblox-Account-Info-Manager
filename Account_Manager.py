from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def populate_list():
    info_list.delete(0, END)
    for row in db.fetch():
        info_list.insert(END, row)


def add_item():
    if username_text.get() == '' or sold_text.get() == '' or password_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(username_text.get(), sold_text.get(),
              password_text.get(), price_text.get())
    info_list.delete(0, END)
    info_list.insert(END, (username_text.get(), sold_text.get(),
                            password_text.get(), price_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = info_list.curselection()[0]
        selected_item = info_list.get(index)

        username_entry.delete(0, END)
        username_entry.insert(END, selected_item[1])
        sold_entry.delete(0, END)
        sold_entry.insert(END, selected_item[2])
        password_entry.delete(0, END)
        password_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], username_text.get(), sold_text.get(),
              password_text.get(), price_text.get())
    populate_list()


def clear_text():
    username_entry.delete(0, END)
    sold_entry.delete(0, END)
    password_entry.delete(0, END)
    price_entry.delete(0, END)


# Create window object
app = Tk()

# username
username_text = StringVar()
username_label = Label(app, text='Username', font=('bold', 14), pady=20)
username_label.grid(row=0, column=0, sticky=W)
username_entry = Entry(app, textvariable=username_text)
username_entry.grid(row=0, column=1)
# sold
sold_text = StringVar()
sold_label = Label(app, text='Sold', font=('bold', 14))
sold_label.grid(row=0, column=2, sticky=W)
sold_entry = Entry(app, textvariable=sold_text)
sold_entry.grid(row=0, column=3)
# password
password_text = StringVar()
password_label = Label(app, text='Password', font=('bold', 14))
password_label.grid(row=1, column=0, sticky=W)
password_entry = Entry(app, textvariable=password_text)
password_entry.grid(row=1, column=1)
# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)
# usernames List (Listbox)
info_list = Listbox(app, height=8, width=50, border=0)
info_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
info_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=info_list.yview)
# Bind select
info_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Account', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Account', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Account', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Account Manager')
app.geometry('700x350')
app.configure(background= 'grey')

# Populate data
populate_list()

# Start program
app.mainloop()
