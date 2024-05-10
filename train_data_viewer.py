import tkinter as tk
import sqlite3
import pymongo

def fetch_sqlite_trains():
    # Connect to SQLite database
    conn = sqlite3.connect('trainDatabase.db')
    cursor = conn.cursor()

    # Query and fetch all data from the trains table
    cursor.execute('SELECT * FROM trains')
    rows = cursor.fetchall()

    # Close connection
    conn.close()

    return rows

def fetch_mongodb_trains():
    # Connect to MongoDB (assuming it's running on localhost)
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['trainDatabase']
    collection = db['trains']

    # Retrieve all documents (train data) from MongoDB collection
    trains_data = list(collection.find())

    # Close MongoDB connection
    client.close()

    return trains_data

def display_trains():
    # Fetch trains data from SQLite
    sqlite_trains = fetch_sqlite_trains()

    # Fetch trains data from MongoDB
    mongodb_trains = fetch_mongodb_trains()

    # Create GUI window
    root = tk.Tk()
    root.title("train Data Viewer, 1CR20CS008")

    # Create a text widget for SQLite train data (comma-separated values)
    sqlite_text_widget = tk.Text(root, height=15, width=80)
    sqlite_text_widget.pack(padx=20, pady=10)

    # Insert SQLite train data into the text widget as comma-separated values
    sqlite_text_widget.insert(tk.END, "SQLite train Data:\n\n")
    for train in sqlite_trains:
        train_info = ", ".join(str(field) for field in train) + "\n"
        sqlite_text_widget.insert(tk.END, train_info)

    # Create a text widget for MongoDB train data (key-value pairs)
    mongodb_text_widget = tk.Text(root, height=15, width=80)
    mongodb_text_widget.pack(padx=20, pady=10)

    # Insert MongoDB train data into the text widget as key-value pairs
    mongodb_text_widget.insert(tk.END, "MongoDB train Data (Key-Value Pairs):\n\n")
    for train in mongodb_trains:
        train_info = f"train Number: {train['train_number']}\nOrigin: {train['origin']}\nDestination: {train['destination']}\nDeparture Date: {train['departure_date']}\nZone: {train['zone']}\n\n"
        mongodb_text_widget.insert(tk.END, train_info)

    # Run the GUI main loop
    root.mainloop()

# Call the display_trains function to show SQLite and MongoDB train data in the GUI
display_trains()
