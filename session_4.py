import pandas as pd
import numpy as np

# ---------------------------------------------------
# 1. Load IPL CSV and print first 5 rows
# ---------------------------------------------------
# Real data: download an IPL dataset (e.g. "IPL Complete Dataset" on Kaggle)
# and use its matches file, e.g. pd.read_csv("matches.csv")
pd.DataFrame({
    "match_id": [1, 2, 3, 4, 5, 6],
    "team1": ["CSK", "MI", "RCB", "KKR", "DC", "SRH"],
    "team2": ["MI", "RCB", "KKR", "DC", "SRH", "CSK"],
    "team1_score": [180, 165, 200, 150, 175, 190],
    "team2_score": [178, 170, 185, 155, 160, 192],
}).to_csv("ipl_matches.csv", index=False)

df1 = pd.read_csv("ipl_matches.csv")
print("Q1.")
print(df1.head())


# ---------------------------------------------------
# 2. Load trending songs JSON and show df.info()
# ---------------------------------------------------
pd.DataFrame({
    "song": ["Kesariya", "Apna Bana Le", "Chaleya", "Tum Hi Ho"],
    "artist": ["Arijit Singh", "Arijit Singh", "Arijit Singh", "Arijit Singh"],
    "streams_millions": [450.5, 320.2, 280.0, 510.7],
    "rank": [2, 3, 4, 1],
}).to_json("trending_songs.json", orient="records")

df2 = pd.read_json("trending_songs.json")
print("\nQ2.")
df2.info()


# ---------------------------------------------------
# 3. Load Zomato TSV and describe all columns
# ---------------------------------------------------
pd.DataFrame({
    "restaurant": ["Spice Hub", "Tandoor Town", "Pizza Point", "Cafe Mocha"],
    "city": ["Rajkot", "Ahmedabad", "Rajkot", "Surat"],
    "rating": [4.2, 4.5, 3.9, 4.1],
    "cost_for_two": [600, 800, 500, 400],
}).to_csv("zomato.tsv", sep="\t", index=False)

df3 = pd.read_csv("zomato.tsv", sep="\t")
print("\nQ3.")
print(df3.describe(include="all"))


# ---------------------------------------------------
# 4. Read a large Excel file in chunks of 2000 rows
# ---------------------------------------------------
# NOTE: read_excel() does NOT support chunksize, so we use skiprows + nrows.
# (Requires: pip install openpyxl)
n_rows = 10500
pd.DataFrame({
    "product_id": np.arange(1, n_rows + 1),
    "name": [f"Product {i}" for i in range(1, n_rows + 1)],
    "price": np.random.randint(100, 50000, n_rows),
}).to_excel("flipkart_products.xlsx", index=False)

file = "flipkart_products.xlsx"
chunk_size = 2000
start = 0
chunk_no = 1

print("\nQ4.")
while True:
    # skip the data rows already read (row 0 is the header, so skip from 1)
    chunk = pd.read_excel(file, skiprows=range(1, start + 1), nrows=chunk_size)
    if chunk.empty:
        break
    print(f"Chunk {chunk_no}: {len(chunk)} rows")
    start += chunk_size
    chunk_no += 1


# ---------------------------------------------------
# 5. Semicolon-separated Paytm CSV: detect missing values
# ---------------------------------------------------
with open("paytm.csv", "w") as f:
    f.write("txn_id;user;amount;status\n"
            "1;Amit;250;SUCCESS\n"
            "2;Riya;;SUCCESS\n"
            "3;Karan;500;\n"
            "4;;120;FAILED\n")

df5 = pd.read_csv("paytm.csv", sep=";")      # sep=";" is the key part
null_counts = df5.isnull().sum()
cols_with_nulls = null_counts[null_counts > 0]

print("\nQ5.")
if cols_with_nulls.empty:
    print("No missing values found.")
else:
    print("Columns with missing values:")
    print(cols_with_nulls)