import pandas as pd
import statsmodels.api as sm
import numpy as np


# load cvs file
loansData = pd.read_csv('loansData_clean.csv')

# add new column and replace Interest Rates with 0.0 or 1.0 
# depending on value
loansData.loc[loansData['Interest.Rate'] < 0.12, 'IR_TF'] = 0
loansData.loc[loansData['Interest.Rate'] >= 0.12, 'IR_TF'] = 1

# add new column Intercept with value 1.0
loansData['Intercept'] = 1.0

ind_vars = ['Amount.Requested', 'Amount.Funded.By.Investors', 'Interest.Rate', 'Monthly.Income', 'Open.CREDIT.Lines', 'Revolving.CREDIT.Balance', 'Inquiries.in.the.Last.6.Months', 'FICO.Score', 'IR_TF', 'Intercept']
loansData[ind_vars] = loansData[ind_vars].astype(float)
loansData.convert_objects(convert_numeric=True)

ind_vars = list(loansData.columns.values)


print loansData[ind_vars].dtypes

# define the logistic regression model
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

# fit the model
result = logit.fit()

# Get the fitted coefficients from the results.
coeff = result.params
print(coeff)

