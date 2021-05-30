import pandas
import numpy
from sklearn.linear_model import LinearRegression

ds = pandas.read_csv('SalaryData.csv')
x = ds['YearExperience'].values.reshape(30,1)
y = ds['Salary']

Model = LinearRegression
Model.fit(x,y)

predict = float(input("Enter the Experience : "))
output = Model.predict( [[predict]] )
print("\nEstimated Salary : ")
print(output)
