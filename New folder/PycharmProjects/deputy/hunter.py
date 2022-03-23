import numpy as np
import pandas as pd
import matplotlib.pylab as plt
df = pd.read_csv('C:/Users/USER/Desktop/Learning/hunterbioinfo.csv')
print(df.head())
#summary statistics
print(df.describe())

#select a single column
col = df['Age']
print(col)

small_df = df[['Age', 'Gender', 'education']]
print(small_df)
print(small_df.head())

#create new column
df['male'] = df['Gender'] =='male'
print(df)

#converting to numpy
print(col.values)
print(df[['Age','Experience']].values)

#creating a new array
arr = df[['Age','Experience']].values
print(arr.shape)
print(arr[0,1])
print(arr[0])
print(arr[:,1])

#masking
mask = arr[:, 0] < 50
print(mask)
print(arr[mask])
print(mask.sum())

#Visualization
plt.subplot(121)
plt.scatter(df['Age'], df['Experience'])
plt.xlabel('Age')
plt.ylabel('Experience')
plt.subplot(122)
plt.scatter(df['Age'], df['Experience'], c=df['male'])
plt.plot([30, 90], [1, 4])
plt.show()