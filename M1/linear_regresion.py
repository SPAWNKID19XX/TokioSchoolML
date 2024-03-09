import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Your data
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 samples, 1 feature, scaled by 10
# Generate corresponding Y values with some noise
noise = np.random.normal(0, 1, (100, 1))  # Add normal distribution noise
Y = 2 * X + 3 + noise  # Linear relationship with intercept 3 and slope 2

x = np.array(X)
y = np.array(Y)

# Reshape the data if it's a single feature
x = x.reshape(-1, 1)

# Create and fit the model
model = LinearRegression()
model.fit(x, y)

# Make predictions
y_pred = model.predict(x)

# Calculate mean squared error
mse = mean_squared_error(y, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot the original data and the regression line
plt.scatter(x, y, label='Original data')
plt.plot(x, y_pred, color='red', linewidth=2, label='Linear regression model')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.show()
