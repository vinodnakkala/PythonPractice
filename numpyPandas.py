# import libraries
import numpy as np
import pandas as pd
# Load dataset
data = np.genfromtxt('401K.csv',delimiter=',', dtype=float, skip_header = 1)
Y = data[:,0:1]
TempX = data[:,1:2]
TempX.size
K = np.ones((1534,1))
X = np.column_stack ((K,TempX))
B = np.dot (np.linalg.inv (np.dot(X.T,X)), np.dot(X.T,Y))
B
E = Y - np.dot(X,B)
E
SSE = np.dot(E.T, E)
SSE
import pandas_datareader.data as web
df = pd.read_csv('aapl.csv')
df
Value = df.Strike * df.Vol
df['size'] = Value
df
df['size'].sum()
df['size'].sum()/df['Vol'].sum()
(df['Open_Int']*df['Strike']).sum()/df['Open_Int'].sum()
df[df['Type'] == 'call']['size'].sum()/df[df['Type'] == 'call']['Vol'].sum()
df[df['Type'] == 'put']['size'].sum()/df[df['Type'] == 'put']['Vol'].sum()
(df[df['Type'] == 'call']['Strike'] * df[df['Type'] == 'call']['Open_Int'] ).sum()/df[df['Type'] == 'call']['Open_Int'].sum()
(df[df['Type'] == 'put']['Strike'] * df[df['Type'] == 'put']['Open_Int'] ).sum()/df[df['Type'] == 'put']['Open_Int'].sum()
df1 = df[df['Expiry'] == '3/4/2016' ]
(df1[df1['Type'] == 'call']['Strike'] * df1[df1['Type'] == 'call']['Vol'] ).sum()/df1[df1['Type'] == 'call']['Vol'].sum()
(df1[df1['Type'] == 'put']['Strike'] * df1[df1['Type'] == 'put']['Vol'] ).sum()/df1[df1['Type'] == 'put']['Vol'].sum()
(df1[df1['Type'] == 'call']['Strike'] * df1[df1['Type'] == 'call']['Open_Int'] ).sum()/df1[df1['Type'] == 'call']['Open_Int'].sum()
(df1[df1['Type'] == 'put']['Strike'] * df1[df1['Type'] == 'put']['Open_Int'] ).sum()/df1[df1['Type'] == 'put']['Open_Int'].sum()
