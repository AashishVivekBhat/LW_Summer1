import pandas
import numpy

db = pandas.read_csv('SalaryData.csv')
x = db['YearsExperience'].values.reshape(30,1)
y = db['Salary'].values.reshape(30,1)

from sklearn.linear_model import LinearRegression
Model = LinearRegression
Model.fit(x,y)

val = float(input("Enter the Experience : "))
output = Model.predict( [[val]] )
print("\nEstimated Salary : ")
print(output)
