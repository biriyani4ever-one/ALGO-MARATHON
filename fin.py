import numpy as np
import pandas as pd     
import matplotlib.pyplot as plt     
import yfinance as yf


#working with financial data 
df = yf.download(input("Enter the ticker symbol: "), start=input("Enter the start date (YYYY-MM-DD):  "), end=input("Enter the end date (YYYY-MM-DD):  " ))
print(df.head())#for first 5 rows   
print(df.tail())#for last 5 rows        

#sanity check
print("Data downloaded successfully!")
df.info()
print(df.describe())

#DOWNLOADING AND VISUALIZING STOCK DATA
df.to_csv("stock_data.csv")    

#fin.py V2
print("="*40)
#WORKING WITH MULTIPLE STOCKS
tickers = input("Enter ticker symbols separated by commas: ").split(',')
multiple_data = yf.download(tickers, start=input("Enter the start date (YYYY-MM-DD):  "), end=input("Enter the end date (YYYY-MM-DD):  " ))
print(multiple_data.head())
print(multiple_data.tail())
close_prices = multiple_data['Close']
print(close_prices.head())  
norm_price = close_prices/close_prices.iloc[0]*100  #NORMALIZING DATA
#PLOTTING STOCK DATA
norm_price.plot(grid=True,linewidth=3, figsize=(10, 6) )
plt.title("Closing Prices of Stocks")                                   
plt.xlabel("Date")      
plt.ylabel("Price (USD)")
plt.legend(tickers)
plt.show()