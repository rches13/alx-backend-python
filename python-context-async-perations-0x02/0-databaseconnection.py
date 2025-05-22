#!/usr/bin/env python3
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        # Open the database connection
        self.conn = sqlite3.connect(self.db_name)
        return self.conn  # This will be assigned to the "as" variable in with statement

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the database connection
        if self.conn:
            self.conn.close()
        # Do not suppress exceptions, so return False
        return False

# Usage of the context manager
if __name__ == "__main__":
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print(results)
