import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    icecream_sales = []
    coldDrink_sales = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            icecream_sales.append(float(row['Temperature']))
            coldDrink_sales.append(float(row['Ice-cream Sales( â‚¹ )']))

    return{'x': icecream_sales, 'y': coldDrink_sales}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Corelation between temperature vs icecream sale:  \n ', corelation[0,1])

def setup():
    data_path = 'icecream.csv'
    dataSource = getDataSource(data_path)
    
    findCorelation(dataSource)
setup()