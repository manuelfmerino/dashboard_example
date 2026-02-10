# dashboard_example
Repository for a data visualization dashboard.

Author: Manuel F. Merino
Contact: manuelfmerino@gmail.com

### Description
This is an example of a dashboard for a data visualization project in the monitorization of stroke patients to identify trends in demographics and lifestyle. This dataset can be used to predict individuals liable to suffering a stroke and to select population segments that can be targeted for clinical trials.

### Usage
An online app has been deployed using Plotly Cloud and can be found in the following link: https://a64c4fe1-ba7d-4bca-8e3c-4304b246fb74.plotly.app/
The code is currently configured to load the data from a .csv file to facilitate online deployment. However, it was originally developed to directly read data from a local PostgreSQL database containing the data. If this alternative method is preferred, it is enough to change the function used to read the data in functions/data_utils.py (uncomment first function and comment second one).

### Dataset
I am using the stroke prediction dataset from Kaggle (https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset). The cleaned up version of the dataset is included as a .csv file (datasets/healthcare_stroke_dataset_clean.csv) and as a dump file of the PostgreSQL database (datasets/stroke_db.sql).

### Aditional details
The dashboard allows visualizing the most relevant demographic (gender, residence, age) and lifestyle (smoking status, job) for healthy people and individuals that suffered a stroke. It also includes comparisons of some health markers such as glucose levels and bmi indices.


### Environment used
Python 3.14.3
Pandas 3.0.0
Matplotlib 3.10.8
Plotly 6.5.2
Dash 4.0.0
Seaborn 0.13.2

PostgreSQL 18 and pgAdmin 4 were used.