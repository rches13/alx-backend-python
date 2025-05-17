
#!/usr/bin/python3
from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """Generator function to stream rows from user_data table in batches."""
    conn_prodev = connect_to_prodev()
    if not conn_prodev:
        return
    cursor = conn_prodev.cursor(dictionary=True)
    offset = 0
    while True:
        query = "SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (batch_size, offset))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            conn_prodev.close()
            return
        for row in rows:
            yield row
        offset += batch_size

def batch_processing(batch_size):
    """Generator function to yield users over age 25."""
    for row in stream_users_in_batches(batch_size):
        if row['age'] > 25:
            yield row