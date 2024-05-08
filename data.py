import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, product text, customer text, retailer text, price text)")
        self.conn.commit()

    #INSERT (ALTER) all the data in the database table
    def insert(self, product, customer, retailer, price):
        self.cur.execute("INSERT INTO products VALUES (NULL, ?, ?,?, ?)",
                         (product, customer, retailer, price))
        self.conn.commit()
        
    # To show all data in the Database
    def fetch(self):
        self.cur.execute("SELECT * FROM products")
        rows = self.cur.fetchall()
        return rows

    #Delete a row from the database table
    def remove(self, id):
        self.cur.execute("DELETE FROM products WHERE id=?", (id,))
        self.conn.commit()

    #To update a row in the database table
    def update(self, id, product, customer, retailer, price):
        self.cur.execute("UPDATE products SET product = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (product, customer, retailer, price, id))
        self.conn.commit()

    #To Delete a row from the Database table
    def __del__(self):
        self.conn.close()

# Database Table Written  
db = Database("ShoppingCart.db")
db.insert("Macbook Air M2","Karan Parmar","Apple Store","$1698")
db.insert("OnePlus 10T","Hirein Makwana","FlipKart","$679")
db.insert("Apple watch Ultra 2","Shaswat Shukla","Unicorn","$1011")
db.insert("Samsung Galaxy S24","Rohan Darji","Amazon","$1493")
db.insert("Canon EOS 90D DSLR","Dhruv Parmar","Tech Electronics","$1357")
db.insert("Nvidia RTX 3090","Jash Patel","Best Buy","$871")
db.insert("ASUS ROG Strix G16","Jash Patel","Vijay sales","$999")
db.insert("Galaxy Watch6 Classic","Jack Allison","Helios Watch Store","$597")
