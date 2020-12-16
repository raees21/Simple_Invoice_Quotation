import tkinter as tk
from tkinter import filedialog 



product = []
name = []
qty = []
VAT = []
total = []
name = []

master = tk.Tk()
master.title("Simple Quotation Tool")


def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    label_file_explorer.configure(text="File Opened: "+filename) 


def write_to_txt():

    inputValue=bus_string.get()
    print(inputValue)
    
    with open("Raees.txt", "w+") as file:
        file.write(str(inputValue)) 

tk.Label(master, text="Business Name").grid(row=0)
tk.Label(master, text="VAT Number").grid(row=1)
tk.Label(master, text="Contact Person").grid(row=2)
tk.Label(master, text="Street Address").grid(row=3)
tk.Label(master, text="City").grid(row=4)
tk.Label(master, text="Province").grid(row=5)
tk.Label(master, text="Contact Number").grid(row=6)
tk.Label(master, text="").grid(row=7)
tk.Label(master, text="Product 1").grid(row=8)
tk.Label(master, text="Product 2").grid(row=9)
tk.Label(master, text="Product 3").grid(row=10)
tk.Label(master, text="Product 4").grid(row=11)
tk.Label(master, text="Product 5").grid(row=12)
tk.Label(master, text="Product 6").grid(row=13)
tk.Label(master, text="Product 7").grid(row=14)
tk.Label(master, text="Product 8").grid(row=15)
tk.Label(master, text="Product 9").grid(row=16)
tk.Label(master, text="Product 10").grid(row=17)
tk.Label(master, text="Product 11").grid(row=18)
tk.Label(master, text="").grid(row=19)
tk.Label(master, text="Totals").grid(row=20)
tk.Label(master, text="").grid(row=21)

tk.Label(master, text="Customer Name").grid(row=0, column=2)
tk.Label(master, text="VAT Number").grid(row=1, column=2)
tk.Label(master, text="Contact Number").grid(row=2, column=2)
tk.Label(master, text="Street Address").grid(row=3, column=2)
tk.Label(master, text="City").grid(row=4, column=2)
tk.Label(master, text="Province").grid(row=5, column=2)

tk.Label(master, text="Name").grid(row=7, column=1)
tk.Label(master, text="Price").grid(row=7, column=2)
tk.Label(master, text="Qty").grid(row=7, column=3)
tk.Label(master, text="VAT").grid(row=7, column=4)
tk.Label(master, text="Total").grid(row=7, column=5)


#String Variables Business Details

bus_string = tk.StringVar()
vat_string = tk.StringVar()
contact_string = tk.StringVar()
street_string = tk.StringVar()
city_string = tk.StringVar()
province_string = tk.StringVar()
contact_string = tk.StringVar()

#Business Details

business_name = tk.Entry(master, textvariable = bus_string).grid(row=0, column=1)
vat_num = tk.Entry(master, textvariable= vat_string).grid(row=1, column=1)
contact_person = tk.Entry(master, textvariable= contact_string).grid(row=2, column=1)
street_add = tk.Entry(master, textvariable= street_string).grid(row=3, column=1)
city = tk.Entry(master, textvariable= city_string).grid(row=4, column=1)
province = tk.Entry(master, textvariable= province_string).grid(row=5, column=1)
contact_num = tk.Entry(master, textvariable= contact_string).grid(row=6, column=1)

#String Variables Customer Details

bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()

#Customer Details

customer_name = tk.Entry(master).grid(row=0, column=3)
vat_num2 = tk.Entry(master).grid(row=1, column=3)
contact_num2 = tk.Entry(master).grid(row=2, column=3)
street_add2 = tk.Entry(master).grid(row=3, column=3)
city2 = tk.Entry(master).grid(row=4, column=3)
province2 = tk.Entry(master).grid(row=5, column=3)

#Product Names

tk.Entry(master).grid(row=8, column=1)
tk.Entry(master).grid(row=9, column=1)
tk.Entry(master).grid(row=10, column=1)
tk.Entry(master).grid(row=11, column=1)
tk.Entry(master).grid(row=12, column=1)
tk.Entry(master).grid(row=13, column=1)
tk.Entry(master).grid(row=14, column=1)
tk.Entry(master).grid(row=15, column=1)
tk.Entry(master).grid(row=16, column=1)
tk.Entry(master).grid(row=17, column=1)
tk.Entry(master).grid(row=18, column=1)

#Product Prices

tk.Entry(master).grid(row=8, column=2)
tk.Entry(master).grid(row=9, column=2)
tk.Entry(master).grid(row=10, column=2)
tk.Entry(master).grid(row=11, column=2)
tk.Entry(master).grid(row=12, column=2)
tk.Entry(master).grid(row=13, column=2)
tk.Entry(master).grid(row=14, column=2)
tk.Entry(master).grid(row=15, column=2)
tk.Entry(master).grid(row=16, column=2)
tk.Entry(master).grid(row=17, column=2)
tk.Entry(master).grid(row=18, column=2)
    
#Quantity

tk.Entry(master).grid(row=8, column=3)
tk.Entry(master).grid(row=9, column=3)
tk.Entry(master).grid(row=10, column=3)
tk.Entry(master).grid(row=11, column=3)
tk.Entry(master).grid(row=12, column=3)
tk.Entry(master).grid(row=13, column=3)
tk.Entry(master).grid(row=14, column=3)
tk.Entry(master).grid(row=15, column=3)
tk.Entry(master).grid(row=16, column=3)
tk.Entry(master).grid(row=17, column=3)
tk.Entry(master).grid(row=18, column=3)

#VAT

tk.Entry(master).grid(row=8, column=4)
tk.Entry(master).grid(row=9, column=4)
tk.Entry(master).grid(row=10, column=4)
tk.Entry(master).grid(row=11, column=4)
tk.Entry(master).grid(row=12, column=4)
tk.Entry(master).grid(row=13, column=4)
tk.Entry(master).grid(row=14, column=4)
tk.Entry(master).grid(row=15, column=4)
tk.Entry(master).grid(row=16, column=4)
tk.Entry(master).grid(row=17, column=4)
tk.Entry(master).grid(row=18, column=4)

#Totals

tk.Entry(master).grid(row=8, column=5)
tk.Entry(master).grid(row=9, column=5)
tk.Entry(master).grid(row=10, column=5)
tk.Entry(master).grid(row=11, column=5)
tk.Entry(master).grid(row=12, column=5)
tk.Entry(master).grid(row=13, column=5)
tk.Entry(master).grid(row=14, column=5)
tk.Entry(master).grid(row=15, column=5)
tk.Entry(master).grid(row=16, column=5)
tk.Entry(master).grid(row=17, column=5)
tk.Entry(master).grid(row=18, column=5)

#Sums

sum_price = tk.Entry(master).grid(row=20, column=2)
sum_vat = tk.Entry(master).grid(row=20, column=4)
sum_total = tk.Entry(master).grid(row=20, column=5)

#String Variables Product Names

bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()
bus_string = tk.StringVar()




button = tk.Button(master, 
                    text="Browse Files", 
                    fg="black",
                    command=browseFiles,)
button.grid(row=22, column=2)

button = tk.Button(master, 
                    text="Create Quote", 
                    fg="black",
                    command=lambda : write_to_txt())
button.grid(row=22, column=1)


button = tk.Button(master, 
                text="QUIT", 
                fg="red",
                command=quit)
button.grid(row=22, column=3)


print(name)

master.mainloop()