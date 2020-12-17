import tkinter as tk
from tkinter import filedialog 

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

name_customer = tk.StringVar()
vat_customer = tk.StringVar()
contact_customer = tk.StringVar()
street_customer = tk.StringVar()
city_customer = tk.StringVar()
province_customer = tk.StringVar()

#Customer Details

customer_name = tk.Entry(master, textvariable= name_customer).grid(row=0, column=3)
vat_num2 = tk.Entry(master, textvariable= vat_customer).grid(row=1, column=3)
contact_num2 = tk.Entry(master, textvariable= contact_customer).grid(row=2, column=3)
street_add2 = tk.Entry(master, textvariable= street_customer).grid(row=3, column=3)
city2 = tk.Entry(master, textvariable= city_customer).grid(row=4, column=3)
province2 = tk.Entry(master, textvariable= province_customer).grid(row=5, column=3)


#String Variables Product Names

product1 = tk.StringVar()
product2 = tk.StringVar()
product3 = tk.StringVar()
product4 = tk.StringVar()
product5 = tk.StringVar()
product6 = tk.StringVar()
product7 = tk.StringVar()
product8 = tk.StringVar()
product9 = tk.StringVar()
product10 = tk.StringVar()
product11 = tk.StringVar()


#Product Names

tk.Entry(master, textvariable= product1).grid(row=8, column=1)
tk.Entry(master, textvariable= product2).grid(row=9, column=1)
tk.Entry(master, textvariable= product3).grid(row=10, column=1)
tk.Entry(master, textvariable= product4).grid(row=11, column=1)
tk.Entry(master, textvariable= product5).grid(row=12, column=1)
tk.Entry(master, textvariable= product6).grid(row=13, column=1)
tk.Entry(master, textvariable= product7).grid(row=14, column=1)
tk.Entry(master, textvariable= product8).grid(row=15, column=1)
tk.Entry(master, textvariable= product9).grid(row=16, column=1)
tk.Entry(master, textvariable= product10).grid(row=17, column=1)
tk.Entry(master, textvariable= product11).grid(row=18, column=1)

#String Variables Product Prices

prices1 = tk.StringVar()
prices2 = tk.StringVar()
prices3 = tk.StringVar()
prices4 = tk.StringVar()
prices5 = tk.StringVar()
prices6 = tk.StringVar()
prices7 = tk.StringVar()
prices8 = tk.StringVar()
prices9 = tk.StringVar()
prices10 = tk.StringVar()
prices11 = tk.StringVar()

#Product Prices

tk.Entry(master, textvariable= prices1).grid(row=8, column=2)
tk.Entry(master, textvariable= prices2).grid(row=9, column=2)
tk.Entry(master, textvariable= prices3).grid(row=10, column=2)
tk.Entry(master, textvariable= prices4).grid(row=11, column=2)
tk.Entry(master, textvariable= prices5).grid(row=12, column=2)
tk.Entry(master, textvariable= prices6).grid(row=13, column=2)
tk.Entry(master, textvariable= prices7).grid(row=14, column=2)
tk.Entry(master, textvariable= prices8).grid(row=15, column=2)
tk.Entry(master, textvariable= prices9).grid(row=16, column=2)
tk.Entry(master, textvariable= prices10).grid(row=17, column=2)
tk.Entry(master, textvariable= prices11).grid(row=18, column=2)

#String Variables Product quantity

quantity1 = tk.StringVar()
quantity2 = tk.StringVar()
quantity3 = tk.StringVar()
quantity4 = tk.StringVar()
quantity5 = tk.StringVar()
quantity6 = tk.StringVar()
quantity7 = tk.StringVar()
quantity8 = tk.StringVar()
quantity9 = tk.StringVar()
quantity10 = tk.StringVar()
quantity11 = tk.StringVar()
    
#Quantity

tk.Entry(master, textvariable= quantity1).grid(row=8, column=3)
tk.Entry(master, textvariable= quantity2).grid(row=9, column=3)
tk.Entry(master, textvariable= quantity3).grid(row=10, column=3)
tk.Entry(master, textvariable= quantity4).grid(row=11, column=3)
tk.Entry(master, textvariable= quantity5).grid(row=12, column=3)
tk.Entry(master, textvariable= quantity6).grid(row=13, column=3)
tk.Entry(master, textvariable= quantity7).grid(row=14, column=3)
tk.Entry(master, textvariable= quantity8).grid(row=15, column=3)
tk.Entry(master, textvariable= quantity9).grid(row=16, column=3)
tk.Entry(master, textvariable= quantity10).grid(row=17, column=3)
tk.Entry(master, textvariable= quantity11).grid(row=18, column=3)

#String Variables Product VAT

VAT1 = tk.StringVar()
VAT2 = tk.StringVar()
VAT3 = tk.StringVar()
VAT4 = tk.StringVar()
VAT5 = tk.StringVar()
VAT6 = tk.StringVar()
VAT7 = tk.StringVar()
VAT8 = tk.StringVar()
VAT9 = tk.StringVar()
VAT10 = tk.StringVar()
VAT11 = tk.StringVar()

#VAT

tk.Entry(master, textvariable= VAT1).grid(row=8, column=4)
tk.Entry(master, textvariable= VAT2).grid(row=9, column=4)
tk.Entry(master, textvariable= VAT3).grid(row=10, column=4)
tk.Entry(master, textvariable= VAT4).grid(row=11, column=4)
tk.Entry(master, textvariable= VAT5).grid(row=12, column=4)
tk.Entry(master, textvariable= VAT6).grid(row=13, column=4)
tk.Entry(master, textvariable= VAT7).grid(row=14, column=4)
tk.Entry(master, textvariable= VAT8).grid(row=15, column=4)
tk.Entry(master, textvariable= VAT9).grid(row=16, column=4)
tk.Entry(master, textvariable= VAT10).grid(row=17, column=4)
tk.Entry(master, textvariable= VAT11).grid(row=18, column=4)

#String Variables Product Totals

Totals1 = tk.StringVar()
Totals2 = tk.StringVar()
Totals3 = tk.StringVar()
Totals4 = tk.StringVar()
Totals5 = tk.StringVar()
Totals6 = tk.StringVar()
Totals7 = tk.StringVar()
Totals8 = tk.StringVar()
Totals9 = tk.StringVar()
Totals10 = tk.StringVar()
Totals11 = tk.StringVar()

#Totals

tk.Entry(master, textvariable= Totals1).grid(row=8, column=5)
tk.Entry(master, textvariable= Totals2).grid(row=9, column=5)
tk.Entry(master, textvariable= Totals3).grid(row=10, column=5)
tk.Entry(master, textvariable= Totals4).grid(row=11, column=5)
tk.Entry(master, textvariable= Totals5).grid(row=12, column=5)
tk.Entry(master, textvariable= Totals6).grid(row=13, column=5)
tk.Entry(master, textvariable= Totals7).grid(row=14, column=5)
tk.Entry(master, textvariable= Totals8).grid(row=15, column=5)
tk.Entry(master, textvariable= Totals9).grid(row=16, column=5)
tk.Entry(master, textvariable= Totals10).grid(row=17, column=5)
tk.Entry(master, textvariable= Totals11).grid(row=18, column=5)

#Sums

sum_price = tk.Entry(master).grid(row=20, column=2)
sum_vat = tk.Entry(master).grid(row=20, column=4)
sum_total = tk.Entry(master).grid(row=20, column=5)


button = tk.Button(master, 
                    text="Browse Files", 
                    fg="black",
                    command=browseFiles)
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

master.mainloop()