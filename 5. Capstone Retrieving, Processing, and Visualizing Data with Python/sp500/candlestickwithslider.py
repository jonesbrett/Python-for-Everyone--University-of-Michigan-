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

fig.update_layout(title="SP500", yaxis_title="Stock Price")

fig.update_layout(xaxis_rangeslider_visible=True)
fig.show()
connection.close()
