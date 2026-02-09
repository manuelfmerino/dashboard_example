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
                "marginBottom": "15px",
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
                    className="kpi-card kpi-generic",
                ),
                html.Div(
                    [
                        html.Div("Healthy", className="kpi-title"),
                        html.Div(id="kpi-no-stroke", className="kpi-value"),
                    ],
                    className="kpi-card kpi-no-stroke",
                ),
                html.Div(
                    [
                        html.Div("Stroke", className="kpi-title"),
                        html.Div(id="kpi-stroke", className="kpi-value"),
                    ],
                    className="kpi-card kpi-stroke",
                ),
            ],
            className="kpi-container",
        ),
        # Row 1 – two large plots
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(
                            id="gender-pie-chart", style={"marginBottom": "-60px"}
                        ),
                        html.P(
                            "Stroke:",
                            style={
                                "textAlign": "left",
                                "marginBottom": "-28px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "paddingLeft": "190px",
                                "position": "relative",
                                "zIndex": 1000,
                            },
                        ),
                        dcc.Dropdown(
                            id="gender_stroke_val",
                            options=[
                                "Yes",
                                "No",
                            ],
                            value="No",  # default selection
                            clearable=False,
                            style={
                                "textAlign": "center",
                                "marginBottom": "5px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "width": "30%",
                                "display": "flex",
                                "margin": "0 auto",
                                "position": "relative",
                                "zIndex": 1000,
                                "paddingLeft": "140px",
                            },
                        ),
                    ]
                ),
                html.Div(
                    [
                        dcc.Graph(
                            id="residence-pie-chart", style={"marginBottom": "-60px"}
                        ),
                        html.P(
                            "Stroke:",
                            style={
                                "textAlign": "left",
                                "marginBottom": "-28px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "paddingLeft": "190px",
                                "position": "relative",
                                "zIndex": 1000,
                            },
                        ),
                        dcc.Dropdown(
                            id="residence_stroke_val",
                            options=[
                                "Yes",
                                "No",
                            ],
                            value="No",  # default selection
                            clearable=False,
                            style={
                                "textAlign": "center",
                                "marginBottom": "5px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "width": "30%",
                                "display": "flex",
                                "margin": "0 auto",
                                "position": "relative",
                                "zIndex": 1000,
                                "paddingLeft": "140px",
                            },
                        ),
                    ]
                ),
                html.Div(
                    [
                        dcc.Graph(id="agebar-chart", style={"marginBottom": "-50px"}),
                        html.P(
                            "Stroke:",
                            style={
                                "textAlign": "left",
                                "marginBottom": "-28px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "paddingLeft": "500px",
                                "position": "relative",
                                "zIndex": 1000,
                            },
                        ),
                        dcc.Dropdown(
                            id="age_stroke_val",
                            options=[
                                "Yes",
                                "No",
                            ],
                            value="No",  # default selection
                            clearable=False,
                            style={
                                "textAlign": "center",
                                "marginBottom": "5px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "width": "20%",
                                "display": "flex",
                                "margin": "0 auto",
                                "position": "relative",
                                "paddingLeft": "500px",
                                "zIndex": 1000,
                            },
                        ),
                    ]
                ),
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
                html.Div(
                    [
                        dcc.Graph(
                            id="stroke-positive-smoker-chart",
                            style={"marginBottom": "-60px"},
                        ),
                        html.P(
                            "Stroke:",
                            style={
                                "textAlign": "left",
                                "marginBottom": "-28px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "paddingLeft": "185px",
                                "position": "relative",
                                "zIndex": 1000,
                            },
                        ),
                        dcc.Dropdown(
                            id="smoker_stroke_val",
                            options=[
                                "Yes",
                                "No",
                            ],
                            value="No",  # default selection
                            clearable=False,
                            style={
                                "textAlign": "center",
                                "marginBottom": "5px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "width": "30%",
                                "display": "flex",
                                "margin": "0 auto",
                                "position": "relative",
                                "zIndex": 1000,
                                "paddingLeft": "180px",
                            },
                        ),
                    ]
                ),
                html.Div(
                    [
                        dcc.Graph(
                            id="job-tree-chart",
                            style={"marginBottom": "-60px", "paddingLeft": "20px"},
                        ),
                        html.P(
                            "Stroke:",
                            style={
                                "textAlign": "left",
                                "marginBottom": "-28px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "paddingLeft": "250px",
                                "position": "relative",
                                "zIndex": 1000,
                            },
                        ),
                        dcc.Dropdown(
                            id="job_stroke_val",
                            options=[
                                "Yes",
                                "No",
                            ],
                            value="No",  # default selection
                            clearable=False,
                            style={
                                "textAlign": "center",
                                "marginBottom": "5px",
                                "fontSize": "18px",
                                "fontFamily": "Arial, sans-serif",
                                "fontWeight": "700",
                                "color": "#2c3e50",
                                "width": "30%",
                                "display": "flex",
                                "margin": "0 auto",
                                "position": "relative",
                                "zIndex": 1000,
                                "paddingLeft": "300px",
                            },
                        ),
                    ]
                ),
                dcc.Graph(id="glucose-bar-chart"),
                dcc.Graph(id="bmi-bar-chart"),
            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr 1fr 1fr",
                "gap": "0px",
                "marginTop": "10px",
            },
        ),
    ]
)


# Define callback functions
chart_utils.register_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
