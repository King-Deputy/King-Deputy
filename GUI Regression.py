import pandas as pd
from sklearn import linear_model
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data = pd.read_excel(r'C:\Users\USER\My Documents\office.xlsx')
df = pd.DataFrame(data, columns=['decour', 'strength','lighting','productivity'])
print(df)

X = df[['decour','strength','lighting']].astype(float)
Y = df['productivity'].astype(float)

mregr = linear_model.LinearRegression()
mregr.fit(X, Y)

print('intercept:\n', mregr.intercept_)
print('coefficient:\n', mregr.coef_)

#tkinter GUI
root = tk.Tk()

canvas1 =tk.Canvas(root, width=500, height=300)
canvas1.pack()

#with sklearn
Intercept_result = ('Intercept:', mregr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify= 'center')
canvas1.create_window(260, 200, window=label_Intercept)

#with sklearn
Coefficients_result = ('Coefficients:', mregr.coef_)
label_Coefficient = tk.Label(root, text=Coefficients_result, justify='center')
canvas1.create_window(260, 220, window=label_Coefficient)

#title
title1 = tk.Label(root, text='Welcome to GUI Regression Created by DEPUTY')
canvas1.create_window(200,60,window=title1)

#New_decour label and input box
label1 = tk.Label(root, text='Enter Office Decoration:')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry(root) #create 1st entry box
canvas1.create_window(270,100,window=entry1)

#New_strength label and input box
label2 = tk.Label(root, text='Enter Office Strength:')
canvas1.create_window(100, 120, window=label2)

entry2 = tk.Entry(root) #create 1st entry box
canvas1.create_window(270,120,window=entry2)

#New_lighting label and input box
label3 = tk.Label(root, text='Enter Office ligthing:')
canvas1.create_window(100, 140, window=label3)

entry3 = tk.Entry(root) #create 1st entry box
canvas1.create_window(270,140,window=entry3)

def values():
    global New_decour #our first input variable
    New_decour = float(entry1.get())

    global New_strength  # our second input variable
    New_strength = float(entry2.get())

    global New_lighting  # our first input variable
    New_lighting = float(entry3.get())

    Prediction_result = ('Predicted Productivity:', mregr.predict([[New_decour, New_strength,New_lighting]]))
    label_prediction = tk.Label(root, text= Prediction_result, bg='Orange')
    canvas1.create_window(260, 280, window=label_prediction)

button1 = tk.Button(root, text = 'Predict Productivity', command = values, bg='green')
canvas1.create_window(270, 170, window=button1)

#plot 1st scatter
figure1 = plt.figure(figsize = (4.5,4), dpi = 100)
ax1 = figure1.add_subplot(111)
ax1.scatter(df['decour'].astype(float), df['productivity'].astype(float), color='r')
scatter1 = FigureCanvasTkAgg(figure1, root)
scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax1.legend(['Employee Productivity'])
ax1.set_xlabel('Office Decoration')
ax1.set_title('Office Decoration VS Employee Productivity', fontsize=10)

#plot 2nd scatter
figure2 = plt.figure(figsize = (4.5,4), dpi = 100)
ax2 = figure2.add_subplot(111)
ax2.scatter(df['strength'].astype(float), df['productivity'].astype(float), color='b')
scatter2 = FigureCanvasTkAgg(figure2, root)
scatter2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax2.legend(['Employee Productivity'])
ax2.set_xlabel('Office Strength')
ax2.set_title('Office Strength VS Employee Productivity', fontsize=10)

#plot 3rd scatter
figure3 = plt.figure(figsize = (4.5,4), dpi = 100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df['lighting'].astype(float), df['productivity'].astype(float), color='g')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['Employee Productivity'])
ax3.set_xlabel('Office Lighting')
ax3.set_title('Office Lighting VS Employee Productivity', fontsize=10)

root.mainloop()