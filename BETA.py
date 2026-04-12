import pandas as pd
import numpy as np
import yfinance as yf

tickers=['PG', '^GSPC']
start='2020-01-01'
end='2024-01-01'
df=yf.download(tickers,start,end)['Close']

LOG_RETURNS = np.log(df / df.shift(1)).dropna()

cov = LOG_RETURNS.cov() * 252

cov_with_market = cov.loc['PG', '^GSPC']

print(f"Covariance of MSFT with the market: {round(cov_with_market, 6)}")

var_market = LOG_RETURNS['^GSPC'].var() * 252
print(f"Variance of the market: {round(var_market, 6)}")

beta = cov_with_market / var_market
print(f"Beta of MSFT: {round(beta, 6)}")

if beta > 1:
    print("MSFT is more volatile than the market.")
elif beta < 1:
    print("MSFT is less volatile than the market.")
else:
    print("MSFT has the same volatility as the market.")