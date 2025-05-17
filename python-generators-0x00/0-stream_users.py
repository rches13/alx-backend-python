
#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def stream_users():
    """Generator function to stream rows from user_data table one by one."""
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="chess",  # Replace with your MySQL username
            password="ronaldo",  # Replace with your MySQL password
            database="ALX_prodev"
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # Return rows as dictionaries
            cursor.execute("SELECT user_id, name, email, age FROM user_data;")
            for row in cursor:
                yield row
    except Error as e:
        print(f"Error streaming data: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
