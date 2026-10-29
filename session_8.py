import pandas as pd

# ---------------------------------------------------
# 1. Find duplicate orders (restaurant name + date)
# ---------------------------------------------------
# Real data: orders = pd.read_csv("zomato_orders.csv")
orders = pd.DataFrame({
    "restaurant": ["Spice Hub", "Pizza Point", "Spice Hub", "Cafe Mocha", "Pizza Point", "Spice Hub"],
    "order_date": ["2026-10-01", "2026-10-02", "2026-10-01", "2026-10-03", "2026-10-05", "2026-10-07"],
    "amount": [450, 300, 450, 220, 310, 500],
})

dup_mask = orders.duplicated(subset=["restaurant", "order_date"], keep=False)
print("Q1. All rows involved in duplicates:")
print(orders[dup_mask])

print("\nRepeat entries only (keep='first'):")
print(orders[orders.duplicated(subset=["restaurant", "order_date"])])


# ---------------------------------------------------
# 2. Most repeated Flipkart reviews with value_counts()
# ---------------------------------------------------
reviews = pd.DataFrame({
    "review": [
        "Great product", "Bad quality", "Great product", "Value for money",
        "Great product", "Bad quality", "Value for money", "Value for money",
        "Value for money", "Average", "Bad quality", "Superb",
    ]
})

counts = reviews["review"].value_counts()
top3_duplicates = counts[counts > 1].head(3)
print("\nQ2. Top 3 repeated reviews:")
print(top3_duplicates)


# ---------------------------------------------------
# 3. Remove duplicate Spotify playlists
# ---------------------------------------------------
playlists = pd.DataFrame({
    "playlist_name": ["Chill Vibes", "Workout Mix", "Chill Vibes", "Road Trip", "Workout Mix", "Road Trip"],
    "creator": ["amit_99", "riya_k", "amit_99", "karan_s", "riya_k", "neha_m"],
})

clean_playlists = playlists.drop_duplicates().reset_index(drop=True)
print("\nQ3. Cleaned playlists:")
print(clean_playlists)


# ---------------------------------------------------
# 4. Standardize Instagram username typos with replace()
# ---------------------------------------------------
insta = pd.DataFrame({
    "username": ["insta_queen", "insta-queen", "instaqueen", "travel_guy", "insta_queen"]
})

insta["username"] = insta["username"].replace(
    ["insta_queen", "insta-queen"], "instaqueen"
)
print("\nQ4. Standardized usernames:")
print(insta)


# ---------------------------------------------------
# 5. Unify payment status to 1 / 0
# ---------------------------------------------------
pay = pd.DataFrame({
    "paid": ["Yes", "yes", "Y", "No", "no", "N", "  yes ", " N  ", "YES"]
})

pay["paid"] = (
    pay["paid"]
    .str.strip()
    .str.lower()
    .map({"yes": 1, "y": 1, "no": 0, "n": 0})
)
print("\nQ5. Unified payment status:")
print(pay)
print(pay["paid"].dtype)