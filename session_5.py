import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# ---------------------------------------------------
# 1. Connect with SQLAlchemy and load the 'restaurants' table
# ---------------------------------------------------
# For a real database, use one of these instead (pip install pymysql / psycopg2-binary):
# engine = create_engine("mysql+pymysql://user:password@localhost:3306/zomato_db")
# engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/zomato_db")

# Demo database so the code runs without a server
engine = create_engine("sqlite:///:memory:")

pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "name": ["Spice Hub", "Tandoor Town", "Pizza Point", "Cafe Mocha", "Biryani House", "Dosa Corner"],
    "city": ["Rajkot", "Ahmedabad", "Rajkot", "Surat", "Vadodara", "Rajkot"],
    "rating": [4.2, 4.5, 3.9, 4.1, 4.4, 4.0],
}).to_sql("restaurants", engine, index=False)

restaurants = pd.read_sql("restaurants", engine)   # loads the entire table
print("Q1.")
print(restaurants.head())


# ---------------------------------------------------
# 2. Custom SQL query with read_sql_query()
# ---------------------------------------------------
pd.DataFrame({
    "title": ["Inception", "Titanic", "Dangal", "Jawan", "3 Idiots", "Leo"],
    "rating": [8.8, 7.9, 8.4, 7.0, 8.4, 7.2],
}).rename(columns={"title": "name"}).to_sql("movies", engine, index=False)

query = "SELECT name, rating FROM movies WHERE rating > 8"
top_movies = pd.read_sql_query(query, engine)
print("\nQ2.")
print(top_movies)


# ---------------------------------------------------
# 3. Read JSON directly from a URL
# ---------------------------------------------------
url = "https://jsonplaceholder.typicode.com/users"
users_df = pd.read_json(url)
print("\nQ3.")
print(users_df["username"])


# ---------------------------------------------------
# 4. Load CSVs with pathlib and merge on user_id
# ---------------------------------------------------
base = Path(".")                       # folder containing the CSV files
orders_path = base / "orders.csv"
users_path = base / "users.csv"

# Sample files so the code runs (skip if you already have these files)
orders_path.write_text("order_id,user_id,amount\n1,101,250\n2,102,400\n3,101,150\n4,103,600\n")
users_path.write_text("user_id,username\n101,Amit\n102,Riya\n103,Karan\n")

orders = pd.read_csv(orders_path)
users = pd.read_csv(users_path)

merged = pd.merge(orders, users, on="user_id")
print("\nQ4.")
print(merged[["order_id", "username", "amount"]])


# ---------------------------------------------------
# 5. Concatenate DataFrames and reset the index
# ---------------------------------------------------
today_orders = pd.DataFrame({
    "order_id": [5, 6, 7],
    "item": ["Pizza", "Burger", "Biryani"],
    "price": [350, 180, 280],
})
yesterday_orders = pd.DataFrame({
    "order_id": [1, 2, 3],
    "item": ["Dosa", "Pasta", "Thali"],
    "price": [120, 300, 220],
})

combined = pd.concat([today_orders, yesterday_orders], ignore_index=True)
# Equivalent: pd.concat([...]).reset_index(drop=True)
print("\nQ5.")
print(combined)