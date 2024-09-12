import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

# Load the historical stock price data
# data = pd.read_csv('path_to_your_data.csv', index_col='Date', parse_dates=True)

# Example data loading (Replace this with actual data loading)
data = pd.read_csv('/Users/ranvirkumarsharma/Downloads/Quote-Equity-AWFIS-EQ-05-07-2024-to-05-08-2024.csv', index_col='Date', parse_dates=True)

# Preprocess data (assuming the CSV has a 'Close' column for closing prices)
data = data[['Close']]

# Plot the historical data
plt.figure(figsize=(10, 6))
plt.plot(data)
plt.title('Historical Stock Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()

# Split data into train and test sets
train_size = int(len(data) * 0.8)
train, test = data[0:train_size], data[train_size:]

# Train the ARIMA model
model = ARIMA(train, order=(5, 1, 0))
model_fit = model.fit(disp=0)

# Make predictions
predictions = model_fit.forecast(steps=len(test))[0]

# Evaluate the model
error = mean_squared_error(test, predictions)
print(f'Mean Squared Error: {error}')

# Plot predictions vs actual
plt.figure(figsize=(10, 6))
plt.plot(test.index, test, label='Actual')
plt.plot(test.index, predictions, color='red', label='Predicted')
plt.title('Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()
