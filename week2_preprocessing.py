from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler

BASE = Path(__file__).resolve().parent

# Load Week 1 logistics dataset
df = pd.read_csv(BASE / "data" / "logistics_data.csv")

print("Original records:", len(df))

# 1. Data inspection
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 2. Convert date column
if "Order_Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"], errors="coerce"
    )

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Convert numeric columns
num_cols = [
    "Distance_KM",
    "Delivery_Time_Hours",
    "Expected_Time_Hours",
    "Transport_Cost_INR",
    "Order_Quantity"
]

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 5. Handle missing values
df = df.dropna(subset=num_cols)

# 6. Clean categorical data
if "Delivery_Status" in df.columns:
    df["Delivery_Status"] = (
        df["Delivery_Status"]
        .astype(str)
        .str.strip()
        .str.title()
    )

# 7. Feature engineering
df["Delay_Hours"] = (
    df["Delivery_Time_Hours"]
    - df["Expected_Time_Hours"]
)

df["Cost_Per_KM"] = (
    df["Transport_Cost_INR"]
    / df["Distance_KM"]
)

# 8. Outlier detection using IQR
Q1 = df["Distance_KM"].quantile(0.25)
Q3 = df["Distance_KM"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Distance_KM"] < lower) |
    (df["Distance_KM"] > upper)
]

print("\nPotential distance outliers:", len(outliers))

# 9. Standardization
features = df[
    ["Distance_KM", "Delivery_Time_Hours", "Order_Quantity"]
]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

df["Distance_Standardized"] = scaled_features[:, 0]
df["Delivery_Time_Standardized"] = scaled_features[:, 1]
df["Quantity_Standardized"] = scaled_features[:, 2]

# 10. Save cleaned dataset
output_dir = BASE / "outputs"
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "week2_cleaned_data.csv"
df.to_csv(output_file, index=False)

print("\n--- WEEK 2 PREPROCESSING COMPLETED ---")
print("Cleaned records:", len(df))
print("Output saved to:", output_file)
