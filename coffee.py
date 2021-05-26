import csv
import plotly.express as px

with open('coffee.csv') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours')
    fig.show()