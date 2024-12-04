"""
This lab will explore establishing a database connection via Python and SQLite,
as well as creating a table, inserting data, and selecting that data.
"""
import sqlite3


conn = sqlite3.connect(":memory:")
cursor = conn.cursor()


# Create a dogs table with autoincrementing ID
def create_dogs_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            breed TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()

   


# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(name, breed, age):
    cursor.execute("""
        INSERT INTO dogs (name, breed, age)
        VALUES (?, ?, ?)
    """, (name, breed, age))
    conn.commit()

    
    


# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table *and returning them*.
def select_all_dogs():
    cursor.execute("""
        SELECT * FROM dogs
    """)
    rows = cursor.fetchall()

    # return the rows
    return rows
