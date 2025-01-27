import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('trainDatabase.db')
cursor = conn.cursor()

# Query and fetch all data from the flights table
cursor.execute('SELECT * FROM trains')
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close connection
conn.close()
