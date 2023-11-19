import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

d=pd.read_excel("economy_model.xlsx")
print(d)

plt.scatter(d.year,d.PCI,label=["Year","PCI"],marker=".")

reg=linear_model.LinearRegression()
reg.fit(d[['year']],d.PCI)
plt.plot(d.year,reg.predict(d[["year"]]),color='b')
plt.show()

plt.scatter(d.year,d.GDP,label=["Year","GDP"],marker="*",color='c')
model=linear_model.LinearRegression()
model.fit(d[["year"]],d.GDP)
plt.plot(d.year,model.predict(d[["year"]]),color='b')
plt.show()

year=int(input('Enter the year:'))

c=reg.predict([[year]])
print("The per capita income of India is ",c,"$ and the GDP of india is",model.predict([[year]]),"Billion")
