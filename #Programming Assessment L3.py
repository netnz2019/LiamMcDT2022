#Programming Assessment L3
#Liam McNeill
#SkinTech Finance GUI App

#-------------------------------|Imports|-------------------------------
from tkinter import *
from tkinter import ttk
from tkinter import dialog

#-------------------------------|Windows|-------------------------------
#Orders window
root = Tk()
root.title("Orders")
root.geometry("500x500")#might change this later

#-------------------------------|Variables|-----------------------------
OrdersVar = StringVar()
OrdersVar.set("Orders")

#-------------------------------|Widgets|-------------------------------
#Will change pack() to grid() in later version
OrdersLabel = Label(root, textvariable=OrdersVar, justify='center')
OrdersLabel.pack()

#Create Frame
order_frame = Frame(root)
order_frame.pack(pady=10)

order_list = Listbox(order_frame, 
    width=100,
    height=15,
    bg="SystemButtonFace",
    bd=5,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"#line under selected order is gone
    )

order_list.pack(side=LEFT, fill=BOTH)

#Create product list
Orders = ["Sunscreen", "SunLotion"] #Add list of SkinTech order but for now just have product names for testing
#Add product list
for Order in Orders:
    order_list.insert(END, Order)

#Add scrollbar
order_scrollbar = Scrollbar(order_frame)
order_scrollbar.pack(side=RIGHT, fill=BOTH)

order_list.config(yscrollcommand=order_scrollbar.set)
order_scrollbar.config(command=order_list.yview)

#create entry box to add products to the list
order_entry = Entry(root)
order_entry.pack(pady=20)

#Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#Button Functions
def add_order():
    order_list.insert(END, order_entry.get())
    order_entry.delete(0, END) #Gets rid of whatever is in the entry.
def delete_order():
    order_list.delete(ANCHOR)

#Menu functions
def save_list():
    pass        

#Add & delete buttons
add_button = Button(button_frame, text="Add Order", command=add_order)
delete_button = Button(button_frame, text="Delete Order", command=delete_order)
add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20)

#Create Menu
menu1 = Menu(root)
root.config(menu=menu1)

#Add items to the menu
file_menu = Menu(menu1, tearoff=False)
menu1.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_list)
#Possibly add a "Save As" option?

#-------------------------------|Mainloop|------------------------------
root.mainloop()