Database Architecture Laboratory

Summary of the Activity:
This project involves creating three types of database architectures: **Single-Tier**, **Two-Tier**, and **Three-Tier**. Each architecture interacts with a database, starting with SQLite and then moving to MySQL. The goal is to demonstrate how database systems can be integrated with different application layers and how to access, store, and retrieve data.

**Key Features:**
- Single-Tier Architecture: Uses SQLite for a lightweight database system embedded in the Python application.
- Two-Tier Architecture: Uses MySQL as the database with Python as the client for interaction.
- Three-Tier Architecture: Implements a web-based application using Flask with MySQL for the backend and HTML/CSS for the frontend.

## **Instructions for Running or Testing the Code:**
Setting up the Project
1. **Install the required software:**
   - [Visual Studio Code](https://code.visualstudio.com/)
   - [Python](https://www.python.org/downloads/)
   - [MySQL](https://dev.mysql.com/downloads/installer/)
   - [Git](https://git-scm.com/downloads)

2. **Install the required Python libraries** by running the following command:
   pip install flask mysql-connector sqlite3

Running the Architectures

#### **Single-Tier Architecture (SQLite and Python)**
1. Navigate to the `single_tier.py` script.
2. Run the Python script:
 python single_tier.py
   

#### **Two-Tier Architecture (MySQL and Python)**
1. Ensure MySQL is installed and running on your machine.
2. Create the `notes_db` database and `notes` table in MySQL using the following SQL commands:
  
   CREATE DATABASE notes_db;
   USE notes_db;
   CREATE TABLE notes (id INT AUTO_INCREMENT PRIMARY KEY, content VARCHAR(255));
  
3. Navigate to the `two_tier.py` script.
4. Run the Python script:
 
   python two_tier.py
 

#### **Three-Tier Architecture (Flask, MySQL, and HTML/CSS)**
1. Ensure MySQL is running and the database and table are set up.
2. Navigate to the `app.py` script and run the Flask application:
   
   python app.py
  
3. Open a browser and go to `http://127.0.0.1:5000/` to see your web application.
4. **Expected Webpage:**
   - A form to add new notes.
   - A list of existing notes fetched from the database.

Relevant Details

- Technologies Used:
  - SQLite for the Single-Tier architecture.
  - MySQL for the Two-Tier and Three-Tier architectures.
  - Flask for the web application in the Three-Tier architecture.
  - HTML/CSS for the frontend.

- Project Goals:
  - Learn and implement database interaction in different architectures.
  - Gain practical experience in connecting databases with Python applications.
  - Understand how web applications interact with databases in a three-tier architecture.

- Additional Notes:
  - The Flask web application uses MySQL as the backend to store and manage data.
  - The frontend displays a form to allow users to add new notes, which are saved in the database.
  - Each architecture is implemented with increasing complexity to demonstrate how databases are integrated in a real-world scenario.

