#i hate endsem atp 
import numpy as np
import matplotlib.pyplot as pl
import yfinance as yf

df=yf.download(input("enter the ticker symbol: "),start=input("enter the start date (YYYY-MM-DD):  "),end=input("enter the end date (YYYY-MM-DD):  " ))
print(df.head())
print(df.tail())

df['simple returns']=(df['Close']/df['Close'].shift(1))-1
print(df['simple returns'].head())
print(df['simple returns'].tail())

#plotting simple returns
df['simple returns'].plot(grid=True, linewidth=2, figsize=(10, 6))
pl.title("Simple Returns of Stock")
pl.xlabel("Date")
pl.ylabel("Simple Returns")
pl.show()