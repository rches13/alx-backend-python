
#!/usr/bin/python3
from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """Generator function to stream rows from user_data table in batches."""
    conn_prodev = connect_to_prodev()
    if conn_prodev:
        cursor = conn_prodev.cursor(dictionary=True)
        offset = 0
        while True:
            query = "SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s"
            cursor.execute(query, (batch_size, offset))
            rows = cursor.fetchall()
            if not rows:
                break
            yield rows
            offset += batch_size
        cursor.close()
        conn_prodev.close()

def batch_processing(batch_size):
    """Generator function to filter users over age 25 from batches."""
    for batch in stream_users_in_batches(batch_size):
        filtered_batch = [row for row in batch if row['age'] > 25]
        if filtered_batch:
            yield filtered_batch