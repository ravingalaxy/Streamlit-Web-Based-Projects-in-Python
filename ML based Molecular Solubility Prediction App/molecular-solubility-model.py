import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import pickle

print("Reading the data")
df = pd.read_csv("delaney_solubility_with_descriptors.csv")
df

X = df.drop(['logS'], axis = 1)
X

Y = df.iloc[:,-1]
Y
print("Linear Regression Model")
model = linear_model.LinearRegression()
model.fit(X, Y)

print("Model Prediction")
Y_pred = model.predict(X)
Y_pred

print("Model Performance")
print('Coefficients: ', model.coef_)
print('Intercept: ', model.intercept_)
print('Mean Squared Error (MSE): %.2f' % mean_squared_error(Y,Y_pred))
print('Coefficient of determination (R^2): %.2f' % r2_score(Y,Y_pred))

print("Model Equation")
print('LogS = {} {} LogP {} MW + {} RB {} AP'.format(model.intercept_, model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3]))

print("Data Visualization (Experimental vs Predicted LogS for Training Data)")

plt.figure(figsize = (5,5))
plt.scatter(x = Y, y = Y_pred, c="red", alpha = 0.3)

z = np.polyfit(Y, Y_pred, 1)
p = np.poly1d(z)

plt.plot(Y, p(Y), "green")
plt.ylabel("Predicted LogS")
plt.xlabel("Experimental LogS")
plt.show()

pickle.dump(model, open("molecular_solubility_model.pkl", "wb"))
