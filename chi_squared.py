import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import scipy.stats as stats
import collections


# load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# clean the data by removing rows with NULL values
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

print "There are " + str(len(freq)) + " unique number of open credit lines."
print "The most common number of open credit lines is ",
for line, count in freq.most_common(1):
	print '%d with %d occurrences.' % (line, count)

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.savefig("testing_loan_data.png")

chi, p = stats.chisquare(freq.values())

print "The Chi square statistic of the distribution of the data is " + str(chi)
print "And the p-value is " + str(p)

