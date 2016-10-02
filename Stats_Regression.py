

In [13]: s1 = np.random.binomial(1,0.5,8)
 
In [14]: s2 = np.random.binomial(1,0.3,8)
 
In [15]: s3 = np.random.binomial(1,0.7,8)
 
In [16]: s1
Out[16]: array([0, 1, 0, 0, 0, 1, 0, 1])
 
In [17]: s2
Out[17]: array([0, 0, 1, 0, 0, 0, 1, 0])
 
In [18]: s3
Out[18]: array([0, 1, 1, 1, 1, 1, 1, 1])
 
In [19]: s4 = np.random.binomial(5,0.3,80)
 
In [20]: s5 = np.random.binomial(5,0.3,800)
 
In [22]: s4.mean()
Out[22]: 1.2625
 
In [23]: s5.mean()
Out[23]: 1.5325
 
In [24]: s6 = np.random.binomial(5,0.3,8000)
 
In [25]: s6.mean()
Out[25]: 1.49925
 
In [27]: from scipy.stats import norm
 
In [29]: norm.cdf(12,10,3)
Out[29]: 0.74750746245307709
 
In [30]: 1-norm.cdf(8,10,3)
Out[30]: 0.74750746245307709
 
In [31]: norm.cdf(8,10,3)+(1-norm.cdf(12,10,3))
Out[31]: 0.50498507509384583
 
In [32]:s7 = np.random.normal(5,2,1000)
In [34]: s8 = s7.reshape((len(s7),1))
In [40]: s9 = pd.DataFrame(s8)
 
In [41]: s9.mean()
Out[41]:
0    4.920263
dtype: float64
 
In [42]: s9.skew()
Out[42]:
0   -0.059438
dtype: float64
 
In [43]: s9.std()
Out[43]:
0    1.938332
dtype: float64
 
In [44]: s9.kurt()
Out[44]:
0    0.001233
dtype: float64
 //  Positive excess kurtosis: leptokurtic, Negative excess kurtosis: platykurtic
In [47]: wages = pd.read_csv("wage1.csv")
 
In [48]: import statsmodels.api as sm
 
In [51]: y = wages.wage
 
In [52]: X = wages.educ
 
In [53]: r = sm.OLS(y,X)
 
In [54]: rf = r.fit()
In [55]: rf.summary()
 
In [57]: Beta1 = np.dot(X,y.T)/np.dot(X,X.T)
In [58]: charity = pd.read_csv("charity.csv")
In [59]: charity.gift.mean()
Out[59]: 7.444470477975632
 
In [60]: charity.mailsyear.mean()
Out[60]: 2.0495548266166823
 
In [61]: charity.mailsyear.min()
Out[61]: 0.25
 
In [62]: y = charity.gift
 
In [63]: x = charity.mailsyear
 
In [64]: x = sm.add_constant(charity.mailsyear)
In [66]: r = sm.OLS(y,x)
 
In [67]: rf = r.fit()
