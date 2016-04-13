import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

# frequencies
testlist = [1, 2, 2, 2, 2, 3, 4, 4, 4, 3, 3, 3]
c = collections.Counter(testlist)
count_sum = sum(c.values())
for k, v in c.iteritems():
	print "The frequency of letter " + str(k) + " is " + str(float(v) / count_sum)


# boxplot
plt.boxplot(testlist)
plt.savefig("boxplot.png")

# histogram
plt.hist(testlist, histtype='bar')
plt.savefig("histogram.png")

# qqplot
plt.figure()
#test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.savefig("qqplot.png") #this will generate the first graph

