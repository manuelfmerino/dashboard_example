# Import necessary libraries
from dash import Dash, dcc, html, Input, Output, callback

# Import data and chart generation functions
from functions import data_utils

from functions import chart_utils

# Fetch the data and headers
data, headers = data_utils.fetch_selected_data()

# Initialize Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div(
    [
        dcc.Graph(id="ecg-pie-chart"),
        dcc.Graph(id="ecg-line-chart"),
        dcc.Graph(id="ecg-bar-chart"),
        dcc.Graph(id="ecg-agebar-chart"),
        dcc.Graph(id="ecg-agepie-chart"),
    ]
)

# Define callback functions
chart_utils.register_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
