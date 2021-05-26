import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    size_of_tv = []
    average_time_spent = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            size_of_tv.append(float(row['Size of TV']))
            average_time_spent.append(float(row['\tAverage time spent watching TV in a week (hours)']))

    return{'x': size_of_tv, 'y': average_time_spent}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Corelation between size of tv vs average watching tv in a week:  \n ', corelation[0,1])

def setup():
    data_path = 'tv.csv'
    dataSource = getDataSource(data_path)
    
    findCorelation(dataSource)
setup()