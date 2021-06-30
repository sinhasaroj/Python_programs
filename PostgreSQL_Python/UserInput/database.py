import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE enteries (content TEXT , date TEXT);")

def add_entry(entry_content,entry_date):
    enteries.append({"content": entry_content,"date": entry_date})


def get_entry():
    return enteries
