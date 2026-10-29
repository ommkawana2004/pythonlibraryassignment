import numpy as np

# ---------------------------------------------------
# 1. Step counts of two friends over a week
# ---------------------------------------------------
friend_a = np.array([5000, 7500, 8200, 6000, 9000, 10000, 4000])
friend_b = np.array([6000, 7000, 8000, 6500, 8500, 9500, 5000])

print("Q1.")
print("Addition      :", friend_a + friend_b)   # combined steps per day
print("Subtraction   :", friend_a - friend_b)   # positive = A walked more
print("Multiplication:", friend_a * friend_b)
print("Division      :", np.round(friend_a / friend_b, 2))  # ratio > 1 = A more active


# ---------------------------------------------------
# 2. Spotify recommendations: dot() vs matmul()
# ---------------------------------------------------
user_pref = np.array([[5, 3, 2],
                      [4, 4, 1],
                      [2, 5, 3]])

song_pop = np.array([[1, 2, 0],
                     [3, 1, 2],
                     [0, 4, 1]])

rec_dot = np.dot(user_pref, song_pop)
rec_matmul = np.matmul(user_pref, song_pop)

print("\nQ2. Recommendation matrix using dot():")
print(rec_dot)
print("Recommendation matrix using matmul():")
print(rec_matmul)
print("Same result?", np.array_equal(rec_dot, rec_matmul))

# Difference shows up with 3D (stacked) arrays
a = np.ones((2, 2, 2))
b = np.ones((2, 2, 2))
print("dot shape   :", np.dot(a, b).shape)      # (2, 2, 2, 2)
print("matmul shape:", np.matmul(a, b).shape)   # (2, 2, 2)


# ---------------------------------------------------
# 3. Instagram image brightness (4x4)
# ---------------------------------------------------
image = np.array([[ 10,  20,  30,  40],
                  [ 50,  60,  70,  80],
                  [ 90, 100, 110, 120],
                  [130, 140, 150, 160]])

image_t = image.T
print("\nQ3. Transposed image:")
print(image_t)
print("Mean     :", np.mean(image_t))
print("Median   :", np.median(image_t))
print("Std Dev  :", np.std(image_t))
print("Variance :", np.var(image_t))


# ---------------------------------------------------
# 4. Zomato rating correlation grid (3x3)
# ---------------------------------------------------
corr = np.array([[1.0, 0.6, 0.3],
                 [0.6, 1.0, 0.5],
                 [0.3, 0.5, 1.0]])

det = np.linalg.det(corr)
print("\nQ4. Determinant:", round(det, 4))

if det != 0:   # invertible only if det is not zero
    inverse = np.linalg.inv(corr)
    print("Inverse:\n", np.round(inverse, 4))

eigenvalues, eigenvectors = np.linalg.eig(corr)
print("Eigenvalues:", np.round(eigenvalues, 4))
print("Eigenvectors (columns):\n", np.round(eigenvectors, 4))


# ---------------------------------------------------
# 5. Swiggy orders: 2 cities x 6 days
# ---------------------------------------------------
orders = np.array([[120, 135, 150, 160, 145, 170],
                   [ 90, 100, 110,  95, 105, 115]])

reshaped = orders.reshape(3, 4)
flat = reshaped.flatten()
part1, part2 = np.split(flat, 2)
stacked = np.vstack((part1, part2))

print("\nQ5. Reshaped (3,4):\n", reshaped)
print("Flattened:", flat)
print("Part 1:", part1)
print("Part 2:", part2)
print("Vertically stacked:\n", stacked)