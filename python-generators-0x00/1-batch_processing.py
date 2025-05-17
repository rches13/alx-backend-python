def stream_users_in_batches(batch_size):
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
                if not batch:
                    break
                yield batch
    except Error as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered_batch = [user for user in batch if user['age'] > 25]
        if filtered_batch:
            yield filtered_batch