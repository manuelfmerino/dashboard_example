import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


### Plot generation
def generate_gender_pie_chart(data, headers, stroke_value):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == stroke_value]

    # Count the occurrences of each gender
    gender_counts = df["gender"].value_counts()

    figure = go.Figure(
        data=[go.Pie(labels=gender_counts.index, values=gender_counts.values, hole=0.6)]
    )
    figure.update_layout(
        title={
            "text": "Gender",
            "font": {"size": 24},
            "x": 0.45,  # center title
        },
        autosize=False,
        width=450,
        height=400,
    )

    return figure


def generate_residence_pie_chart(data, headers, residence_stroke_val):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == residence_stroke_val]

    # Count the occurrences of each gender
    gender_counts = df["residence_type"].value_counts()

    figure = go.Figure(
        data=[go.Pie(labels=gender_counts.index, values=gender_counts.values, hole=0.6)]
    )
    figure.update_layout(
        title={
            "text": "Residence",
            "font": {"size": 24},
            "x": 0.45,  # center title
        },
        autosize=False,
        width=450,
        height=400,
    )

    return figure


def generate_agebar_chart(data, headers, age_stroke_val):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == age_stroke_val]

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
            "text": "Age",
            "font": {"size": 24},
            "x": 0.5,  # center title
        },
        xaxis_title="Age Group",
        yaxis_title="Count",
        width=800,
        height=400,
    )

    return fig


def generate_stroke_positive_smoker_chart(data, headers, smoker_stroke_val):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == smoker_stroke_val]

    # Count the occurrences of each smoking case
    smoking_counts = df["smoking_status"].value_counts()

    color_map = {
        "never smoked": "#5863f9",
        "Unknown": "#ec4b34",
        "formerly smoked": "#9b59b6",
        "smokes": "#00c58b",
    }
    colors = [color_map[label] for label in smoking_counts.index]

    figure = go.Figure(
        go.Treemap(
            labels=smoking_counts.index,
            parents=[""] * len(smoking_counts),  # single-level treemap
            values=smoking_counts.values,
            marker=dict(colors=colors),
            textinfo="label+value+percent root",
        )
    )

    figure.update_layout(
        title={
            "text": "Smoking status",
            "font": {"size": 24},
            "x": 0.45,  # center title
        },
        autosize=False,
        width=500,
        height=450,
    )

    return figure


def generate_job_tree_chart(data, headers, job_stroke_val):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Get stroke-positive people
    df = df[df["stroke"] == job_stroke_val]

    # Count the occurrences of each smoking case
    job_counts = df["work_type"].value_counts()

    color_map = {
        "Private": "#5863f9",
        "Self-employed": "#ec4b34",
        "children": "#9b59b6",
        "Govt_job": "#00c58b",
        "Never_worked": "#ff9750",
    }
    colors = [color_map[label] for label in job_counts.index]

    figure = go.Figure(
        data=[
            go.Pie(
                labels=job_counts.index,
                values=job_counts.values,
                marker=dict(colors=colors),
                hole=0.6,
            )
        ]
    )

    figure.update_layout(
        title={
            "text": "Occupation",
            "font": {"size": 24},
            "x": 0.45,  # center title
        },
        autosize=False,
        width=500,
        height=450,
    )

    return figure


def generate_glucose_box_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    figure = go.Figure()
    figure.add_trace(
        go.Box(
            y=df[df["stroke"] == "No"]["avg_glucose_level"],
            name="Healthy",
            marker_color="lightseagreen",
        )
    )
    figure.add_trace(
        go.Box(
            y=df[df["stroke"] == "Yes"]["avg_glucose_level"],
            name="Stroke",
            marker_color="indianred",
        )
    )
    figure.update_layout(
        title={
            "text": "Avg. glucose levels",
            "font": {"size": 24},
            "x": 0.5,  # center title
        },
        xaxis_title="Patient",
        yaxis_title="Glucose levels (mg/dL)",
        autosize=False,
        width=450,
        height=400,
    )

    return figure


def generate_bmi_box_chart(data, headers):
    # Convert the data and headers to a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)

    figure = go.Figure()
    figure.add_trace(
        go.Box(
            y=df[df["stroke"] == "No"]["bmi"],
            name="Healthy",
            marker_color="lightseagreen",
        )
    )
    figure.add_trace(
        go.Box(
            y=df[df["stroke"] == "Yes"]["bmi"],
            name="Stroke",
            marker_color="indianred",
        )
    )
    figure.update_layout(
        title={
            "text": "BMI",
            "font": {"size": 24},
            "x": 0.5,  # center title
        },
        xaxis_title="Patient",
        yaxis_title="Body mass index",
        autosize=False,
        width=450,
        height=400,
    )

    return figure


# Callbacks
from dash import Input, Output
from functions import data_utils

# Fetch the data and headers
data, headers = data_utils.fetch_selected_data()


# Define callback functions
def update_kpis_chart(chart_id):
    df = pd.DataFrame(data, columns=headers)

    return (
        len(df),
        (df["stroke"] == "Yes").sum(),
        (df["stroke"] == "No").sum(),
    )


def update_gender_pie_chart(stroke_value):
    figure = generate_gender_pie_chart(data, headers, stroke_value)
    return figure


def update_residence_pie_chart(residence_stroke_val):
    figure = generate_residence_pie_chart(data, headers, residence_stroke_val)
    return figure


def update_agebar_chart(age_stroke_val):
    figure = generate_agebar_chart(data, headers, age_stroke_val)
    return figure


def update_stroke_positive_smoker_chart(smoker_stroke_val):
    figure = generate_stroke_positive_smoker_chart(data, headers, smoker_stroke_val)
    return figure


def update_job_tree_chart(job_stroke_val):
    figure = generate_job_tree_chart(data, headers, job_stroke_val)
    return figure


def update_glucose_box_chart(chart_id):
    figure = generate_glucose_box_chart(data, headers)
    return figure


def update_bmi_box_chart(chart_id):
    figure = generate_bmi_box_chart(data, headers)
    return figure


# Register the callback functions
def register_callbacks(app):

    @app.callback(
        Output("kpi-total", "children"),
        Output("kpi-stroke", "children"),
        Output("kpi-no-stroke", "children"),
        Input("gender-pie-chart", "figure"),  # or a dropdown, etc.
    )
    def update_kpis_callback(chart_id):
        return update_kpis_chart(chart_id)

    @app.callback(
        Output("gender-pie-chart", "figure"), [Input("gender_stroke_val", "value")]
    )
    def update_gender_pie_chart_callback(gender_stroke_val):
        return update_gender_pie_chart(gender_stroke_val)

    @app.callback(
        Output("residence-pie-chart", "figure"),
        [Input("residence_stroke_val", "value")],
    )
    def update_residence_pie_chart_callback(residence_stroke_val):
        return update_residence_pie_chart(residence_stroke_val)

    @app.callback(Output("agebar-chart", "figure"), [Input("age_stroke_val", "value")])
    def update_agebar_chart_callback(age_stroke_val):
        return update_agebar_chart(age_stroke_val)

    @app.callback(
        Output("stroke-positive-smoker-chart", "figure"),
        [Input("smoker_stroke_val", "value")],
    )
    def update_stroke_positive_smoker_chart_callback(smoker_stroke_val):
        return update_stroke_positive_smoker_chart(smoker_stroke_val)

    @app.callback(
        Output("job-tree-chart", "figure"),
        [Input("job_stroke_val", "value")],
    )
    def update_job_tree_chart_callback(job_stroke_val):
        return update_job_tree_chart(job_stroke_val)

    @app.callback(
        Output("glucose-bar-chart", "figure"),
        [Input("glucose-bar-chart", "id")],
    )
    def update_glucose_box_chart_callback(chart_id):
        return update_glucose_box_chart(chart_id)

    @app.callback(
        Output("bmi-bar-chart", "figure"),
        [Input("bmi-bar-chart", "id")],
    )
    def update_bmi_box_chart_callback(chart_id):
        return update_bmi_box_chart(chart_id)
