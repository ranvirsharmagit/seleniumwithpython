import pandas as pd

# Load the uploaded historical stock price data
file_path = '/Users/ranvirkumarsharma/Downloads/Quote-Equity-AWFIS-EQ-05-07-2024-to-05-08-2024.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data to understand its structure
data.head()

# Preprocess the data
data['Date'] = pd.to_datetime(data['Date'], format('%D-%M-%Y'))
#data['Date'] = pd.to_datetime(data['Date'], format='%D-%M-%Y')
data.set_index('Date', inplace=True)
data = data[['close']]

# Plot the historical data
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(data)
plt.title('Historical Stock Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()

# Display the first few rows of the processed data
data.head()


# Inspect the columns of the dataset
data.columns
