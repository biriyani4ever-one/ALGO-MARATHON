#i hate endsem atp 
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('dark_background')

df=yf.download(input("enter the ticker symbol: "),start=input("enter the start date (YYYY-MM-DD):  "),end=input("enter the end date (YYYY-MM-DD):  " ))
print(df.head())
print(df.tail())

df['simple returns']=(df['Close']/df['Close'].shift(1))-1
print(df['simple returns'].head())
print(df['simple returns'].tail())

avg_returns=df['simple returns'].mean()*252*100
print(f"\nThe annualized simple returns is: {round(avg_returns, 2)}%")

#advisory 
print("\nSTOCK BROKER ADVISORY")
print("="*30)

if avg_returns>15:
    print("The stock is performing excellently. Consider buying more shares.")
elif 5<avg_returns<=15:
    print("The stock is performing well. Hold your position.")
elif 0<avg_returns<=5:
    print("The stock is showing modest returns. Monitor closely.")
elif -5<avg_returns<=0:
    print("The stock is underperforming. Consider selling some shares.")
print("="*30)

#plotting simple returns
df['simple returns'].plot(grid=True, linewidth=2, figsize=(10, 6))
plt.title("Simple Returns of Stock")
plt.xlabel("Date")
plt.ylabel("Simple Returns")
plt.show()




