
# import the libraries
import numpy as np
import pandas as pd
# Read the CSV files required 
t = pd.read_csv('t.csv',index_col=0,header=0)
tn = pd.read_csv("tn.csv", index_col=0,header=0)
users = pd.read_csv("users.csv",header=0)
posts = pd.read_csv("posts.csv",header=0)
users1 = pd.read_csv("users1.csv",header=0)
users2 = pd.read_csv("users2.csv",header=0)
airfare = pd.read_csv("airfare.csv",header=0)
sales = pd.read_csv("sales.csv",header=0)

#subset based on dates and get "High" values
t['2015-04-04':'2015-05-04'].High 
# subset when low is more than 37 and display their high values
temp = t[t['Low']>37]
temp[['High','Low']]
# Alternatively can be done this way
t[t['Low']>37][['High','Low']] 
# Get mean value of 'Adj Close' for last 1 year in the data
Last1Year = t['2015-03-05':'2016-03-04']
Last1Year['Adj Close'].mean() 
# Get minimum value of 'High' of last 1 year
Last1Year = t['2015-03-05':'2016-03-04']
Last1Year['High'].min()
# Get maximum price of 'Low' price of last 3 months
Last3Months = t['2015-12-04':'2016-03-04']
Last3Months['Low'].max() 
# Displaying Average price of Open and Close of each day
t['avg_price'] = 0.5*t['Open']+0.5*t['Close'] 
# Find the average price and display difference between actual price and average price
avg = t.mean()
a7=t-avg 
# Get Absolute difference between 'Open' and 'Close' prices and store it in a column
def absValue(a,b):
   .....:   return  abs(a-b)
t['dpr']=absValue(t['Open'],t['Close']) 
# Move 'Adj Close' of previous day
t['Adj Close']/t['Adj Close'].shift(1)-1
# Drop the observation if there are more than or equal to 2 missing values
tn.dropna(thresh=2) 
# Drop columns having atleast missing values
tn.dropna(thresh=10,axis=1) 
# Merge users and posts dataset
pd.merge(users,posts,left_on='id',right_on='uid') 
# Merge users and posts datasets by retaining all observations in user
pd.merge(users,posts,left_on='id',right_on='uid',how='left') 
# Concatenate users1 and users2 datasets
pd.concat([users1,users2]) 
#Change the view of dataframe to see distance, id wise by each year
airfare.pivot('id','year','dist') 
# Create a pivot table to see distance and Fare for each id and year
airfare.pivot_table(['dist','fare'],index=['id'],columns=['year'])
# Show the passengers having 20% each in the group
passen = airfare.ix[:,3]
pd.qcut(passen,5) 
# Create Dummies and join with airfares
dummies = pd.get_dummies(airfare['year'],prefix='year')
airfare_dummies = airfare.join(dummies)
# The average fare for each id
airfare.groupby('id').mean()
# Create a pivot table to see sales across State/Segment in each year
a20=sales.pivot_table('Sales',index=['State','Segment'],columns=['Year'])


