import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password TEXT NOT NULL
)
""")

# Predictions Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    area REAL,
    bedrooms INTEGER,
    bathrooms INTEGER,
    stories INTEGER,
    parking INTEGER,
    predicted_price REAL,
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    rating INTEGER NOT NULL,

    review TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    email TEXT UNIQUE,

    password TEXT

)
""")

# Default Admin

cursor.execute("""
INSERT OR IGNORE INTO admin(
email,
password
)

VALUES(
'admin@gmail.com',
'admin123'
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")