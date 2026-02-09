# Import the necessary libraries
# import psycopg2
import pandas as pd


# Function to connect to PostgreSQL database and fetch data
""" def fetch_selected_data():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="stroke_db",
            user="manfernandez",  # mostly this is used
            password="",
            host="127.0.0.1",  # mostly this is used
            port="5432",  # mostly this is used
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute a query to fetch file number, gender, and diseases
        cur.execute("SELECT * FROM public.stroke_data")

        # Fetch all rows from the result set
        rows = cur.fetchall()
        headers = [desc[0] for desc in cur.description]

        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return the fetched data and headers
        return rows, headers

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) """


# Alternatively, can directly read data from a .csv file
def fetch_selected_data():
    df = pd.read_csv("datasets/healthcare_stroke_dataset_clean.csv", sep=",")

    rows = df.values
    headers = df.columns.tolist()

    return rows, headers
