import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv("Housing.csv")

# Convert Yes/No Columns

binary_columns = [
    'mainroad',
    'guestroom',
    'basement',
    'hotwaterheating',
    'airconditioning',
    'prefarea'
]

for col in binary_columns:
    df[col] = df[col].map({
        'yes': 1,
        'no': 0
    })

# Encode Furnishing Status

le = LabelEncoder()

df['furnishingstatus'] = le.fit_transform(
    df['furnishingstatus']
)

# Features

X = df.drop('price', axis=1)

# Target

y = df['price']

# Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Save Model

pickle.dump(
    model,
    open("model.pkl", "wb")
)

# Save Encoder

pickle.dump(
    le,
    open("encoder.pkl", "wb")
)

print("Model Trained Successfully")