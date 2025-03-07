import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

# Create a table for storing notes
cursor.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)''')

# Function to add a note
def add_note(content):
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()

# Function to view notes
def view_notes():
    cursor.execute("SELECT * FROM notes")
    for row in cursor.fetchall():
        print(row)

# Add a sample note
add_note("This is my first note!")

# Display all notes
view_notes()

# Close the connection
conn.close()
