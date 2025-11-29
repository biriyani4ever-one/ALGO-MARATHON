#calculating logarithmic returns
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('ggplot')

df=yf.download(input("enter the ticker symbol: "),start=input("enter the start date (YYYY-MM-DD):  "),end=input("enter the end date (YYYY-MM-DD):  " ))
print(df.head())
print(df.tail())
df['log returns']=np.log(df['Close']/df['Close'].shift(1))

log_returns_avg=df['log returns'].mean()*252*100
print(f"The annualized logarithmic returns is: {round(log_returns_avg, 2)}%")

#plotting logarithmic returns
df['log returns'].plot(grid=True, linewidth=2, figsize=(10, 6))
plt.title("Logarithmic Returns of Stock")
plt.xlabel("Date")
plt.ylabel("Logarithmic Returns")
plt.show()
