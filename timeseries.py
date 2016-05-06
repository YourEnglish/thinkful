import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Online I could only find a zip file of this file
# so I have downloaded it to my own computer

dateparse = lambda dates: pd.datetime.strptime(dates, '%b-%Y')

df = pd.read_csv('loans_count.csv', parse_dates='Month', index_col='Month',date_parser=dateparse)
df.columns = ['#Loans']

ts = df['#Loans']

plt.plot(ts)
plt.show()


"""
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)
print loan_count_summary
"""

