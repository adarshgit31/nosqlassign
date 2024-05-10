import sqlite3
import random
from datetime import datetime, timedelta

# Create a SQLite connection and cursor
conn = sqlite3.connect('trainDatabase.db')  # Use 'trainDatabase.db' as the SQLite database
cursor = conn.cursor()

# Create a trains table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trains (
        id INTEGER PRIMARY KEY,
        train_number TEXT,
        origin TEXT,
        destination TEXT,
        departure_date TEXT,
        zone TEXT
    )
''')


# Function to generate random train data
def generate_train_data(num_records):
    trains_data = []
    cities = ['Bangalore', 'New Delhi', 'Patna', 'Lucknow', 'Mumbai', 'DehraDun', 'Kolkata']
    zones={'Bangalore':"SWR", 'New Delhi':"NR", 'Patna':"ECR", 'Lucknow':"NCR", 'Mumbai':"CR", 'DehraDun':"NR", 'Kolkata':"ER"}
    for _ in range(num_records):
        train_number = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + str(random.randint(100, 999))
        origin = random.choice(cities)
        destination = random.choice(cities)
        while destination == origin:
            destination = random.choice(cities)

        departure_date = datetime.now() + timedelta(days=random.randint(1, 30))
        zone=zones.get(origin)
        
        trains_data.append((train_number, origin, destination, departure_date.strftime('%Y-%m-%d %H:%M:%S'),
                             zone))

    return trains_data


# Generate train data (200 records)
trains_data = generate_train_data(200)

# Insert generated data into the trains table
cursor.executemany('''
    INSERT INTO trains (train_number, origin, destination, departure_date, zone)
    VALUES (?, ?, ?, ?, ?)
''', trains_data)

# Commit changes and close connection
conn.commit()
conn.close()
