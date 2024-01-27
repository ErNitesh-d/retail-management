import tkinter as tk
import sqlite3

def create_bill_table(cursor):
    table = []
    headers = ["Item", "Quantity", "Price"]
    table.append(headers)
    cursor.execute("SELECT name, quantity, price FROM bill")
    for row in cursor.fetchall():
        table.append(row)
    return table

def save_bill_to_file(table, file_name):
    with open(file_name, 'w') as file:
        for row in table:
            line = " ".join([str(cell) for cell in row])
            file.write(line + '\n')

def save_bill():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    bill_table = create_bill_table(cursor)
    save_bill_to_file(bill_table, 'bill.txt')
    cursor.close()
    conn.close()

root = tk.Tk()
save_button = tk.Button(root, text="Save Bill", command=save_bill)
save_button.pack()

root.mainloop()
