#preprocess the data

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('/Users/ranvirkumarsharma/Downloads/Quote-Equity-AWFIS-EQ-05-07-2024-to-05-08-2024.csv')

# Strip extra spaces from the column names
data.columns = data.columns.str.strip()

# Convert the 'Date' column to datetime format and set it as the index
data['Date'] = pd.to_datetime(data['Date'], format=('%d-%m-%Y'))
data.set_index('Date', inplace=True)

# Select the 'close' column for analysis
data = data[['close']]

# Plot the historical data
plt.figure(figsize=(10, 6))
plt.plot(data)
plt.title('Historical Stock Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()

# Display the first few rows of the processed data
print(data.head())

#train and test split
# Split the data into train and test sets
train_size = int(len(data) * 0.8)
train, test = data[0:train_size], data[train_size:]

#train the arima model
from statsmodels.tsa.arima.model import ARIMA

# Train the ARIMA model
model = ARIMA(train, order=(5, 1, 0))
model_fit = model.fit()

#make pridiction # Make predictions
predictions = model_fit.forecast(steps=len(test))

# Evaluate the model
from sklearn.metrics import mean_squared_error
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
