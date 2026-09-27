import pandas as pd
import numpy as np

np.random.seed(42)
n_rows = 1500

sub_categories = {
    'Clothing': ['Saree', 'Trousers', 'Shirt', 'Dress'],
    'Electronics': ['Printers', 'Accessories', 'Phones', 'Laptops'],
    'Furniture': ['Bookcases', 'Tables', 'Chairs', 'Furnishings']
}

payment_modes = ['COD', 'Credit Card', 'UPI', 'Debit Card', 'Net Banking']
customer_names = [
    'Vrinda', 'Yogesh', 'Yohann', 'Yash', 'Yaanvi', 
    'Wale', 'Priya', 'Rohan', 'Ananya', 'Kartik', 'Sneha', 'Arjun'
]

months = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]

records = []
for i in range(n_rows):
    cat = np.random.choice(list(sub_categories.keys()), p=[0.45, 0.35, 0.20])
    sub_cat = np.random.choice(sub_categories[cat])
    pay_mode = np.random.choice(payment_modes, p=[0.40, 0.25, 0.15, 0.12, 0.08])
    cust = np.random.choice(customer_names)
    month_idx = np.random.randint(0, 12)
    month = months[month_idx]
    
    quarter = f"Qtr {month_idx // 3 + 1}"
    qty = np.random.randint(1, 6)
    
    if cat == 'Electronics':
        amount = np.random.randint(1500, 12000)
    elif cat == 'Furniture':
        amount = np.random.randint(2000, 15000)
    else:
        amount = np.random.randint(400, 3500)
    
    margin = np.random.uniform(0.05, 0.28)
    if month in ['May', 'July', 'December'] and np.random.rand() > 0.45:
        profit = -1 * round(amount * np.random.uniform(0.04, 0.15), 2)
    else:
        profit = round(amount * margin, 2)
        
    records.append({
        'OrderID': f"ORD-{1000 + i}",
        'CustomerName': cust,
        'Category': cat,
        'Sub-Category': sub_cat,
        'Amount': amount,
        'Profit': profit,
        'Quantity': qty,
        'PaymentMode': pay_mode,
        'Month': month,
        'Quarter': quarter
    })

df = pd.DataFrame(records)
output_csv = "Ecommerce_Sales_Data.csv"
df.to_csv(output_csv, index=False)
print(f"SUCCESS: Generated {len(df)} transactions in '{output_csv}'")