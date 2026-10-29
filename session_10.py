# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------
# 1. Line plot of daily steps (last 7 days), saved as PNG
# ---------------------------------------------------
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [6500, 8200, 7400, 9100, 5800, 10500, 7200]

plt.figure(figsize=(7, 4))
plt.plot(days, steps, marker="o", color="green")
plt.title("Daily Steps - Last 7 Days")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.grid(True, alpha=0.3)
plt.savefig("steps_lineplot.png", dpi=150, bbox_inches="tight")
plt.show()


# ---------------------------------------------------
# 2. Scatter plot: Zomato rating vs average meal price
# ---------------------------------------------------
restaurants = ["Spice Hub", "Tandoor Town", "Pizza Point", "Cafe Mocha", "Biryani House",
               "Dosa Corner", "Thali Palace", "Burger Barn", "Chaat Center", "Sushi Spot"]
ratings = [4.2, 4.5, 3.9, 4.1, 4.4, 4.0, 4.3, 3.8, 4.1, 4.6]
avg_price = [400, 600, 350, 300, 450, 200, 380, 250, 150, 900]

plt.figure(figsize=(7, 5))
plt.scatter(ratings, avg_price, color="tomato", s=80, edgecolors="black")
plt.title("Zomato Rating vs Average Meal Price (Rajkot)")
plt.xlabel("Zomato Rating")
plt.ylabel("Average Meal Price for One (₹)")
plt.grid(True, alpha=0.3)
plt.show()


# ---------------------------------------------------
# 3. Bar chart: orders per platform, different colors + legend
# ---------------------------------------------------
platforms = ["Swiggy", "Zomato", "Domino's"]
orders = [8, 12, 5]
colors = ["orange", "red", "blue"]

plt.figure(figsize=(6, 4))
bars = plt.bar(platforms, orders, color=colors)
plt.title("Orders Placed Last Month")
plt.xlabel("Platform")
plt.ylabel("Number of Orders")
plt.legend(bars, platforms, title="Platform")   # one legend entry per bar
plt.show()


# ---------------------------------------------------
# 4. Histogram of Spotify session durations (5 bins)
# ---------------------------------------------------
durations = [12, 25, 38, 45, 18, 60, 33, 27, 52, 41,
             15, 30, 48, 22, 36, 55, 29, 43, 20, 35]   # 20 sessions, minutes

plt.figure(figsize=(6, 4))
plt.hist(durations, bins=5, color="mediumseagreen", edgecolor="black")
plt.title("Spotify Listening Session Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Sessions")
plt.show()


# ---------------------------------------------------
# 5. Two subplots: screen time (line) and likes (bar)
# ---------------------------------------------------
screen_time = [1.5, 2.0, 1.2, 2.8, 3.1, 4.0, 3.5]    # hours
likes = [20, 35, 15, 40, 55, 70, 60]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7))

ax1.plot(days, screen_time, marker="o", color="purple")
ax1.set_title("Daily Instagram Screen Time")
ax1.set_xlabel("Day")
ax1.set_ylabel("Hours")
ax1.grid(True, alpha=0.3)

ax2.bar(days, likes, color="deeppink")
ax2.set_title("Posts Liked Per Day")
ax2.set_xlabel("Day")
ax2.set_ylabel("Number of Likes")

fig.tight_layout()                         # stops titles and labels overlapping
fig.savefig("social_media_usage.png", dpi=150)
plt.show()