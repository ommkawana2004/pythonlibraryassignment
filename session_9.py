import pandas as pd
import numpy as np

# ---------------------------------------------------
# 1. Convert delivery timestamp strings to datetime
# ---------------------------------------------------
timestamps = ['2024-06-01 14:30', '2024-06-02 09:15', '2024-06-03 20:45']
delivery_times = pd.to_datetime(timestamps)
print("Q1.")
print(delivery_times)


# ---------------------------------------------------
# 2. Extract year, month, weekday from order_date
# ---------------------------------------------------
# Real data: df = pd.read_csv("orders.csv")
df = pd.DataFrame({
    "order_date": [
        "2024-06-01 10:15:00", "2024-06-02 18:40:00", "2024-06-04 12:05:00",
        "2024-06-07 21:30:00", "2024-06-09 09:00:00", "2024-06-10 15:20:00",
        "2024-06-15 11:45:00", "2024-06-16 19:10:00", "2024-06-18 13:25:00",
    ],
    "amount": [450, 300, 220, 510, 180, 640, 275, 390, 330],
})

df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d %H:%M:%S")
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["weekday"] = df["order_date"].dt.day_name()   # use .dt.weekday for 0-6 numbers
print("\nQ2.")
print(df)


# ---------------------------------------------------
# 3. Set order_date as index and count orders per week
# ---------------------------------------------------
df_indexed = df.set_index("order_date")
weekly_orders = df_indexed.resample("W").size()
print("\nQ3. Orders per week:")
print(weekly_orders)


# ---------------------------------------------------
# 4. Convert UTC timestamps to Asia/Kolkata
# ---------------------------------------------------
posts = pd.DataFrame({
    "posted_at": pd.to_datetime([
        "2024-06-01 00:00:00", "2024-06-01 06:30:00", "2024-06-01 12:15:00",
        "2024-06-01 18:45:00", "2024-06-02 03:20:00", "2024-06-02 09:00:00",
    ])
})

posts["posted_at"] = posts["posted_at"].dt.tz_localize("UTC")    # mark as UTC
posts["posted_at_ist"] = posts["posted_at"].dt.tz_convert("Asia/Kolkata")
print("\nQ4.")
print(posts[["posted_at", "posted_at_ist"]].head())


# ---------------------------------------------------
# 5. is_weekend feature
# ---------------------------------------------------
df["is_weekend"] = df["order_date"].dt.weekday >= 5     # 5 = Saturday, 6 = Sunday
# Equivalent with numpy: np.isin(df["order_date"].dt.weekday, [5, 6])
print("\nQ5.")
print(df[["order_date", "weekday", "is_weekend"]])