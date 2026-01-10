import pandas as pd                 
import numpy as np      
import yfinance as yf
import matplotlib.pyplot as plt

plt.style.use('ggplot')     

tickers = input("Enter the ticker symbols (comma separated): ").split(',')
df = yf.download(tickers, start=input("Enter the start date (YYYY-MM-DD):  "), end=input("Enter the end date (YYYY-MM-DD):  " ))        
print(df.head())
print(df.tail())

# Calculating portfolio returns 
returns=(df['Close']/df['Close'].shift(1))-1
print(returns.head())

annualized_returns=returns.mean()*252*100

weights = np.array([float(x) for x in input("Enter the weights for each ticker (comma separated, must sum to 1): ").split(',')])
return_portfolio = np.dot(annualized_returns, weights)
print(f"The annualized portfolio returns is: {round(return_portfolio, 2)}%")                   