
#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def stream_users_in_batches(batch_size):
    """Generator function to stream rows from user_data table in batches."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="chess",  
            password="ronaldo",  
            database="ALX_prodev"
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT user_id, name, email, age FROM user_data;")
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:  # No more rows to fetch
                    break
                yield batch
    except Error as e:
        print(f"Error streaming data: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def batch_processing(batch_size):
    """Generator function to process batches and filter users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        filtered_batch = [user for user in batch if user['age'] > 25]
        if filtered_batch:  # Yield only if there are users over 25
            yield filtered_batch