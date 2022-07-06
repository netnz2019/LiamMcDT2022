#Programming Assessment L3
#Liam McNeill
#SkinTech Finance GUI App

#-------------------------------|Imports|-------------------------------
from tkinter import *
from tkinter import ttk

#-------------------------------|Windows|-------------------------------
#Orders window
root = Tk()
root.title("Orders")

#-------------------------------|Widgets|-------------------------------
orders = StringVar()
orders.set("Orders") #This will make changes to code easier

#Will change pack() to grid() in later version
OrdersLabel = Label(root, textvariable=orders, justify="center")
OrdersLabel.pack()

OrdersButton = Button(root, textvariable=orders, justify="left")
OrdersButton.pack()

AddOrder = Button(root, text="Add Order", justify="left") #will be used to add orders in later version
AddOrder.pack()

#-------------------------------|Mainloop|-------------------------------
root.mainloop()