#using pandas datareader to get gdp data (no API key needed)
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
plt.style.use('dark_background')

gdp_data = pdr.get_data_fred('GDP', start='2000-01-01')
print(gdp_data.head())
print(gdp_data.tail())

gdp_per_capita = pdr.get_data_fred('A939RC0Q052SBEA', start='2000-01-01')
print(gdp_per_capita.head())
print(gdp_per_capita.tail())

gdp_data.to_csv("gdp_data.csv")
gdp_per_capita.to_csv("gdp_per_capita_data.csv")

#plotting gdp data
gdp_data.plot(grid=True, linewidth=2, figsize=(10, 6) )
plt.title("US GDP Over Time")
plt.xlabel("Year")
plt.ylabel("GDP (in Billions USD)")

gdp_per_capita.plot(grid=True, linewidth=2, figsize=(10, 6))
plt.title("US GDP Per Capita Over Time")
plt.xlabel("Year")
plt.ylabel("GDP Per Capita (in USD)")
plt.tight_layout()
plt.show()
 
