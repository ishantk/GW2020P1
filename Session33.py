"""
    Predicting Continuous Value
    Linear Regression sklearn
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

table = pd.read_csv("advertising.csv")
print(table)

X = table.TV.values
Y = table.Sales.values

print(X)
print(Y)

plt.scatter(X, Y)
plt.show()

# Reshaping to 2D Array
X = X.reshape(len(X), 1)        # Original X from DataSet
Y = Y.reshape(len(Y), 1)        # Original Y from DataSet

print(X)
print(Y)

# Create ML Model LinearRegression for predicting Sales on unseen data :)
model = LinearRegression()

# Train the Model
model.fit(X, Y)

b0 = model.intercept_
b1 = model.coef_

# Let's predict the values for all of the original inputs
Y1 = model.predict(X)    # Predicted Y i.e. Y1 for all the Original X


print(X[0], Y[0], Y1[0])

score = r2_score(Y, Y1)
print("R2 Score is:", score)

print("Equation of Line: Y = {} + {}*X".format(b0[0], b1[0][0]))

unseen_x = 18.0
predicted_y = b0[0] +  b1[0][0]*unseen_x
print("Predicted Y is:", predicted_y)

"""
    Project Discussion
    1. Go to Covid19india.org
    2. Webscrap the Data for your state and that too day wise
    3. Create a dataset i.e. .csv file from it
    4. From the data set use either, LinearRegression or PolynomialRegression or anything else of your choice
       to perform predictions of number of cases to come in a future date :) 
    
    May not take more than 3 days | 7 days   

"""