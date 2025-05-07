import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_name TEXT PRIMARY KEY,
    password TEXT,
    score REAL
)
''')

# Data to insert
students = [
    ("salma", "123", 5),
    ("ahmed_moh", "123", 2),
    ("mohamed_ayman", "123", 5),
    ("marvel", "123", 10),
    ("abdelrahman_tamem", "123", 5),
    ("yousuf_waleed", "123", 4),
    ("menna", "123", 5),
    ("mahmoud_elhewala", "123", 8),
    ("Rawda", "123", 8),
    ("mohamed_medhat", "123", 9),
    ("mahmoud_sakr", "123", 9.5),
    ("abdelrahman_khaled", "123", 10),
    ("youssef_waleed", "123", 9),
    ("mohamed_sal", "123", 2),
    ("Ali_tamer", "123", 5),
]

# Insert data
cursor.executemany('INSERT OR REPLACE INTO students VALUES (?, ?, ?)', students)

# Commit and close
conn.commit()
conn.close()

print("Database and table created, and data inserted successfully.")
