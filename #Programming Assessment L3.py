# Programming Assessment L3
# Liam McNeill
# SkinTech Finance GUI App

#-------------------------------|Imports|-------------------------------
from tkinter import *
from tkinter import ttk
from tkinter import dialog
from tkinter import filedialog
import csv # better than excel
import pickle

#--------------------------------|Class|--------------------------------
class Table:
     
    def __init__(self, root):

        # Groups widgets together
        label_frame = LabelFrame(root, text="Product List")
        label_frame.pack(expand = 'yes', fill = 'both', padx=15, pady=15)

        # code for creating table
        for r in range(total_rows):
            print(r)
            for c in range(total_columns):
                self.x = StringVar()
                self.x.set(Data[r][c])
                print(c)

                if c == 1:
                    self.e = Label(label_frame, textvariable=self.x, width=40, fg='blue', font=('Arial',12,'bold'), justify="left")
                elif c == 0:
                    self.e = Label(label_frame, textvariable=self.x, width=10, fg='blue', font=('Arial',12,'bold'), justify=LEFT)
                else:
                    self.e = Label(label_frame, textvariable=self.x, width=10, fg='blue', font=('Arial',12,'bold'), justify=RIGHT)

                self.e.grid(row=r, column=c)

        #ADDING A SCROLLBAR
        #myscrollbar = Scrollbar(label_frame)
        #myscrollbar.pack(side=RIGHT, fill=BOTH)

        #label_frame.config(yscrollcomand=myscrollbar.set)
        #myscrollbar.config(command=label_frame.yview)

filepath = 'ClientPricelist2022_test.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(map(tuple, Reader)) # Converts into tuple

print(Data)

# find total number of rows and
# columns in list
total_rows = len(Data)
total_columns = len(Data[0])

#-------------------------------|Windows|-------------------------------
# Orders window
root = Tk()
root.title("Orders")
root.geometry("500x500") # might change this later
t = Table(root)

#------------------------------|Functions|------------------------------
# Button Functions
def add_order():
    pass
def delete_order():
    pass

# Menu functions
def save_list():
    pass
def open_list():
    pass

#-------------------------------|Variables|-----------------------------
OrdersVar = StringVar()
OrdersVar.set("Orders")

ProductVar = StringVar()
ProductVar.set("Product") # Will be used when making/adding orders

filepath = 'ClientPricelist2022.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0]) # gets rid of header row

# Client List variables
Invoice_num = [] 
for product in list(range(0, len(Data))):
    Invoice_num.append(Data[product][0])
Invoice = StringVar(value = Invoice_num)

Prod_Name = []
for product in list(range(0, len(Data))):
    Prod_Name.append(Data[product][1])
Name = StringVar(value = Prod_Name)

Price = []
for product in list(range(0, len(Data))):
    Price.append(Data[product][2].strip('$'))
Cost = DoubleVar(value = Price)

Retail_price = []
for product in list(range(0, len(Data))):
    Retail_price.append(Data[product][3].strip('$'))
rrp = DoubleVar(value = Retail_price)
print(Retail_price[0] + Price[0])

# Create a Listbox frame
list_frame = Frame(root)
list_frame.pack(pady=10)

# Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#---------------------------------|GUI|---------------------------------
# Login Canvas
login_canvas = Canvas(root)

# Main Canvas
main_canvas = Canvas(root)

# Will change pack() to grid() in later version
OrdersLabel = Label(root, textvariable=OrdersVar)
OrdersLabel.pack()

# create entry box to add orders to the list
order_entry = Entry(root)
order_entry.pack(pady=20)

# Add & delete buttons
add_button = Button(button_frame, text="Add Order", activebackground="green", activeforeground="white", command=add_order)
delete_button = Button(button_frame, text="Delete Order", activebackground="green", activeforeground="white", command=delete_order)
add_button.grid(row=1, column=0)
delete_button.grid(row=1, column=1, padx=20)

#---------------------------------|Menu|--------------------------------
# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_list) # Dropdown option
file_menu.add_command(label="open", command=open_list)

#-------------------------------|Mainloop|------------------------------
root.mainloop()
