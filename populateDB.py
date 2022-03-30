import csv
import sqlite3

def initDB():
    connection = sqlite3.connect('Project/quotes.db')
    cursor = connection.cursor()
    cursor.execute('''DROP TABLE IF EXISTS Quotes''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Quotes
                  (id INTEGER, quote TEXT, emotion TEXT, used BOOLEAN)''')

    connection.commit()
    connection.close()

def populateDB(filenamecsv):
    connection = sqlite3.connect('Project/quotes.db')
    cursor = connection.cursor()

    file = open(filenamecsv)
    csvreader = csv.reader(file, delimiter=";")
    for row in csvreader:
        query = '''INSERT INTO Quotes(id, quote, emotion, used) VALUES (?, ?, ?, ?)'''
        cursor.execute(query, (row[0], row[1], row[2], row[3]));
    connection.commit()
    connection.close()

initDB()
populateDB("quotes.csv");
print("Done")
