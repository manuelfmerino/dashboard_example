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
        # Dashboard title
        html.H1(
            "Stroke patients at a glance",
            style={
                "textAlign": "center",
                "marginBottom": "30px",
                "fontSize": "48px",
                "fontFamily": "Arial, sans-serif",
                "fontWeight": "700",
                "color": "#2c3e50",
            },
        ),
        # Brief summary
        html.Div(
            [
                html.Div(
                    [
                        html.Div("Total patients", className="kpi-title"),
                        html.Div(id="kpi-total", className="kpi-value"),
                    ],
                    className="kpi-card",
                ),
                html.Div(
                    [
                        html.Div("Healthy", className="kpi-title"),
                        html.Div(id="kpi-no-stroke", className="kpi-value"),
                    ],
                    className="kpi-no-stroke",
                ),
                html.Div(
                    [
                        html.Div("Stroke", className="kpi-title"),
                        html.Div(id="kpi-stroke", className="kpi-value"),
                    ],
                    className="kpi-stroke",
                ),
            ],
            className="kpi-container",
        ),
        # Row 1 – two large plots
        html.Div(
            [
                dcc.Graph(id="gender-pie-chart"),
                dcc.Graph(id="residence-pie-chart"),
                dcc.Graph(id="agebar-chart"),
            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr 1fr",
                "gap": "0px",
            },
        ),
        # Row 2 – three smaller plots
        html.Div(
            [
                dcc.Graph(id="stroke-positive-smoker-chart"),
                dcc.Graph(id="job-tree-chart"),
                dcc.Graph(id="glucose-bar-chart"),
                dcc.Graph(id="bmi-bar-chart"),
            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr 1fr 1fr",
                "gap": "0px",
                "marginTop": "20px",
            },
        ),
    ]
)


# Define callback functions
chart_utils.register_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
