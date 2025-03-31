import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Features
y = np.array([2.2, 2.8, 3.6, 4.5, 5.1])      # Labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Print results
print("Predicted values:", y_pred)
print("Actual values:", y_test)


# Plot the regression line
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.legend()
plt.show()