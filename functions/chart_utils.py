import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


### Plot generation
def generate_gender_pie_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == "Yes"]

    # Count the occurrences of each gender
    gender_counts = df["gender"].value_counts()

    figure = go.Figure(
        data=[go.Pie(labels=gender_counts.index, values=gender_counts.values, hole=0.6)]
    )
    figure.update_layout(
        title={
            "text": "Gender distribution",
            "font": {"size": 24},
            "x": 0.5,  # center title
        },
        autosize=False,
        width=500,
        height=500,
    )

    return figure


def generate_agebar_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == "Yes"]

    # Convert age column to numeric data type
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    # Define age groups
    age_groups = [
        "0-5",
        "5-10",
        "10-15",
        "15-20",
        "20-25",
        "25-30",
        "30-35",
        "35-40",
        "40-45",
        "45-50",
        "50-55",
        "55-60",
        "60-65",
        "65-70",
        "70-75",
        "75-80",
        "80-85",
        "85-90",
        "90+",
    ]

    # Assign each age to an age group
    df["Age Group"] = pd.cut(
        df["age"],
        bins=[
            0,
            5,
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            float("inf"),
        ],
        labels=age_groups,
        right=False,
    )

    # Group the data by age group and calculate the count
    grouped_data = df.groupby("Age Group").size().reset_index(name="Count")

    # Create the bar chart
    fig = go.Figure(
        data=go.Bar(
            x=grouped_data["Age Group"],
            y=grouped_data["Count"],
            text=grouped_data["Count"],
            textposition="auto",
        )
    )

    # Customize the layout
    fig.update_layout(
        title={
            "text": "Age distribution",
            "font": {"size": 24},
            "x": 0.5,  # center title
        },
        xaxis_title="Age Group",
        yaxis_title="Count",
        width=900,
        height=500,
    )

    return fig


def generate_stroke_positive_smoker_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == "Yes"]

    # Count the occurrences of each smoking case
    smoking_counts = df["smoking_status"].value_counts()

    figure = go.Figure(
        data=[
            go.Pie(labels=smoking_counts.index, values=smoking_counts.values, hole=0.6)
        ]
    )
    figure.update_layout(
        title={
            "text": "Smoking status",
            "font": {"size": 24},
            "x": 0.5,  # center title
        },
        autosize=False,
        width=500,
        height=500,
    )

    return figure


def generate_glucose_box_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    figure = go.Figure()
    figure.add_trace(
        go.Box(
            y=df[df["stroke"] == "No"]["avg_glucose_level"],
            name="No",
            marker_color="lightseagreen",
        )
    )
    figure.add_trace(
        go.Box(
            y=df[df["stroke"] == "Yes"]["avg_glucose_level"],
            name="Yes",
            marker_color="indianred",
        )
    )
    figure.update_layout(
        title={
            "text": "Average glucose levels",
            "font": {"size": 24},
            "x": 0.5,  # center title
        },
        xaxis_title="Stroke",
        yaxis_title="Glucose levels (mg/dL)",
        autosize=False,
        width=450,
        height=450,
    )

    return figure


# DO THE SAME WITH BMI AND THATS IT!! EXPLAIN AND DOCUMENT!


# Callbacks
from dash import Input, Output
from functions import data_utils

# Fetch the data and headers
data, headers = data_utils.fetch_selected_data()


# Define the callback function to update the pie chart
def update_gender_pie_chart(chart_id):
    figure = generate_gender_pie_chart(data, headers)
    return figure


def update_agebar_chart(chart_id):
    figure = generate_agebar_chart(data, headers)
    return figure


def update_stroke_positive_smoker_chart(chart_id):
    figure = generate_stroke_positive_smoker_chart(data, headers)
    return figure


def update_glucose_box_chart(chart_id):
    figure = generate_glucose_box_chart(data, headers)
    return figure


# Register the callback functions
def register_callbacks(app):
    @app.callback(
        Output("gender-pie-chart", "figure"), [Input("gender-pie-chart", "id")]
    )
    def update_gender_pie_chart_callback(chart_id):
        return update_gender_pie_chart(chart_id)

    @app.callback(Output("agebar-chart", "figure"), [Input("agebar-chart", "id")])
    def update_agebar_chart_callback(chart_id):
        return update_agebar_chart(chart_id)

    @app.callback(
        Output("stroke-positive-smoker-chart", "figure"),
        [Input("stroke-positive-smoker-chart", "id")],
    )
    def update_stroke_positive_smoker_chart_callback(chart_id):
        return update_stroke_positive_smoker_chart(chart_id)

    @app.callback(
        Output("glucose-bar-chart", "figure"),
        [Input("glucose-bar-chart", "id")],
    )
    def update_glucose_box_chart_callback(chart_id):
        return update_glucose_box_chart(chart_id)
