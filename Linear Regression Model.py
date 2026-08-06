import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Task 1: Data Preparation
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable
y = np.array([2, 4, 5, 4, 5])  # Dependent variable
plt.scatter(x, y)
plt.title("Data Visualization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Task 2: Train the Linear Regression Model
model = LinearRegression()
model.fit(x, y)
print("Slope (m):", model.coef_[0], "Intercept (c):", model.intercept_)

# Task 3: Predictions and Evaluation
y_pred = model.predict(x)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("Mean Squared Error:", mse, "R2 Score:", r2)

# Task 4: Visualizing the Regression Line
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')
plt.title("Regression Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
