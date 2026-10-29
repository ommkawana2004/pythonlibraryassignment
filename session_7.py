import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------
# 1. Detect outliers in 'user_rating' using the IQR method
# ---------------------------------------------------
zomato = pd.DataFrame({
    "user_rating": [4.2, 4.5, 3.9, 4.1, 4.4, 1.0, 4.0, 4.3, 5.0, 0.5]
})
# Real data: zomato = pd.read_csv("zomato_ratings.csv")

q1 = zomato["user_rating"].quantile(0.25)
q3 = zomato["user_rating"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = zomato[(zomato["user_rating"] < lower) | (zomato["user_rating"] > upper)]
print("Q1.")
print(f"Q1={q1}, Q3={q3}, IQR={iqr:.3f}, bounds=({lower:.3f}, {upper:.3f})")
print("Outlier indices:", outliers.index.tolist())


# ---------------------------------------------------
# 2. Boxplot of 'order_amount'
# ---------------------------------------------------
swiggy = pd.DataFrame({
    "order_amount": [250, 300, 280, 350, 400, 320, 290, 310, 2500, 270, 330, 3000]
})

plt.figure(figsize=(6, 5))
plt.boxplot(swiggy["order_amount"])
plt.title("Swiggy Order Amount Distribution")
plt.xlabel("Orders")
plt.ylabel("Order Amount (₹)")
plt.show()   # the circles above the whisker are the outliers (2500 and 3000)


# ---------------------------------------------------
# 3. Winsorization at the 5th and 95th percentiles
# ---------------------------------------------------
paytm = pd.DataFrame({
    "transaction_amount": [100, 150, 200, 250, 300, 350, 400, 450, 500, 5000]
})

low = paytm["transaction_amount"].quantile(0.05)
high = paytm["transaction_amount"].quantile(0.95)

print("\nQ3. Before:")
print(paytm["transaction_amount"].describe())

paytm["transaction_amount"] = paytm["transaction_amount"].clip(lower=low, upper=high)

print("\nAfter winsorization:")
print(paytm["transaction_amount"].describe())


# ---------------------------------------------------
# 4. Convert price strings like '₹1,299' to numbers
# ---------------------------------------------------
flipkart = pd.DataFrame({
    "price": ["₹1,299", "₹24,999", "₹499", "₹1,05,000"]
})

flipkart["price"] = (
    flipkart["price"]
    .str.replace(r"[^\d.]", "", regex=True)   # remove everything except digits and dot
    .astype(float)
)
print("\nQ4.")
print(flipkart)
print(flipkart["price"].dtype)


# ---------------------------------------------------
# 5. Convert a mixed-type 'is_premium' column to boolean
# ---------------------------------------------------
spotify = pd.DataFrame({
    "is_premium": [True, "True", 1, "yes", "no", 0, False, "False", None, "YES"]
})

true_values = {"true", "1", "1.0", "yes"}

spotify["is_premium"] = (
    spotify["is_premium"]
    .astype(str)          # make everything a string
    .str.strip()
    .str.lower()          # handle 'YES', 'True', etc.
    .isin(true_values)    # True only for the accepted values
)
print("\nQ5.")
print(spotify)
print(spotify["is_premium"].dtype)