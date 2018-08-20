#Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the Data Set
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Split the Data Set into Training and Test Set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fit Simple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test Set Results
y_pred = regressor.predict(X_test)

# Ask User for Years of Experience
exp = input("Enter Years of Experience: ")
exp = int(exp)
salary = regressor.predict(exp)
salary = int(salary)
print("With", exp, "years of experience, you should obtain a salary of approximately $", salary)
