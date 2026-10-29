import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
sns.set_theme(style="whitegrid")

# ---------------------------------------------------
# 1. Univariate analysis of 'total_runs' (IPL)
# ---------------------------------------------------
# Real data: ipl = pd.read_csv("ipl_matches.csv")
ipl = pd.DataFrame({
    "match_id": range(1, 21),
    "total_runs": rng.integers(250, 420, size=20),
})

col = ipl["total_runs"]
print("Q1.")
print("Mean  :", round(col.mean(), 2))
print("Median:", col.median())
print("Min   :", col.min())
print("Max   :", col.max())
print("Std   :", round(col.std(), 2))
# Shortcut: print(col.describe())


# ---------------------------------------------------
# 2. Bar plot: count of reviews per rating (Flipkart)
# ---------------------------------------------------
reviews = pd.DataFrame({
    "rating": rng.choice([1, 2, 3, 4, 5], size=200, p=[0.08, 0.07, 0.15, 0.30, 0.40]),
    "category": rng.choice(["Mobiles", "Laptops", "Fashion"], size=200),
})

plt.figure(figsize=(6, 4))
sns.countplot(data=reviews, x="rating", hue="rating", palette="viridis",
              order=[1, 2, 3, 4, 5], legend=False)
plt.title("Number of Reviews per Rating")
plt.xlabel("Rating (stars)")
plt.ylabel("Number of Reviews")
plt.show()


# ---------------------------------------------------
# 3. Scatterplot: cost for two vs user rating (Zomato)
# ---------------------------------------------------
cost = rng.integers(200, 2000, size=60)
zomato = pd.DataFrame({
    "average_cost_for_two": cost,
    "user_rating": np.clip(3.2 + cost / 2000 + rng.normal(0, 0.3, size=60), 1, 5).round(1),
})

plt.figure(figsize=(7, 5))
sns.scatterplot(data=zomato, x="average_cost_for_two", y="user_rating", color="tomato")
plt.title("Cost for Two vs User Rating")
plt.xlabel("Average Cost for Two (₹)")
plt.ylabel("User Rating")
plt.show()


# ---------------------------------------------------
# 4. groupby: average box office collection per genre
# ---------------------------------------------------
movies = pd.DataFrame({
    "genre": ["Action", "Comedy", "Drama", "Action", "Thriller", "Comedy",
              "Drama", "Action", "Thriller", "Romance", "Romance", "Drama"],
    "box_office_collection": [450, 180, 120, 600, 250, 210, 90, 380, 300, 150, 170, 130],  # ₹ crore
})

genre_avg = (
    movies.groupby("genre")["box_office_collection"]
    .mean()
    .sort_values(ascending=False)
    .reset_index(name="avg_box_office_cr")
)
print("\nQ4. Average box office by genre:")
print(genre_avg)


# ---------------------------------------------------
# 5. Pairplot on Spotify song features
# ---------------------------------------------------
n = 150
danceability = rng.uniform(0.2, 0.95, n)
energy = np.clip(0.5 * danceability + rng.normal(0.3, 0.15, n), 0, 1)
valence = np.clip(0.6 * energy + rng.normal(0.15, 0.15, n), 0, 1)
popularity = np.clip(30 + 40 * danceability + rng.normal(0, 10, n), 0, 100)

spotify = pd.DataFrame({
    "danceability": danceability,
    "energy": energy,
    "valence": valence,
    "popularity": popularity,
})

sns.pairplot(spotify, corner=False)
plt.suptitle("Spotify Audio Features: Pairwise Relationships", y=1.02)
plt.show()