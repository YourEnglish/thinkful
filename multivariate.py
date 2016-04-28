import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/loans/loansData.csv')

# remove rows with null values
df.dropna(inplace=True)

# "Cleaning" the data
df['int_rate'] = map(lambda x: float(x.replace('%','')),
                                 df['Interest.Rate'])
df['annual_inc'] = map(lambda x: float(x * 12),
                              df['Monthly.Income'])
df['home_ownership'] = df['Home.Ownership']

# new columns for categorical variable home ownership
df.loc[df['home_ownership'] == 'MORTGAGE', 'ho_mortgage'] = int(1)
df.loc[df['home_ownership'] != 'MORTGAGE', 'ho_mortgage'] = int(0)

df.loc[df['home_ownership'] == 'RENT', 'ho_rent'] = int(1)
df.loc[df['home_ownership'] != 'RENT', 'ho_rent'] = int(0)

df.loc[df['home_ownership'] == 'OWN', 'ho_own'] = int(1)
df.loc[df['home_ownership'] != 'OWN', 'ho_own'] = int(0)

# first task: Use income (annual_inc) to model interest rates (int_rate).
x1 = df['annual_inc']
y = df['int_rate']

# The dependent variable
y = np.matrix(y).transpose()
# The independent variables shaped as columns
x = np.matrix(x1).transpose()

# x = np.column_stack([x1, x2])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print f.summary()

# second task: Add home ownership (home_ownership) to the model.
x1 = df['annual_inc']
x2 = df['ho_mortgage']
x3 = df['ho_rent']
x4 = df['ho_own']
y = df['int_rate']

# The dependent variable
y = np.matrix(y).transpose()
# The independent variables shaped as columns
x1 = np.matrix(x1).transpose()
x2 = np.matrix(x2).transpose()
x3 = np.matrix(x3).transpose()
x4 = np.matrix(x4).transpose()

x = np.column_stack([x1, x2, x3, x4])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print f.summary()

