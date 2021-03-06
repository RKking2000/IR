# import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read dataset
dataset=pd.read_csv ("hours.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

# Import Linear Regression and creat objet of it
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)
print (' Accuracy : '), regressor.score(X,y) * 100

# predict value using regressor object 
y_pred=regressor.predict([[8]])
print (y_pred)

# Take user input
hours=int (input('Enter the no of hours :'))

# calculate vaule of y
eq=regressor.coef_*hours+regressor.intercept_
print ('y=%f*%f+%f') %(regressor.coef_,hours,regressor.intercept_)
pint ("Risk Score:"), eq[0]
plt.plot(X,y, 'o')
plt.plot(X, regressor.predict(X));
plt.show()