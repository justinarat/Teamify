import os
import sys
import sqlite3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app, db


def create_tables():
    with app.app_context():
        db.create_all()
        print("All tables created.")


def create_database(database_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(database_path), exist_ok=True)

    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)

    # Close the connection
    conn.close()

    print(f"Database created at {os.path.abspath(database_path)}")


if __name__ == "__main__":
    create_tables()
