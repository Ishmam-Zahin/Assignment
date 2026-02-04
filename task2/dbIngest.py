import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv("./backend/.env")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

create_query = """
    CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    model VARCHAR(100) UNIQUE,
    release_date VARCHAR(20),
    display_size NUMERIC(3,1),
    display_width INTEGER,
    display_height INTEGER,
    battery INTEGER,
    camera INTEGER,
    ram INTEGER,
    storage INTEGER,
    price NUMERIC(8,2)
);
"""

cursor.execute(create_query)

df = pd.read_csv("data.csv")

insert_query = """
    INSERT INTO phones
    (model, release_date, display_size, display_width, display_height,
     battery, camera, ram, storage, price)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (model) DO NOTHING;
"""

# ---------- INSERT DATA ----------
for _, row in df.iterrows():
    cursor.execute(
        insert_query,
        (
            row["model"],
            row["release_date"],
            float(row["display_size"]),
            int(row["display_width"]),
            int(row["display_height"]),
            int(row["battery"]),
            row["camera"],
            int(row["ram"]),
            int(row["storage"]),
            float(row["price"])
        )
    )

conn.commit()
cursor.close()
conn.close()

print("CSV data inserted successfully!")
