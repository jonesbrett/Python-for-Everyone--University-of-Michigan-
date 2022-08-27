import sqlite3
import pandas

connection = sqlite3.connect("sp500.sqlite")
curs = connection.cursor()

# Run create table sql query
curs.execute(
    """CREATE TABLE IF NOT EXISTS TradeData (id INTEGER, date text, open INTEGER, high INTEGER, low INTEGER, close INTEGER, volume INTEGER, adj_close INTEGER)"""
)

# Load CSV into Pandas DataFrame
data = pandas.read_csv("sp500.csv")

# Write data to SQLite db table
data.to_sql("TradeData", connection, if_exists="replace", index=False)

prompt = input("Would you like to view the table: yes or no? ")
if prompt == "yes":
    curs.execute("select * from TradeData")
    trades = curs.fetchall()
    for row in trades:
        print(row)

print("closing connection")
connection.close()
