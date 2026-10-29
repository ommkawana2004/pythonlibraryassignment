import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------
# 1. 2x2 grid: line, bar, scatter, pie
# ---------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
axes[0, 0].plot(days, [5, 7, 6, 9, 8], marker="o", color="teal")
axes[0, 0].set_title("Line: Daily Orders")

axes[0, 1].bar(["Swiggy", "Zomato", "Domino's"], [12, 15, 7], color=["orange", "red", "blue"])
axes[0, 1].set_title("Bar: Orders by App")

axes[1, 0].scatter([4.2, 4.5, 3.9, 4.1, 4.4], [400, 600, 350, 300, 450], color="purple")
axes[1, 0].set_title("Scatter: Rating vs Price")
axes[1, 0].set_xlabel("Rating")
axes[1, 0].set_ylabel("Price (₹)")

axes[1, 1].pie([40, 30, 20, 10], labels=["Pizza", "Biryani", "Burger", "Dosa"], autopct="%1.1f%%")
axes[1, 1].set_title("Pie: Favourite Food")

fig.tight_layout()
plt.show()


# ---------------------------------------------------
# 2. Delivery time bars with different color, linestyle, linewidth
# ---------------------------------------------------
apps = ["Zomato", "Swiggy", "Domino's"]
times = [32, 28, 25]                     # minutes
colors = ["red", "orange", "blue"]
linestyles = ["-", "--", ":"]
linewidths = [2, 3, 4]

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(apps, times, color=colors, alpha=0.6)

for bar, ls, lw, c in zip(bars, linestyles, linewidths, colors):
    bar.set_edgecolor(c)
    bar.set_linestyle(ls)
    bar.set_linewidth(lw)
    bar.set_facecolor(c)
    bar.set_alpha(0.5)

ax.set_title("Average Delivery Time")
ax.set_xlabel("Platform")
ax.set_ylabel("Minutes")
plt.show()


# ---------------------------------------------------
# 3. Multi-axis chart: followers (left) and daily posts (right)
# ---------------------------------------------------
influencers = ["Inf A", "Inf B", "Inf C", "Inf D", "Inf E"]
followers = [1.2, 3.4, 0.8, 5.6, 2.1]     # in millions
posts = [2.5, 1.2, 3.0, 0.8, 1.8]

fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.plot(influencers, followers, color="royalblue", marker="o", linewidth=2)
ax1.set_xlabel("Influencer")
ax1.set_ylabel("Followers (millions)", color="royalblue")
ax1.tick_params(axis="y", labelcolor="royalblue")

ax2 = ax1.twinx()                         # second y-axis on the right
ax2.plot(influencers, posts, color="crimson", marker="s", linestyle="--", linewidth=2)
ax2.set_ylabel("Avg Daily Posts", color="crimson")
ax2.tick_params(axis="y", labelcolor="crimson")

ax1.set_title("Followers vs Daily Posting Frequency")
fig.tight_layout()
plt.show()


# ---------------------------------------------------
# 4. Scatter: tickets sold vs IMDb rating, with movie names
# ---------------------------------------------------
movies = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]
tickets = [2.5, 4.1, 1.8, 3.3, 5.0]       # in millions
imdb = [7.2, 8.1, 6.5, 7.8, 8.4]

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(tickets, imdb, color="darkorange", s=100, edgecolors="black")

for name, x, y in zip(movies, tickets, imdb):
    ax.annotate(name, (x, y), textcoords="offset points", xytext=(0, 10), ha="center")

ax.set_title("Tickets Sold vs IMDb Rating")
ax.set_xlabel("Tickets Sold (millions)")
ax.set_ylabel("IMDb Rating")
ax.set_ylim(6, 9)
plt.show()


# ---------------------------------------------------
# 5. Annotate peak sales as 'Big Billion Days'
# ---------------------------------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [120, 110, 130, 125, 140, 135, 150, 145, 160, 320, 210, 180]   # ₹ crore

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(months, sales, marker="o", color="navy")

peak_idx = int(np.argmax(sales))
ax.annotate(
    "Big Billion Days",
    xy=(months[peak_idx], sales[peak_idx]),
    xytext=(months[peak_idx - 3], sales[peak_idx] - 30),
    arrowprops=dict(facecolor="red", shrink=0.05, width=2),
    fontsize=12, fontweight="bold", color="red",
)

ax.set_title("Flipkart Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (₹ crore)")
ax.grid(True, alpha=0.3)
plt.show()