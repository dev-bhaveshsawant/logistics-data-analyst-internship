import pandas as pd
import matplotlib.pyplot as plt

# Load logistics dataset
df = pd.read_csv("logistics_data_week3.csv")

# Basic EDA
print(df.head())
print(df.info())
print(df.describe())

# Central tendency
print("Mean:")
print(df[["Shipment_Volume", "Distance_km", "Delivery_Time_days", "Transportation_Cost"]].mean())

print("Median:")
print(df[["Shipment_Volume", "Distance_km", "Delivery_Time_days", "Transportation_Cost"]].median())

# Correlation
print(df[["Shipment_Volume", "Distance_km", "Delivery_Time_days", "Transportation_Cost"]].corr())

# 1. Delivery-time distribution
plt.hist(df["Delivery_Time_days"], bins=12, edgecolor="black")
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Time (days)")
plt.ylabel("Number of Shipments")
plt.show()

# 2. Cost by transport mode
df.boxplot(column="Transportation_Cost", by="Transport_Mode")
plt.title("Transportation Cost by Transport Mode")
plt.suptitle("")
plt.show()

# 3. Shipment volume vs delivery time
for mode in df["Transport_Mode"].unique():
    data = df[df["Transport_Mode"] == mode]
    plt.scatter(data["Shipment_Volume"], data["Delivery_Time_days"], label=mode)

plt.title("Shipment Volume vs Delivery Time")
plt.xlabel("Shipment Volume")
plt.ylabel("Delivery Time (days)")
plt.legend()
plt.show()

# 4. Average delivery time by region
df.groupby("Region")["Delivery_Time_days"].mean().plot(kind="bar")
plt.title("Average Delivery Time by Region")
plt.xlabel("Region")
plt.ylabel("Average Delivery Time (days)")
plt.show()
