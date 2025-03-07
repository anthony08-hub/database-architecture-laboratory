import mysql.connector

# Connect to MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="09633183975anthony08-",  
    database="note_db"
)

cursor = db.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS notes (id INT AUTO_INCREMENT PRIMARY KEY, content VARCHAR(255))''')

# Function to add a note
def add_note(content):
    cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
    db.commit()

# Function to view notes
def view_notes():
    cursor.execute("SELECT * FROM notes")
    for row in cursor.fetchall():
        print(row)

# Add a sample note
add_note("This is my second note!")

# View all notes
view_notes()

# Close the connection
db.close()
