import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

loansData_raw = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData = pd.DataFrame(loansData_raw)  # Not really crucial, but without
                                         # pd.DataFrame() we would 
                                         # just have "two names for the same
                                         # object". This is the way some
                                         # Python object function and can seem 
                                         # strange at first

# "Cleaning" the data
loansData['Interest.Rate'] = map(lambda x: float(x.replace('%','')),
                                 loansData_raw['Interest.Rate'])
loansData['FICO.Range'] = map(lambda x: int(x.split('-')[0]),
                              loansData_raw['FICO.Range'])

# add new column and replace Interest Rates with 0.0 or 1.0 
# depending on value
loansData.loc[loansData['Interest.Rate'] < 12, 'IR_TF'] = int(1)
loansData.loc[loansData['Interest.Rate'] >= 12, 'IR_TF'] = int(0)

# add new column Intercept with value 1.0
loansData['Intercept'] = 1.0


# Make a list of independent variables we wish to build our model on
ind_vars = ['Amount.Requested',
            'FICO.Range',
            'Intercept']

print loansData[ind_vars].dtypes

y = loansData['IR_TF'].values
X = loansData[ind_vars].values

# define the logistic regression model
logit = sm.Logit(y, X)

# fit the model
logreg_model = logit.fit()

# Print the parameter estimation summary
print logreg_model.summary()

# assign coefficients to list
coeff = logreg_model.params

# assign variables
a2 = coeff[0]
a1 = coeff[1]
const = coeff[2]
e = 2.718281828459

# logistic function
def logistic_function(fico_score, loan_amount):
    p = 1 / (1 + (e ** ((const + (a1 * fico_score) + (a2 * loan_amount)))))
    print str(fico_score) + " as FicoScore and " + str(loan_amount) + " as Loan Amount, gives the following probability to pass " + str(p)

# call function with parameters 
logistic_function(750, 10000)

# Make testing inputs, one for each class of outputs
X_test_1 = loansData.loc[loansData.IR_TF == 1, ind_vars]
X_test_0 = loansData.loc[loansData.IR_TF == 0, ind_vars]

# Get the re
y_test_1 = logreg_model.predict(X_test_1)
y_test_0 = logreg_model.predict(X_test_0)

# Plotting histograms of test outputs
plt.subplot(221)
plt.hist(y_test_1,30)
plt.xlabel('probability')
plt.ylabel('# of cases')
plt.title('Predictions for class 1')

plt.subplot(223)
plt.hist(y_test_0,30)
plt.xlabel('probability')
plt.ylabel('# of cases')
plt.title('Predictions for class 0')

plt.subplot(122)
sns.distplot(y_test_1,
             hist = False,
             kde_kws={"shade": True},
             color = 'b')
sns.distplot(y_test_0,
             hist = False,
             kde_kws={"shade": True},
             color = 'r')
plt.title('Probability density plot')
plt.legend(['Class 1','Class 0'])
plt.xlim([0,1])

plt.tight_layout()  # <- needed for "nice" plotting, without label overlapping
plt.show()

