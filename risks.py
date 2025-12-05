import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('dark_background')        

tickers = input("Enter ticker symbols separated by commas: ").split(',')
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
df = yf.download(tickers, start=start_date, end=end_date)
print(df.head())
print(df.tail())

returns = np.log(df['Close']/df['Close'].shift(1)) 
print(returns.head())

sec_risk = returns.std()*252**0.5*100

print("\nAnnualized Simple Returns Risk for Stocks:" )  
print(sec_risk)

#position sizing based on risk
total_capital = float(input("Enter your total capital for investment: "))
print("\nPosition Sizing Based on Risk:")
for ticker in tickers:
    risk = sec_risk[ticker]
    if risk != 0:
        position_size = (total_capital * 0.01) / (risk / 100)
        print(f"For {ticker}, with a risk of {round(risk, 2)}%, you should invest approximately: ${round(position_size, 2)}")
    else:
        print(f"For {ticker}, risk is zero, cannot determine position size.")

#plotting risk bar chart
colors = ['cyan', 'magenta', 'yellow', 'lime', 'orange', 'red', 'blue', 'green']
sec_risk.plot(kind='bar', figsize=(10, 6), color=colors[:len(tickers)])
plt.title("Annualized Risks of Stocks")
plt.xlabel("Ticker Symbols")
plt.ylabel("Risk (%)")
plt.show()