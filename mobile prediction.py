import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('Price.csv')
plt.scatter(data['Version'], data['Price'])
plt.show()
model = LinearRegression()
model.fit(data[['Version']], data[['Price']])
print(model.predict([[30]]))
