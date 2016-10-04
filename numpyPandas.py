# import libraries
import numpy as np
import pandas as pd
# Load dataset
data = np.genfromtxt('401K.csv',delimiter=',', dtype=float, skip_header = 1)
# Separate independent and dependant variables in different dataframes
Y = data[:,0:1]
TempX = data[:,1:2]
TempX.size
# Add 1's in the column
K = np.ones((1534,1))
# Stack by column, 1s and two columns above
X = np.column_stack ((K,TempX))
# Dot product of dot products to compute coefficient
B = np.dot (np.linalg.inv (np.dot(X.T,X)), np.dot(X.T,Y))
# Calculate error term
E = Y - np.dot(X,B)
# Calculate Sum of squared Errors
SSE = np.dot(E.T, E)
# Read aaple stock data
import pandas_datareader.data as web
df = pd.read_csv('aapl.csv')
# Create Value, product of Volume and Strike
Value = df.Strike * df.Vol
# Store it as Size in the dataframe
df['size'] = Value
# See the sum of Size
df['size'].sum()
# Calculate Sum/Volume
df['size'].sum()/df['Vol'].sum()
# Similarly calculate for Opening price
# Calculate the weighted strike price using ‘Vol’ as weights for put
(df['Open_Int']*df['Strike']).sum()/df['Open_Int'].sum()
df[df['Type'] == 'call']['size'].sum()/df[df['Type'] == 'call']['Vol'].sum()
# # Calculate the weighted strike price using ‘Vol’ as weights for put
df[df['Type'] == 'put']['size'].sum()/df[df['Type'] == 'put']['Vol'].sum()
# # Calculate the weighted strike price using ‘Vol’ as weights for call
# weighted strike price using ‘Open_Int’ as weights
(df[df['Type'] == 'call']['Strike'] * df[df['Type'] == 'call']['Open_Int'] ).sum()/df[df['Type'] == 'call']['Open_Int'].sum()
(df[df['Type'] == 'put']['Strike'] * df[df['Type'] == 'put']['Open_Int'] ).sum()/df[df['Type'] == 'put']['Open_Int'].sum()
# Only ones Expiry is on 3/4/2016
df1 = df[df['Expiry'] == '3/4/2016' ]
# Find the weighted strike price using ‘Vol’ as weights for call and put
(df1[df1['Type'] == 'call']['Strike'] * df1[df1['Type'] == 'call']['Vol'] ).sum()/df1[df1['Type'] == 'call']['Vol'].sum()
(df1[df1['Type'] == 'put']['Strike'] * df1[df1['Type'] == 'put']['Vol'] ).sum()/df1[df1['Type'] == 'put']['Vol'].sum()
# Find the weighted strike price using ‘Open_Int’ as weights for put and call
(df1[df1['Type'] == 'call']['Strike'] * df1[df1['Type'] == 'call']['Open_Int'] ).sum()/df1[df1['Type'] == 'call']['Open_Int'].sum()
(df1[df1['Type'] == 'put']['Strike'] * df1[df1['Type'] == 'put']['Open_Int'] ).sum()/df1[df1['Type'] == 'put']['Open_Int'].sum()
