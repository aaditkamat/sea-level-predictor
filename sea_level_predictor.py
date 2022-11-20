import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Create scatter plot
    plt.scatter(x, y)
    
    # Create first line of best fit
    result = linregress(x, y)
    slope, intercept = result.slope, result.intercept
    x = np.arange(x.min(), 2051)
    y = slope * x + intercept
    plt.plot(x, y)
    
    # Create second line of best fit
    x = df.loc[df['Year'] >= 2000, 'Year']
    y = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']
    result = linregress(x, y)
    slope, intercept = result.slope, result.intercept
    x = np.arange(x.min(), 2051)
    y = slope * x + intercept
    plt.plot(x, y)
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    return plt.gca()