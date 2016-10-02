
# simulate binomial with 8 possibillities
s1 = np.random.binomial(1,0.5,8)
# simulate binomial with 8 possibillities, biased one
s2 = np.random.binomial(1,0.3,8)
# simulate binomial with 8 possibillities, biased one with 0.7
s3 = np.random.binomial(1,0.7,8)
# Print s1,s2 and s3 
s1
#Out[16]: array([0, 1, 0, 0, 0, 1, 0, 1])
s2
#Out[17]: array([0, 0, 1, 0, 0, 0, 1, 0])
s3
#Out[18]: array([0, 1, 1, 1, 1, 1, 1, 1])
# Try biased with 80 times
In [19]: s4 = np.random.binomial(5,0.3,80)
# Try biased with 800 times
In [20]: s5 = np.random.binomial(5,0.3,800)
# Observe the mean if experiment is tried 8,80 and 800 times 
s4.mean()
#Out[22]: 1.2625
s5.mean()
#Out[23]: 1.5325
s6 = np.random.binomial(5,0.3,8000)
s6.mean()
# Its observed that as no of trials increased, mean closes to 1.5 , 0.3*5
#Out[25]: 1.49925
# import norm
from scipy.stats import norm
# Create a Cumulative distribution function
norm.cdf(12,10,3)
# See values in cdf before/after
1-norm.cdf(8,10,3)
# Add two cdfs and observe 
norm.cdf(8,10,3)+(1-norm.cdf(12,10,3))
#Out[31]: 0.50498507509384583
# Generate normal distribution 
s7 = np.random.normal(5,2,1000)
#reshape to get series
s8 = s7.reshape((len(s7),1))
# convert it ot dataframe
s9 = pd.DataFrame(s8)
# Find summary stats 
s9.mean()
#0    4.920263
s9.skew()
#Out[42]: 0   -0.059438
s9.std()
#Out[43]: 0    1.938332
s9.kurt()
#Out[44]: 0    0.001233
#  Positive excess kurtosis: leptokurtic, Negative excess kurtosis: platykurtic
# Read a csv named wage1
wages = pd.read_csv("wage1.csv")
import statsmodels.api as sm
# Set independant and dependant variables
y = wages.wage
X = wages.educ
# Give OLS as criteria
r = sm.OLS(y,X)
# Fir the regression and see summary 
rf = r.fit()
rf.summary()
# Calculate coefficients manually 
Beta1 = np.dot(X,y.T)/np.dot(X,X.T)
# Read another data frame
charity = pd.read_csv("charity.csv")
charity.gift.mean()
#Out[59]: 7.444470477975632
charity.mailsyear.mean()
#Out[60]: 2.0495548266166823
charity.mailsyear.min()
#Out[61]: 0.25
# Declare independant and dependant variables
y = charity.gift
x = charity.mailsyear
# Fit regression 
x = sm.add_constant(charity.mailsyear)
r = sm.OLS(y,x)
rf = r.fit()
