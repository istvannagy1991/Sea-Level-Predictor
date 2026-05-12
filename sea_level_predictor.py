#tengerszint előrejelző
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    #read csv
    df = pd.read_csv('epa-sea-level.csv')
    df = df.dropna()    #clead data nan values
    df['Year'] = pd.to_numeric(df['Year'])
    plt.figure(figsize=(10,6))

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Calculate line of best fit
    res = linregress(df['Year'].values, df['CSIRO Adjusted Sea Level'].values)
    x_pred = np.arange(df['Year'].min(), 2051)
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r', linewidth=2)

    # Second line of best fit (2000 onward)
    df_2000 = df[df['Year'] >= 2000]

    res_2000 = linregress(
        df_2000['Year'],
        df_2000['CSIRO Adjusted Sea Level']
    )

    x_2000 = np.arange(2000, 2051)
    y_2000 = res_2000.slope * x_2000 + res_2000.intercept

    plt.plot(x_2000, y_2000, 'g', linewidth=2)


    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')


    plt.show()
    return plt.gca()
