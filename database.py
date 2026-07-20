import sqlite3

def get_connection():
    connection = sqlite3.connect("finance.db")
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    with open("schema.sql") as s:
        contents = s.read()
    
    connection.executescript(contents)

    connection.close()

def add_transaction(description, amount, date, category):
    connection = get_connection()

    connection.execute("INSERT INTO transactions (description, amount, date, category) VALUES (?, ?, ?, ?)",
                        (description, amount, date, category))

    connection.commit()

    connection.close()
