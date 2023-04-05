import numpy as np
from sklearn.linear_model import LinearRegression

# Generate some synthetic data
x = np.random.rand(100)
y = 2*x + np.random.normal(scale=0.2, size=100)

# Fit a linear regression model
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

# Print the slope and intercept of the fitted line
print('Slope:', model.coef_[0])
print('Intercept:', model.intercept_)
