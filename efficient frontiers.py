import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

assets = ['AAPL', 'MSFT']
start = '2020-01-01'
end = '2024-01-01'
data = yf.download(assets, start=start, end=end)
log_returns = np.log(data['Close'] / data['Close'].shift(1)).dropna()
correlation_matrix = log_returns.corr()
print("Correlation Matrix:")
print(correlation_matrix)
num_assets = len(assets)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
print(weights)
print(weights.sum())

#expected portfolio return 
expected_return = np.sum(weights * log_returns.mean()) * 252
print(f"Expected Portfolio Return: {round(expected_return*100, 2)}%")

#expected portfolio variance
expected_variance = np.dot(weights.T, np.dot(log_returns.cov() * 252, weights))
print(f"Expected Portfolio Variance: {round(expected_variance*100, 4)}%")

#expected portfolio volatility
expected_volatility = np.sqrt(expected_variance)
print(f"Expected Portfolio Volatility: {round(expected_volatility*100, 2)}%")

pfolio_returns = []
pfolio_volatility = []
for x in range(10000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 252)
    pfolio_volatility.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 252, weights))))

pfolio_returns = np.array(pfolio_returns)
pfolio_volatility = np.array(pfolio_volatility)
print(pfolio_returns)
print(pfolio_volatility)

portfolio = pd.DataFrame({'Returns': pfolio_returns, 'Volatility': pfolio_volatility})
portfolio.plot(x= 'Volatility', y='Returns', kind='scatter', figsize=(10, 6), grid=True)
plt.title('Efficient Frontier')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.show()