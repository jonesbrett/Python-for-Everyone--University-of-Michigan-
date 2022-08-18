# Instructions

# If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

# Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

# CREATE TABLE Ages (
#  name VARCHAR(128),
#  age INTEGER
# )

# Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows
# and only these rows with the following commands:

# DELETE FROM Ages;
# INSERT INTO Ages (name, age) VALUES ('Conli', 14);
# INSERT INTO Ages (name, age) VALUES ('Danielle', 33);
# INSERT INTO Ages (name, age) VALUES ('Aarron', 21);
# INSERT INTO Ages (name, age) VALUES ('Nicodemus', 20);
# INSERT INTO Ages (name, age) VALUES ('Myrna', 37);

# Once the inserts are done, run the following SQL command:

# SELECT hex(name || age) AS X FROM Ages ORDER BY X

# Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.

# Note: This assignment must be done using SQLite - in particular, the SELECT query above will not work in
# any other database. So you cannot use MySQL or Oracle for this assignment.

import sqlite3

conn = sqlite3.connect("Assignment 15.2.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute(
    """
CREATE TABLE Counts (org TEXT, count INTEGER)"""
)

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split("@")[1]
    cur.execute("SELECT count FROM Counts WHERE org = ? ", (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute(
            """INSERT INTO Counts (org, count)
                VALUES (?, 1)""",
            (domain,),
        )
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (domain,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
