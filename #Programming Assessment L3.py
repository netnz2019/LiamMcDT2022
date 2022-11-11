# Programming Assessment L3
# Liam McNeill
# SkinTech Finance GUI App
# Big chunk of stuff explaining how program works
# Error checking - add to write up and code

#-------------------------------|Imports|-------------------------------
from tkinter import *
from tkinter import ttk
import csv # better than excel
import pickle
import time

#--------------------------------|Class|--------------------------------
class Table:
     
    def __init__(self, root, lst):

        myscrollbar = ttk.Scrollbar(root, orient="vertical")
        myscrollbar.pack(side=RIGHT, fill=BOTH)

        add_order = LabelFrame(root, text="Add/Delete Order")
        add_order.pack(pady=20)

        outer_frame = Frame(root)
        outer_frame.pack(pady=15)

        #outer_frame.config(yscrollcomand=myscrollbar.set)
        #myscrollbar.config(command=outer_frame.yview)

        # Groups widgets together
        table_frame = LabelFrame(outer_frame, text="Order List")
        table_frame.pack(expand = 'yes', padx=15, pady=15)

        # Code for creating table
        def table():
            # find total number of rows and columns in list
            total_rows = len(lst) # decides the amount of rows via number of tuples (orders) in lst
            total_columns = len(lst[0]) # decides the amount of columns via number of values in the first tuple of lst
            for r in range(total_rows): 
                for c in range(total_columns):
                    self.__x = StringVar()
                    self.__x.set(lst[r][c])

                    if c == 1: # change width of product name labels
                        self.l = Label(table_frame, textvariable=self.__x, width=20, fg='blue', font=('Arial',12,'bold'))
                    elif c == 2:
                        self.l = Label(table_frame, textvariable=self.__x, width=30, fg='blue', font=('Arial',12,'bold'))
                    elif c == 0: # change width of product code labels
                        self.l = Label(table_frame, textvariable=self.__x, width=10, fg='blue', font=('Arial',12,'bold'))
                    elif r >= 1 and c == 7: # allows user to change status value
                        self.l = Entry(table_frame, textvariable=self.__x, width=10, font=('Arial',12,'bold'))
                    else: # defualt Label settings
                        self.l = Label(table_frame, textvariable=self.__x, width=10, fg='blue', font=('Arial',12,'bold'))

                    self.l.grid(row=r, column=c)
        
        table() # Calls the table when staring up GUI
                    

        # ADDING A SCROLLBAR
        #myscrollbar = Scrollbar(table_frame)
        #myscrollbar.pack(side=RIGHT, fill=BOTH)

        #outer_frame.config(yscrollcomand=myscrollbar.set)
        #myscrollbar.config(command=outer_frame.yview)

        #outer_frame.pack()

        #-------------------------------|Functions|-------------------------------
        # Button Functions
        def add(): # Makes order a tuple to then add to overall list
            Num = 0 # resets counter

            order = (client_entry.get(), 
                    address_entry.get(), 
                    totalcost_entry.get(), 
                    totalrrp_entry.get(), 
                    doi_entry.get(), 
                    datedue_entry.get(), 
                    status_entry.get())

            if totalcost_entry.get().isnumeric() == TRUE and totalrrp_entry.get().isnumeric() == TRUE: # Checks prices are numbers
                totalcost = "${}".format(totalcost_entry.get())
                totalrrp = "${}".format(totalrrp_entry.get())
                for i in order:
                    if len(i) > 0:
                        Num = Num + 1 # Adds to counter
                    else:
                        __f = Label(add_order, text="ENTRY IS EMPTY", fg="red", font=('Arial',10,'bold'))
                        __f.grid(row=2, column=7)            
            else:
                f = Label(add_order, text="Invalid Number", fg="red", font=('Arial',10,'bold'))
                f.grid(row=2, column=3, columnspan=2) 

            InvNum = len(lst)

            if Num == 7: # Checks counter
                order = (InvNum, 
                        client_entry.get(), 
                        address_entry.get(), 
                        totalcost, 
                        totalrrp, 
                        doi_entry.get(), 
                        datedue_entry.get(), 
                        status_entry.get())
                lst.append(order)
                table() # Recalls table so that it is updated 
            else:
                pass


        def delete_order(): # function to delete unwanted orders
            if d.get().isnumeric() == TRUE:
                if int(d.get()) <= len(lst):
                    print(len(lst))
                    for x in range(8):
                        if x == 1: # gets rid of bottom order widgets and specifies width
                            l = Label(table_frame, text="", width=20, fg='blue', font=('Arial',12,'bold'))
                        elif x == 2:
                            l = Label(table_frame, text="", width=30, fg='blue', font=('Arial',12,'bold'))
                        else: 
                            l = Label(table_frame, text="", width=10, fg='blue', font=('Arial',12,'bold'))
                        l.grid(row=len(lst)-1, column=x)

                    lst.pop(int(d.get()))
                    table() # updates table without selected order

                else:
                    pass
            else:
                b = Label(add_order, text="ENTRY ISN'T A NUMBER", fg="red", font=('Arial',10,'bold'))
                b.grid(row=2, column=2)



        # Menu functions
        def save_list():
            #define a patch for the pickle file on your disk
            pick_path = 'lst.pkl'

            #convert the dictionary to pickle
            with open (pick_path, 'wb') as pick:
                pickle.dump(lst, pick)
        

        def open_list():
            pass

        #-------------------------------|Widgets|-------------------------------
        # Add order widgets
        instructions = Label(add_order, text="Please add oder details below")
        instructions.grid(row=0, column=0, columnspan=2)

        Client = StringVar()
        Client.set("Client")
        client_entry = Entry(add_order, textvariable=Client, width=40)
        client_entry.grid(row=1, column=1)

        Address = StringVar()
        Address.set("Address")
        address_entry = Entry(add_order, textvariable=Address, width=40)
        address_entry.grid(row=1, column=2)

        TotalCost = StringVar()
        TotalCost.set("Total Cost")
        totalcost_entry = Entry(add_order, textvariable=TotalCost, width=10)
        totalcost_entry.grid(row=1, column=3)

        TotalRRP = StringVar()
        TotalRRP.set("Total RRP")
        totalrrp_entry = Entry(add_order, textvariable=TotalRRP, width=10)
        totalrrp_entry.grid(row=1, column=4)

        DoI = StringVar()
        DoI.set("DoI")
        doi_entry = Entry(add_order, textvariable=DoI, width=10)
        doi_entry.grid(row=1, column=5)

        DateDue = StringVar()
        DateDue.set("Date Due")
        datedue_entry = Entry(add_order, textvariable=DateDue)
        datedue_entry.grid(row=1, column=6)

        status = StringVar()
        status.set("Status")
        status_entry = Entry(add_order, textvariable=status)
        status_entry.grid(row=1, column=7)

        Inv = StringVar()
        Inv.set("Enter in Inv.Num of order you want to delete")
        d = Entry(add_order, textvariable=Inv, width=40)
        d.grid(row=2, column=1)

        # Add & delete buttons
        add_button = Button(add_order, text="Add Order", activebackground="green", activeforeground="white", command=add)
        delete_button = Button(add_order, text="Delete Order", activebackground="red", activeforeground="white", command=delete_order)
        add_button.grid(row=1, column=0)
        delete_button.grid(row=2, column=0)

        # Create Menu
        my_menu = Menu(root)
        root.config(menu=my_menu)

        # Add items to the menu
        file_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=save_list) # Dropdown option
        #file_menu.add_command(label="open", command=open_list)


filepath = 'ClientPricelist2022_test.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(map(tuple, Reader)) # Converts into tuple

# List for orders
lst = [("Inv. Num", "Client", "Address", "Total Cost", "Total RRP", "DoI", "Date Due", "Status")] # List of Orders

#-------------------------------|Windows|-------------------------------
# Orders window
root = Tk()
root.title("Orders")
root.geometry("1750x750") # might change this later

t = Table(root, lst)

#---------------------------------|GUI|---------------------------------
# Login Canvas
login_canvas = Canvas(root)

# Main Canvas
main_canvas = Canvas(root)

#-------------------------------|Mainloop|------------------------------
root.mainloop()
