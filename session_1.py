# pip install numpy

import numpy as np

# ---------------------------------------------------
# 2. Instagram influencer followers
# ---------------------------------------------------
followers = np.array([1200, 15000, 67000, 340000, 1250000])

print("Q2. Followers array:", followers)
print("Shape:", followers.shape)
print("Number of dimensions:", followers.ndim)
print("Data type:", followers.dtype)


# ---------------------------------------------------
# 3. Zomato order IDs using np.arange()
# ---------------------------------------------------
order_ids = np.arange(101, 111)   # 10 values: 101 to 110

print("\nQ3. Order IDs:", order_ids)
print("Size:", order_ids.size)


# ---------------------------------------------------
# 4. 3x3 identity matrix using np.eye()
# ---------------------------------------------------
like_matrix = np.eye(3)

print("\nQ4. Like identity matrix:")
print(like_matrix)

# The diagonal values (1s) represent each playlist item "liking" itself,
# i.e. a self-like. The off-diagonal values (0s) mean no likes between
# different items.


# ---------------------------------------------------
# 5. Cricket scores: memory per element
# ---------------------------------------------------
scores_list = [45, 67, 120, 89, 54]
scores = np.array(scores_list)

print("\nQ5. Scores array:", scores)
print("Bytes per score:", scores.itemsize)