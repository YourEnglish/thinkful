import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# remove %
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate


# split range in two numbers as list
cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))

# change from string to integer
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])

#first_numbers2 = cleanFICORange.map(lambda x: [int(x[0])])


# split the two items in the list
first_numbers, last_numbers = zip(*cleanFICORange)

# add the first items in a new column called "FICO.Score"
loansData['FICO.Score'] = first_numbers

loansData.head()

# extract some columns from the new set
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# reshape the data
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# put two columns together to create an input matrix
x = np.column_stack([x1,x2])

# create linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

# output results summary
print f.summary()

print loansData[0:5]


"""plt.figure()
p = loansData['FICO.Score'].hist()
plt.savefig("ficoscore_hist.png")
plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.savefig("ficoscore_sp.png")
"""






