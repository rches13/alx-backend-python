Python Generators - 0x00
Overview
This project demonstrates the use of Python generators to stream data from a MySQL database. The script seed.py sets up a MySQL database ALX_prodev, creates a table user_data, populates it with data from a CSV file, and provides a generator to stream the table's rows one by one.
Repository

GitHub Repository: alx-backend-python
Directory: python-generators-0x00
Files: seed.py, 0-main.py, user_data.csv, README.md

Requirements

Python 3.8+
MySQL Server
mysql-connector-python package (pip install mysql-connector-python)
A CSV file named user_data.csv with columns: name, email, age

Setup

Install the required package:pip install mysql-connector-python


Update the MySQL credentials in seed.py (replace your_username and your_password).
Ensure user_data.csv is in the project directory with the format:name,email,age
John Doe,john@example.com,30
Jane Smith,jane@example.com,25
...



Usage
Run the main script to set up the database and test the setup:
chmod +x 0-main.py
./0-main.py

To use the generator:
from seed import connect_to_prodev, stream_user_data

connection = connect_to_prodev()
if connection:
    for row in stream_user_data(connection):
        print(row)
    connection.close()

Files

seed.py: Contains functions to connect to MySQL, create the database and table, insert data, and a generator to stream data.
0-main.py: Tests the database setup and data insertion.
user_data.csv: Sample data file.
README.md: Project documentation.

Expected Output
Running ./0-main.py should produce output similar to:
connection successful
Database ALX_prodev created successfully or already exists
Table user_data created successfully
Data inserted successfully
Database ALX_prodev is present
[('UUID1', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67.0), ...]

Notes

Ensure MySQL server is running and accessible.
The generator stream_user_data is memory-efficient, yielding one row at a time.
Replace placeholders in seed.py with your MySQL credentials.
UUIDs are generated for user_id, so actual UUIDs will differ.

Author
Faith Okoth
