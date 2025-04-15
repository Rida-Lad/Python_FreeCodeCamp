import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def sea_level_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')
    
    # First line of best fit (all data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = range(1880, 2051)
    plt.plot(years1, res1.intercept + res1.slope*years1, 'r', label='1880-2013 Trend')
    
    # Second line of best fit (2000 onwards)
    recent = df[df['Year'] >= 2000]
    res2 = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    years2 = range(2000, 2051)
    plt.plot(years2, res2.intercept + res2.slope*years2, 'green', label='2000-2013 Trend')
    
    # Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)
    
    # Save and return
    plt.savefig('sea_level_plot.png')
    return plt.gcf()

# Generate the plot
sea_level_plot()