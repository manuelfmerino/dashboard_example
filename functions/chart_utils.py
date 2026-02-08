import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


### Plot generation
# Function to generate the pie chart
def generate_gender_pie_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == "Yes"]

    # Count the occurrences of each disease
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


def generate_line_chart(data, headers):
    df = pd.DataFrame(data, columns=headers)

    dx1_counts = df["DX1"].value_counts().reset_index()
    dx1_counts.columns = ["DX1", "Count"]
    dx1_counts = dx1_counts.sort_values(by="DX1")

    fig = px.line(dx1_counts, x="DX1", y="Count")

    fig.update_layout(
        yaxis=dict(range=[0, 20000]), xaxis_title="DX1", yaxis_title="Count"
    )

    return fig


def generate_bar_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Reshape the data to create a single 'Disease' column
    diseases = df[["DX1", "DX2", "DX3"]].values.flatten()
    genders = df["Gender"].values.repeat(3)
    df = pd.DataFrame({"Disease": diseases, "Gender": genders})

    # Drop missing values (empty cells)
    df = df.dropna(subset=["Disease"])

    # Group the data by disease and gender, and calculate the count
    grouped_data = df.groupby(["Disease", "Gender"]).size().reset_index(name="Count")

    # Create the bar chart
    fig = go.Figure()

    # Add bars for each disease and gender
    for gender in grouped_data["Gender"].unique():
        gender_data = grouped_data[grouped_data["Gender"] == gender]
        fig.add_trace(
            go.Bar(
                x=gender_data["Disease"],
                y=gender_data["Count"],
                name=gender,
                text=gender_data["Count"],
                textposition="auto",
            )
        )

    # Customize the layout
    fig.update_layout(
        title="Distribution of Diseases by Gender",
        xaxis_title="Disease",
        yaxis_title="Count",
        barmode="group",
        width=1500,
        height=700,
    )
    return fig


def generate_agepie_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Reshape the data to create a single 'Disease' column
    diseases = df[["DX1", "DX2", "DX3"]].values.flatten()
    genders = df["Gender"].values.repeat(3)
    df = pd.DataFrame({"Disease": diseases, "Gender": genders})

    # Drop missing values (empty cells)
    df = df.dropna(subset=["Disease"])

    # Group the data by gender and calculate the count
    grouped_data = df.groupby("Gender").size().reset_index(name="Count")

    # Create the pie chart
    fig = go.Figure(
        data=go.Pie(
            labels=grouped_data["Gender"],
            values=grouped_data["Count"],
            textinfo="label+percent",
            insidetextorientation="radial",
            hole=0.6,
        )
    )

    # Customize the layout
    fig.update_layout(
        title="Distribution of Diseases by Gender",
    )

    return fig


# Callbacks
from dash import Input, Output
from functions import data_utils

# Fetch the data and headers
data, headers = data_utils.fetch_selected_data()


# Define the callback function to update the pie chart
def update_gender_pie_chart(chart_id):
    figure = generate_gender_pie_chart(data, headers)
    return figure


def update_agepie_chart(chart_id):
    figure = generate_agepie_chart(data, headers)
    return figure


def update_bar_chart(chart_id):
    figure = generate_bar_chart(data, headers)
    return figure


def update_agebar_chart(chart_id):
    figure = generate_agebar_chart(data, headers)
    return figure


def update_line_chart(chart_id):
    figure = generate_line_chart(data, headers)
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

    # @app.callback(Output("agepie-chart", "figure"), [Input("agepie-chart", "id")])
    # def update_agepie_chart_callback(chart_id):
    #    return update_agepie_chart(chart_id)

    # @app.callback(Output("bar-chart", "figure"), [Input("bar-chart", "id")])
    # def update_bar_chart_callback(chart_id):
    #    return update_bar_chart(chart_id)

    # @app.callback(Output("line-chart", "figure"), [Input("line-chart", "id")])
    # def update_line_chart_callback(chart_id):
    #    return update_line_chart(chart_id)
