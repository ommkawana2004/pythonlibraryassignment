import numpy as np

# ---------------------------------------------------
# 1. 2D array of Zomato ratings (4 users x 5 food items)
# ---------------------------------------------------
ratings = np.array([
    [4, 5, 3, 4, 2],   # User 1
    [5, 4, 4, 3, 5],   # User 2
    [3, 4, 5, 2, 4],   # User 3
    [4, 3, 2, 5, 4]    # User 4
])

# Slicing: rows 1 and 2 (second and third users)
second_third_users = ratings[1:3]
print("Q1. Ratings by 2nd and 3rd users:")
print(second_third_users)


# ---------------------------------------------------
# 2. Boolean indexing: days with steps > 8000
# ---------------------------------------------------
steps = np.array([7500, 8200, 9000, 6800, 10500, 7900, 8800, 5000, 9500, 8100])

active_days = steps[steps > 8000]
print("\nQ2. Days with steps > 8000:")
print(active_days)


# ---------------------------------------------------
# 3. Fancy indexing: IPL scores from matches 2, 5, 7
# ---------------------------------------------------
scores = np.array([180, 165, 200, 150, 175, 190, 210, 160])

# Matches are numbered 1-8, so subtract 1 for zero-based indices
selected_scores = scores[[1, 4, 6]]
print("\nQ3. Scores from matches 2, 5 and 7:")
print(selected_scores)


# ---------------------------------------------------
# 4. Broadcasting: 10% discount on Flipkart prices (no loops)
# ---------------------------------------------------
prices = np.array([1500, 2500, 999, 4999, 750])

discounted_prices = prices * 0.90   # scalar broadcast to every element
print("\nQ4. Prices after 10% discount:")
print(discounted_prices)


# ---------------------------------------------------
# 5. Boolean masking: set negative Spotify ratings to 0
# ---------------------------------------------------
song_ratings = np.array([4, -2, 0, 5, -1, 3, -4, 2])

song_ratings[song_ratings < 0] = 0
print("\nQ5. Ratings after replacing negatives with 0:")
print(song_ratings)