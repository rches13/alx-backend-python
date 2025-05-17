
#!/usr/bin/python3
from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """Fetch a page of users from user_data with given page_size and offset."""
    conn_prodev = connect_to_prodev()
    if conn_prodev:
        cursor = conn_prodev.cursor(dictionary=True)
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        rows = cursor.fetchall()
        cursor.close()
        conn_prodev.close()
        return rows
    return []

def lazy_paginate(page_size):
    """Generator function to lazily load pages of users."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        for row in page:
            yield row
        offset += page_size