# pip install ydata-profiling sweetviz dtale

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

# ---------------------------------------------------
# 1. Profile report: Spotify Top 100 Songs
# ---------------------------------------------------
# Real data: spotify = pd.read_csv("spotify_top100.csv")
n = 100
spotify = pd.DataFrame({
    "track_name": [f"Song {i}" for i in range(n)],
    "artist": rng.choice(["Arijit Singh", "Taylor Swift", "Drake", "Dua Lipa", "Badshah"], n),
    "danceability": rng.uniform(0.3, 0.95, n).round(2),
    "popularity": rng.integers(60, 100, n).astype(float),
    "duration": [f"{rng.integers(2, 5)}:{rng.integers(10, 59)}" for _ in range(n)],  # text, not numeric
})
spotify.loc[rng.choice(n, 8, replace=False), "popularity"] = np.nan   # missing values

from ydata_profiling import ProfileReport

profile = ProfileReport(spotify, title="Spotify Top 100 Profile")
profile.to_file("spotify_profile.html")        # open this file in your browser
print("Missing values per column:\n", spotify.isnull().sum())
print("\nData types:\n", spotify.dtypes)


# ---------------------------------------------------
# 2. Sweetviz: compare Mumbai vs Delhi Zomato data
# ---------------------------------------------------
import sweetviz as sv

def make_city(cost_mean, rating_mean):
    return pd.DataFrame({
        "cost_for_two": rng.normal(cost_mean, 200, 150).round(-1).clip(100),
        "rating": rng.normal(rating_mean, 0.4, 150).clip(1, 5).round(1),
        "online_order": rng.choice(["Yes", "No"], 150),
    })

mumbai = make_city(900, 4.0)      # real data: pd.read_csv("zomato_mumbai.csv")
delhi = make_city(700, 3.8)       # real data: pd.read_csv("zomato_delhi.csv")

report = sv.compare([mumbai, "Mumbai"], [delhi, "Delhi"])   # compare() for two datasets
report.show_html("zomato_mumbai_vs_delhi.html")             # analyze(df) is for one dataset


# ---------------------------------------------------
# 3. D-Tale: filter Myntra products with price > 2000
# ---------------------------------------------------
import dtale

myntra = pd.DataFrame({
    "product": [f"Item {i}" for i in range(200)],
    "brand": rng.choice(["Roadster", "HRX", "Puma", "Nike", "Biba"], 200),
    "price": rng.integers(299, 6000, 200),
})  # real data: pd.read_csv("myntra.csv")

print("Products with price > 2000:", (myntra["price"] > 2000).sum())   # cross-check count

d = dtale.show(myntra)     # prints a link (usually http://localhost:40000) to open in the browser
# In the browser: top-left menu > "Custom Filter" > type  price > 2000  > Apply
# The row count appears at the top of the grid. Take your screenshot there.


# ---------------------------------------------------
# 5. Swiggy orders: auto-EDA summary report
# ---------------------------------------------------
swiggy = pd.DataFrame({
    "order_id": range(1, 301),
    "restaurant": rng.choice(["Spice Hub", "Pizza Point", "Cafe Mocha", "Biryani House"], 300),
    "order_value": rng.integers(120, 1200, 300),
    "delivery_time_min": rng.normal(35, 8, 300).round(0),
    "payment_mode": rng.choice(["UPI", "Card", "Cash"], 300),
})
swiggy.loc[rng.choice(300, 15, replace=False), "delivery_time_min"] = np.nan
swiggy.to_csv("swiggy_orders.csv", index=False)

df = pd.read_csv("swiggy_orders.csv")
ProfileReport(df, title="Swiggy Orders Report", explorative=True).to_file("swiggy_report.html")
print("Report saved as swiggy_report.html")