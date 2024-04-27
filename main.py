import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import requests

# Function to fetch data from API
def fetch_data():
    url = "YOUR_API_ENDPOINT"
    response = requests.get(url)
    data = response.json()
    return data

# Fetch data from API
data = fetch_data()

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Data Table"),
    dash_table.DataTable(
        id='datatable',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'scroll'},
        style_cell={
            'minWidth': '0px', 'maxWidth': '180px',
            'whiteSpace': 'normal'
        },
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_size=10,
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)