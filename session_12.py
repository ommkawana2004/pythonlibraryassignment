# pip install seaborn

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# ---------------------------------------------------
# 1. Histplot: delivery times of 50 Zomato orders
# ---------------------------------------------------
delivery_times = rng.normal(loc=32, scale=7, size=50).round(1)   # minutes

plt.figure(figsize=(7, 4))
sns.histplot(delivery_times, bins=10, kde=True, color="tomato")
plt.title("Zomato Delivery Time Distribution")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Number of Orders")
plt.show()


# ---------------------------------------------------
# 2. Boxplot: total bill by day (tips dataset)
# ---------------------------------------------------
tips = sns.load_dataset("tips")     # needs internet the first time

plt.figure(figsize=(7, 5))
sns.boxplot(data=tips, x="day", y="total_bill", hue="day", palette="Set2", legend=False)
plt.title("Total Bill by Day of the Week")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()


# ---------------------------------------------------
# 3. Violinplot: IPL scores for 8 teams, 'darkgrid' theme
# ---------------------------------------------------
sns.set_theme(style="darkgrid")

teams = ["CSK", "MI", "RCB", "KKR", "DC", "SRH", "RR", "PBKS"]
ipl = pd.DataFrame({
    "team": np.repeat(teams, 15),
    "runs": np.concatenate([rng.normal(loc=rng.integers(155, 185), scale=20, size=15)
                            for _ in teams]).round(0),
})

plt.figure(figsize=(10, 5))
sns.violinplot(data=ipl, x="team", y="runs", hue="team", palette="muted", legend=False)
plt.title("IPL Run Distribution by Team")
plt.xlabel("Team")
plt.ylabel("Runs Scored")
plt.show()


# ---------------------------------------------------
# 4. Countplot: songs per genre (40 tracks, 5 genres)
# ---------------------------------------------------
genres = ["Pop", "Rock", "Bollywood", "Hip-Hop", "Classical"]
songs = pd.DataFrame({
    "genre": rng.choice(genres, size=40, p=[0.3, 0.2, 0.3, 0.15, 0.05])
})

plt.figure(figsize=(7, 4))
sns.countplot(data=songs, x="genre", hue="genre", palette="viridis",
              order=songs["genre"].value_counts().index, legend=False)
plt.title("Number of Songs per Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Songs")
plt.show()


# ---------------------------------------------------
# 5. KDE plot: daily steps for a week, 'whitegrid' theme
# ---------------------------------------------------
sns.set_theme(style="whitegrid")

steps = [6500, 8200, 7400, 9100, 5800, 10500, 7200]

plt.figure(figsize=(7, 4))
sns.kdeplot(steps, color="seagreen", fill=True, linewidth=2)
plt.title("Distribution of Daily Step Counts")
plt.xlabel("Steps per Day")
plt.ylabel("Density")
plt.show()