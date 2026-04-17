import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

DATA_PATH = "./formatted_data.csv"

df = pd.read_csv(DATA_PATH)
df = df.sort_values("date")

fig = px.line(df, x="date", y="sales")
fig.update_layout(xaxis_title="Date", yaxis_title="Sales ($)")

dash_app = Dash(__name__)

dash_app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", id="header"),
    dcc.Graph(id="visualization", figure=fig),
])

if __name__ == "__main__":
    dash_app.run_server()
