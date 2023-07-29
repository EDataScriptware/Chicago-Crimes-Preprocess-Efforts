import json
import numpy as np
import random

def apply_dropout(product_prices, dropout_rate):
    num_samples = len(product_prices)
    num_drop = int(dropout_rate * num_samples)
    drop_indices = random.sample(range(num_samples), num_drop)
    for idx in drop_indices:
        product_prices[idx] = 0.0
    return product_prices


# Load incoming data from JSON
data = json.load(open('input.json'))

# Extract the product prices as an array
product_prices = np.array([product["price"] for product in data["products"]])

# Set the dropout rate (0.2 means 20% of the prices will be set to zero :/ )
dropout_rate = 0.2

# Apply dropout normalization to the product prices
normalized_prices = apply_dropout(product_prices.copy(), dropout_rate)

# Update the normalized prices back to the data dictionary
for i, product in enumerate(data["products"]):
    product["normalized_price"] = float(normalized_prices[i])

# Display the updated data with dropout normalization applied
json.dump(data, open('dropout_normalization_output.json', 'w'), indent=4)