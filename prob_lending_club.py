import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# make DataFrame of github data
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# clean the data by removing rows with NULL values
loansData.dropna(inplace=True)

# generate boxplot for Amount Requested
loansData.boxplot(column='Amount.Requested')
plt.savefig("amount_requested_boxplot.png")

# generate histogram for Amount Requested
loansData.hist(column='Amount.Requested')
plt.savefig("amount_requested_histogram.png")

# test if data is normally distributed
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("amount_requested_qq.png")
