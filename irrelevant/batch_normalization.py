import json
import numpy as np

# Load incoming data from JSON
data = json.load(open('input.json'))

# Extract the product prices as an array
prices = np.array([product["price"] for product in data["products"]])

# Calculate the mean and standard deviation of the prices
mean = np.mean(prices)
std = np.std(prices)

# Batch normalize the prices
normalized_prices = (prices - mean) / std

# Update the normalized prices back to the data dictionary
for i, product in enumerate(data["products"]):
    product["normalized_price"] = float(normalized_prices[i])

# Display the updated data with batch normalization applied
json.dump(data, open('batch_normalization_output.json', 'w'), indent=4)
