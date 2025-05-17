
#!/usr/bin/python3
from seed import connect_to_prodev

def stream_user_ages():
    """Generator function to yield user ages one by one."""
    conn_prodev = connect_to_prodev()
    if conn_prodev:
        cursor = conn_prodev.cursor()
        cursor.execute("SELECT age FROM user_data")
        for row in cursor:
            yield row[0]
        cursor.close()
        conn_prodev.close()

def calculate_average_age():
    """Calculate the average age using the generator."""
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    return total_age / count if count > 0 else 0

if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")