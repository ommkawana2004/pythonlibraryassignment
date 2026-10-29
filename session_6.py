import pandas as pd
import numpy as np

# ---------------------------------------------------
# 1. Load IPL player stats and count missing values
# ---------------------------------------------------
# Sample file (replace with your downloaded CSV, e.g. pd.read_csv("ipl_players.csv"))
pd.DataFrame({
    "player": ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "KL Rahul",
               "Hardik Pandya", "Ravindra Jadeja", "Jasprit Bumrah", "Shubman Gill"],
    "runs": [7263, 6211, np.nan, 4689, 2525, np.nan, 56, 3200],
    "matches": [237, 243, 250, np.nan, 123, 226, 120, 100],
    "strike_rate": [130.4, 130.8, 135.9, 134.6, np.nan, 127.6, 70.0, 135.0],
}).to_csv("ipl_players.csv", index=False)

df = pd.read_csv("ipl_players.csv")
print("Q1. Data:")
print(df)
print("\nMissing values per column (isnull):")
print(df.isnull().sum())
print("\nNon-missing values per column (notnull):")
print(df.notnull().sum())


# ---------------------------------------------------
# 2. dropna(axis=0, how='any') and compare shapes
# ---------------------------------------------------
print("\nQ2. Shape before dropping:", df.shape)
df_dropped = df.dropna(axis=0, how="any")
print("Shape after dropping:", df_dropped.shape)
print(df_dropped)


# ---------------------------------------------------
# 3. Fill missing 'runs' with the column mean
# ---------------------------------------------------
df_filled = df.copy()
df_filled["runs"] = df_filled["runs"].fillna(df_filled["runs"].mean())
print("\nQ3. Runs column after fillna(mean):")
print(df_filled["runs"])


# ---------------------------------------------------
# 4. Zomato ratings: forward fill, then backward fill
# ---------------------------------------------------
ratings = pd.DataFrame({
    "restaurant": [f"Restaurant {i}" for i in range(1, 9)],
    "rating": [np.nan, 4.2, np.nan, np.nan, 3.8, 4.5, np.nan, 4.0],
})

print("\nQ4. Before:")
print(ratings)

ratings["rating_filled"] = ratings["rating"].ffill()           # forward fill
print("\nAfter ffill (first value still missing):")
print(ratings[["restaurant", "rating_filled"]])

ratings["rating_filled"] = ratings["rating_filled"].bfill()    # backward fill leftovers
print("\nAfter ffill + bfill:")
print(ratings)