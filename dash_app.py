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
        html.H1(
            "Stroke distribution dashboard",
            style={
                "textAlign": "center",
                "marginBottom": "30px",
                "fontSize": "48px",  # bigger text
                "fontFamily": "Arial, sans-serif",
                "fontWeight": "700",
                "color": "#2c3e50",
            },
        ),
        html.Div(
            [
                dcc.Graph(id="gender-pie-chart"),
                dcc.Graph(id="agebar-chart"),
                dcc.Graph(id="stroke-positive-smoker-chart"),
                dcc.Graph(id="glucose-bar-chart"),
            ],
            style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "10px"},
        ),
    ]
)


# Define callback functions
chart_utils.register_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
