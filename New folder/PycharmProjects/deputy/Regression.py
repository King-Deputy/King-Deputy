import numpy as np
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import xlrd
import matplotlib.pyplot as plt
data = pd.read_excel(r'C:\Users\USER\My Documents\Age_Score.xlsx')
df = pd.DataFrame(data, columns=['Age', 'Score'])
print(df)
#plot scatter diagram
plt.scatter(df['Age'],df['Score'],color='red')
plt.title('Students Age VS Students Score',fontsize=14)
plt.xlabel('Students Age',fontsize=14)
plt.ylabel('Students Score',fontsize=14)
plt.grid(True)
plt.show()
#running Simple linear regression
X = np.array(df['Age']).reshape((-1, 1))
Y = np.array(df['Score'])
#with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)
r_sq = regr.score(X,Y)

print('intercept: \n', regr.intercept_)
print('coefficient \n', regr.coef_)
print('coefficient of determination: \n', r_sq)
#prediction with sklearn
Y_pred = regr.predict(X)
print('predicted response:',Y_pred)

New_Age = [33]
print('Predicted Score: \n', regr.predict([New_Age]))

#with statsmodels
X=sm.add_constant(X)

model = sm.OLS(Y,X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
