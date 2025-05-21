import pandas as pd
import random
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define constants
num_rows = 3000  # Number of rows of data
regions = ['North', 'South', 'East', 'West']
categories = {
    'Electronics': ['Smartphone', 'Laptop', 'Smart Watch', 'Tablet', 'Headphones'],
    'Clothing': ['T-shirt', 'Jeans', 'Jacket', 'Sneakers', 'Hat'],
    'Home & Kitchen': ['Blender', 'Microwave', 'Vacuum Cleaner', 'Lamp', 'Chair'],
    'Sports': ['Football', 'Tennis Racket', 'Basketball', 'Yoga Mat', 'Dumbbells'],
    'Books': ['Fiction', 'Biography', 'Science', 'History', 'Children']
}
payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery']

# Generate data
data = []
for i in range(1001, 1001 + num_rows):
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(10, 500), 2)
    cost = round(unit_price * random.uniform(0.5, 0.9), 2)
    
    data.append({
        'Order ID': i,
        'Order Date': fake.date_between(start_date='-1y', end_date='today'),
        'Customer ID': f'C{random.randint(1000, 2000)}',
        'Region': random.choice(regions),
        'Product Category': category,
        'Product Name': product,
        'Quantity': quantity,
        'Unit Price': unit_price,
        'Cost': cost,
        'Payment Method': random.choice(payment_methods)
    })

df = pd.DataFrame(data)

# Save as CSV file
file_path = 'ecommerce_sales.csv'
df.to_csv(file_path, index=False)

print(f"Generated data saved to {file_path}")
