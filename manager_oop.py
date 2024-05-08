
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from data import Database

# Instanciate database object
db = Database('ShoppingCart.db')

# Main Application/GUI class
class Application(tk.Frame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        app.title('Product Manager Application')
        # Width height
        app.geometry("610x440")
        # Create widgets/grid
        self.app_widgets()
        # Init selected item var
        self.selected_item = 0
        # Population initial list
        self.display_list()
        # self.parts_list.delete(8, tk.END)

    def app_widgets(self):
        # Product
        self.product_text = tk.StringVar()
        self.product_label = tk.Label(
            self.app, text='Product Name', 
            font=('bold', 15), pady=20)
        self.product_label.grid(row=0, column=0, sticky=tk.W)
        self.product_entry = tk.Entry(self.app, textvariable=self.product_text)
        self.product_entry.grid(row=0, column=1)
        
        #Customer
        self.customer_text = tk.StringVar()
        self.customer_label = tk.Label(
            self.app, text='Customer', 
            font=('bold', 15))
        self.customer_label.grid(row=0, column=2, sticky=tk.W)
        self.customer_entry = tk.Entry(
            self.app, textvariable=self.customer_text)
        self.customer_entry.grid(row=0, column=3)
        
        #Retailer
        self.retailer_text = tk.StringVar()
        self.retailer_label = tk.Label(
            self.app, text='Retailer', 
            font=('bold', 15))
        self.retailer_label.grid(row=1, column=0, sticky=tk.W)
        self.retailer_entry = tk.Entry(
            self.app, textvariable=self.retailer_text)
        self.retailer_entry.grid(row=1, column=1)
        
        #Price
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.app, text='Price', 
            font=('bold', 15))
        self.price_label.grid(row=1, column=2, sticky=tk.W)
        self.price_entry = tk.Entry(self.app, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=3)
        
        #Buttons
        self.add_btn = tk.Button(
            self.app, text="Add Part", width=12, command=self.add_item)
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(
            self.app, text="Remove Part", width=12, command=self.remove_text)
        self.remove_btn.grid(row=2, column=1)

        self.update_btn = tk.Button(
            self.app, text="Update Part", width=12, command=self.update_data)
        self.update_btn.grid(row=2, column=2)

        self.clear_btn = tk.Button(
            self.app, text="Clear Input", width=12, command=self.clear_list)
        self.clear_btn.grid(row=2, column=3)

        #list (listbox)
        self.shop_cart = tk.Listbox(self.app, height=10, width=60, border=1)
        self.shop_cart.grid(row=3, column=0, columnspan=3,
                             rowspan=6, pady=20, padx=20)
        
        # Create scrollbar to GUI App
        self.scroll_bar = tk.Scrollbar(self.app)
        self.scroll_bar.grid(row=3, column=3, sticky=tk.N+tk.S)
        
        # Set scrollbar
        self.shop_cart.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.configure(command=self.shop_cart.yview)

        # Bind select
        self.shop_cart.bind('<<ListboxSelect>>', self.select_data)


    def display_list(self):
        # Delete items before update
        self.shop_cart.delete(0, tk.END)
        # Loop 
        for row in db.fetch():
            # Insert into list
            self.shop_cart.insert(tk.END, row)
    
    #Execute when item is select
    def select_data(self, event):
        
        try:
            #Get index List
            index = self.shop_cart.curselection()[0]
            #Get select item
            self.select_item = self.shop_cart.get(index)

            # Add text to entries
            self.product_entry.delete(0, tk.END)
            self.product_entry.insert(tk.END, self.select_item[1])
            self.customer_entry.delete(0, tk.END)
            self.customer_entry.insert(tk.END, self.select_item[2])
            self.retailer_entry.delete(0, tk.END)
            self.retailer_entry.insert(tk.END, self.select_item[3])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(tk.END, self.select_item[4])
            
        except IndexError:
            pass
        
    # Add List item
    def add_item(self):
        if self.product_text.get() == '' or self.customer_text.get() == '' or self.retailer_text.get() == '' or self.price_text.get() == '':
            messagebox.showerror(
                "Input Error", "Please include all fields")
            return
        
        # Insert into Data
        db.insert(self.product_text.get(), self.customer_text.get(),
                  self.retailer_text.get(), self.price_text.get())
        # Clear list
        self.shop_cart.delete(0, tk.END)
        # Insert into listbox
        self.shop_cart.insert(tk.END, (self.product_text.get(), self.customer_text.get(
        ), self.retailer_text.get(), self.price_text.get()))
        self.clear_list()
        self.display_list()

    # Remove List Item
    def remove_text(self):
        db.remove(self.select_item[0])
        self.clear_list()
        self.display_list()

    # Update List item
    def update_data(self):
        db.update(self.select_item[0], self.product_text.get(
        ), self.customer_text.get(), self.retailer_text.get(), self.price_text.get())
        self.display_list()

    # Clear all Input fields
    def clear_list(self):
        self.product_entry.delete(0, tk.END)
        self.customer_entry.delete(0, tk.END)
        self.retailer_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)


root = tk.Tk()
window = Application(app=root)
window.mainloop()
