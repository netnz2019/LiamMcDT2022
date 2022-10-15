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

        outer_frame = LabelFrame(root)
        outer_frame.pack()

        # Groups widgets together
        table_frame = LabelFrame(outer_frame, text="Product List")
        table_frame.pack(expand = 'yes', padx=15, pady=15)

        # Code for creating table
        for r in range(total_rows):
            print(r)
            for c in range(total_columns):
                self.__x = StringVar()
                self.__x.set(lst[r][c])
                print(c)

                if c == 1: # change width of product name labels
                    self.l = Label(table_frame, textvariable=self.__x, width=40, fg='blue', font=('Arial',12,'bold'), justify='left')
                elif c == 0: # change width of product code labels
                    self.l = Label(table_frame, textvariable=self.__x, width=10, fg='blue', font=('Arial',12,'bold'), justify="left")
                elif r >= 1 and c == 7: # allows user to change status value
                    __sttus = ["Paid", "Due", "Sent"]
                    status = StringVar()
                    status.set(__sttus[1])
                    self.l = ttk.Combobox(table_frame, textvariable=status, state="readonly", width=10, font=('Arial',12,'bold'), justify=RIGHT)
                    self.l['values'] = __sttus
                else: # defualt Label settings
                    self.l = Label(table_frame, textvariable=self.__x, width=10, fg='blue', font=('Arial',12,'bold'), justify=RIGHT)

                self.l.grid(row=r, column=c)

        # ADDING A SCROLLBAR
        #myscrollbar = Scrollbar(table_frame)
        #myscrollbar.pack(side=RIGHT, fill=BOTH)

        #table_frame.config(yscrollcomand=myscrollbar.set)
        #myscrollbar.config(command=table_frame.yview)

lst = [("Inv. Num", "Client", "Address", "Total Cost", "Total RRP", "DoI", "Date Due", "Status"), ("1", "Someone", "113 Johns Rd, Bryndwr", "$420.69", "$841.38", "29/09/22", "10/10/22", "Paid")] # List of Orders

filepath = 'ClientPricelist2022_test.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(map(tuple, Reader)) # Converts into tuple

print(Data)

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

#-------------------------------|Windows|-------------------------------
# Orders window
root = Tk()
root.title("Orders")
root.geometry("1750x750") # might change this later

Orders = []

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
