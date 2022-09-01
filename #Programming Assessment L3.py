#Programming Assessment L3
#Liam McNeill
#SkinTech Finance GUI App

#-------------------------------|Imports|-------------------------------
from tkinter import *
from tkinter import ttk
from tkinter import dialog
from tkinter import filedialog
import csv #better than excel
import pickle

#-------------------------------|Windows|-------------------------------
#Orders window
root = Tk()
root.title("Orders")
root.geometry("500x500")#might change this later

#------------------------------|Functions|------------------------------
#Button Functions
def add_order():
    product_list.insert(END, order_entry.get())
    order_entry.delete(0, END) #Gets rid of whatever is in the entry.
def delete_order():
    product_list.delete(ANCHOR)

#Menu functions
def save_list():
    file_name = filedialog.asksaveasfilename(title="Save File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        
    #Grab all the orders from the list
    orders = product_list.get(0, END)

    #Open file
    output_file = open(file_name, 'wb')

    #Actually add the stuff to the file
    pickle.dump(orders, output_file)
def open_list():
    file_name = filedialog.askopenfilename(title="Open File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    
    if file_name:
        #Delete currently open file
        product_list.delete(0, END)

        #Open File
        input_file = open(file_name, 'rb')

        #Load date
        orders = pickle.load(input_file)

        #Output order to the screen
        for order in orders:
            product_list.insert(END, order)

#-------------------------------|Variables|-----------------------------
OrdersVar = StringVar()
OrdersVar.set("Orders")

ProductVar = StringVar()
ProductVar.set("Product") #Will be used when making/adding orders

filepath = 'ClientPricelist2022.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0]) # gets rid of header row

#Client List variables
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

#Create a Listbox frame
list_frame = Frame(root)
list_frame.pack(pady=10)

#Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#---------------------------------|GUI|---------------------------------
#Login Canvas
login_canvas = Canvas(root)

#Main Canvas
main_canvas = Canvas(root)

#Will change pack() to grid() in later version
OrdersLabel = Label(root, textvariable=OrdersVar)
OrdersLabel.pack()

product_list = Listbox(list_frame,
    listvariable = rrp,
    width=100,
    height=15,
    bg="SystemButtonFace",
    bd=5,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none", #line under selected order is gone
    )
product_list.pack(side=LEFT, fill=BOTH)

#Add scrollbar
order_scrollbar = Scrollbar(list_frame)
order_scrollbar.pack(side=RIGHT, fill=BOTH)

product_list.config(yscrollcommand=order_scrollbar.set)
order_scrollbar.config(command=product_list.yview)

#create entry box to add orders to the list
order_entry = Entry(root)
order_entry.pack(pady=20)

#Add & delete buttons
add_button = Button(button_frame, text="Add Order", activebackground="green", activeforeground="white", command=add_order)
delete_button = Button(button_frame, text="Delete Order", activebackground="green", activeforeground="white", command=delete_order)
add_button.grid(row=1, column=0)
delete_button.grid(row=1, column=1, padx=20)

#---------------------------------|Menu|--------------------------------
#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_list) #Dropdown option
file_menu.add_command(label="open", command=open_list)

#-------------------------------|Mainloop|------------------------------
root.mainloop()
