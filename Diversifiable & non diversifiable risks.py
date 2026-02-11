import pandas as pd
import numpy as np
import yfinance as yf

tickers=['MSFT', 'AAPL', 'GOOGL']
start='2020-01-01'
end='2024-01-01'

sec_returns = yf.download(tickers, start=start, end=end)['Close'].pct_change().dropna()

#Diversifiable risk (specific to individual stocks)
weights = np.array([0.4, 0.3, 0.3])  
var_a = sec_returns['MSFT'].var()*250
var_b = sec_returns['AAPL'].var()*250
var_c = sec_returns['GOOGL'].var()*250

# one-line fix: compute portfolio variance using full covariance matrix (annualized)
pfolio_var = float(weights @ (sec_returns.cov() * 250).values @ weights)

dr= pfolio_var - (weights[0]**2 * var_a + weights[1]**2 * var_b + weights[2]**2 * var_c)
print(f"{round(dr*100,3)}% Diversifiable Risk")

#Non-diversifiable risk (systematic risk affecting the entire market)
ndr= pfolio_var - dr
print(f"{round(ndr*100,3)}% Non-Diversifiable Risk")