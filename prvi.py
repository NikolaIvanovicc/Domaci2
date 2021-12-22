from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if ime_text.get() == '' or prezime_text.get() == '' or godina_text.get() == '' or ocjena_text.get() == '':
        messagebox.showerror('Greska', 'Popunite sva polja')
        return
    db.insert(ime_text.get(), prezime_text.get(),
              godina_text.get(), ocjena_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (ime_text.get(), prezime_text.get(),
                            godina_text.get(), ocjena_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        ime_entry.delete(0, END)
        ime_entry.insert(END, selected_item[1])
        prezime_entry.delete(0, END)
        prezime_entry.insert(END, selected_item[2])
        godina_entry.delete(0, END)
        godina_entry.insert(END, selected_item[3])
        ocjena_entry.delete(0, END)
        ocjena_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], ime_text.get(), prezime_text.get(),
              godina_text.get(), ocjena_text.get())
    populate_list()


def clear_text():
    ime_entry.delete(0, END)
    prezime_entry.delete(0, END)
    godina_entry.delete(0, END)
    ocjena_entry.delete(0, END)


# Create window object
app = Tk()

# ime studenta
ime_text = StringVar()
ime_lable = Label(app, text='ime ', font=('bold', 14), pady=20)
ime_lable.grid(row=0, column=0, sticky=W)
ime_entry = Entry(app, textvariable=ime_text)
ime_entry.grid(row=0, column=1)
# prezime
prezime_text = StringVar()
prezime_label = Label(app, text='prezime', font=('bold', 14))
prezime_label.grid(row=0, column=2, sticky=W)
prezime_entry = Entry(app, textvariable=prezime_text)
prezime_entry.grid(row=0, column=3)
# godina skolovanja
godina_text = StringVar()
godina_label = Label(app, text='godina', font=('bold', 14))
godina_label.grid(row=1, column=0, sticky=W)
godina_entry = Entry(app, textvariable=godina_text)
godina_entry.grid(row=1, column=1)
# ocjena
ocjena_text = StringVar()
ocjena_label = Label(app, text='ocjna', font=('bold', 14))
ocjena_label.grid(row=1, column=2, sticky=W)
ocjena_entry = Entry(app, textvariable=ocjena_text)
ocjena_entry.grid(row=1, column=3)
# lista studenata
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll 
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add ', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove ', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update ', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Part Manager')
app.geometry('700x350')

# Populate data
populate_list()

# Start program
app.mainloop()

