import plotly.graph_objects as go
import pandas as pd
import sqlite3

connection = sqlite3.connect("sp500.sqlite")
cur = connection.cursor()

trades = pd.read_sql_query("SELECT * from TradeData", connection)

fig = go.Figure(
    data=[
        go.Candlestick(
            x=trades["date"],
            open=trades["open"],
            high=trades["high"],
            low=trades["low"],
            close=trades["close"],
        )
    ]
)

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()
connection.close()
