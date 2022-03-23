import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm
data = pd.read_excel(r'C:\Users\USER\My Documents\office.xlsx')
df = pd.DataFrame(data, columns=['decour', 'strength','lighting','productivity'])
print(df)

#Visualization
plt.subplot(131)
plt.scatter(df['decour'],df['productivity'], color = 'Blue', marker = 'o')
plt.title('Office Decoration Vs Employee Productivity')
plt.xlabel('Office Decoration')
plt.ylabel('Employee Decoration')
plt.xticks([]); plt.xticks([])
plt.subplot(132)
plt.scatter(df['strength'],df['productivity'], color = 'Red', marker = '^')
plt.title('Office Strength Vs Employee Productivity')
plt.xlabel('Office Strength')
plt.ylabel('Employee Decoration')
plt.xticks([]); plt.xticks([])
plt.subplot(133)
plt.scatter(df['lighting'],df['productivity'], color = 'Green', marker = 'o')
plt.title('Office Lighting Vs Employee Productivity')
plt.xlabel('Office Ligthing')
plt.ylabel('Employee Decoration')
plt.xticks([]); plt.xticks([])


#Numerical computations
#Descriptive tools
print(df.describe())

#correlation
print('The Pairwise Correlation Coefficient \n')
print(df.corr())

#Multiple regression analysis
X = df[['decour','strength','lighting']]
Y = df['productivity']

#with sklearn
mregr = linear_model.LinearRegression()
mregr.fit(X, Y)
print('intercept:\n', mregr.intercept_)
print('coefficient:\n', mregr.coef_)
r_sq = mregr.score(X, Y)
#prediction with sklearn
y_pred = mregr.predict(X)
df['Predicted Value'] = y_pred
df['residual'] = df['productivity'] - df['Predicted Value']
print(df)

#forecast
New_decour = np.array([2.4,1.9,3.6])
New_strength = np.array([2.7,3.7,3.2])
New_lighting = np.array([1.3,1.6,2.1])
New_productivity = (mregr.intercept_) + (mregr.coef_[0]) * New_decour + (mregr.coef_[1]) * New_strength + (mregr.coef_[2]) * New_lighting
print('predicted productivity:\n',New_productivity)

#with statsmodels
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
prediction = model.predict(X)
print(prediction)
print_model = model.summary()
print(print_model)
