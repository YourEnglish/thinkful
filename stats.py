import pandas as pd
from scipy import stats


data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

mode_alcohol = stats.mode(df['Alcohol'])
mode_tobacco = stats.mode(df['Tobacco'])

print "The mean for the Alcohol and Tobacco dataset is",
print str(df['Alcohol'].mean()) + " and " + str(df['Tobacco'].mean())

print "The median for the Alcohol and Tobacco dataset is",
print str(df['Alcohol'].median()) + " and " + str(df['Tobacco'].median())

print "The mode for the Alcohol and Tobacco dataset is",
print str(mode_alcohol[0]).strip('[]') + " and" + str(mode_tobacco[0]).strip('[]')

print "The range for the Alcohol and Tobacco dataset is",
print str(max(df['Alcohol']) - min(df['Alcohol'])) + " and " + str(max(df['Tobacco']) - min(df['Tobacco']))

print "The variance for the Alcohol and Tobacco dataset is",
print str(df['Alcohol'].var()) + " and " + str(df['Tobacco'].var())

print "The standard deviation for the Alcohol and Tobacco dataset is",
print str(df['Alcohol'].std()) + " and " + str(df['Tobacco'].std())


