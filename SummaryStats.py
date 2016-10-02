
# Calculate mean, standard deviation and variance
# Calculate mean of variances

import numpy as np 

i = 0
large = 100000
a = np.empty([large,1])
mu = 0
sigma = 0.1
var = sigma*sigma

n = 2
while n < 10:
	i = 0
	while i < large:
		a[i,0] = np.random.normal(mu, sigma, n).var()
		i = i + 1
	print "n = ", n
	print "mean of variances:" , a.mean()
	m = float(n)
	print "(n-1)/n of var: ", ((m-1)/m)*var
	print "\n"
	n = n + 1

# generate random numbers and calculate sumary stats
i = 0
large = 100000
a = np.empty([large,1])
b = np.empty([large,1])
mu = 0
sigma = 0.1

n = 100
while n < 110:
	i = 0
	while i < large:
		a[i,0] = np.random.normal(mu, sigma, n)[0]
		b[i,0] = np.random.normal(mu, sigma, n).mean()
		i = i + 1
	
	print "n = ", n
	print "mean of 1st value:" , a.mean()
	print "mean of sample:" , b.mean()
	print "Population mean:" , mu
	print "\n"
	n = n + 1

# Calculate 95% confidence interval using p-values
# See how many times mean is in confidence interval

import math

i = 0
large = 100000
a = np.empty([large,1])
mu = 0
sigma = 1

n = 100
while n < 105:
	i = 0
	while i < large:
		m = np.random.normal(mu, sigma, n).mean()
		x = m - 1.96/math.sqrt(n)
		y = m + 1.96/math.sqrt(n)
		if x <= mu <= y:
			a[i,0] = 0
		else:
			a[i,0] = 1
		i = i + 1
	
	print "n = ", n
	nr = a.sum()
	dr = len(a)

	print "Number of times mu is NOT within 95% CI:" , nr 
	print "Total number of results:", dr
	print "Proportion of times mu is NOT within 95% CI:", nr/dr
	print "\n"
	n = n + 1

 
  
