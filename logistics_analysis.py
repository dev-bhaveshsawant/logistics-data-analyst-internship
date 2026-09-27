from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

BASE=Path(__file__).resolve().parent
df=pd.read_csv(BASE/"data/logistics_data.csv")
df["Order_Date"]=pd.to_datetime(df["Order_Date"],errors="coerce")
df=df.drop_duplicates()
num=["Distance_KM","Delivery_Time_Hours","Expected_Time_Hours","Transport_Cost_INR","Order_Quantity"]
for c in num: df[c]=pd.to_numeric(df[c],errors="coerce")
df=df.dropna(subset=num)
df["Delay_Hours"]=df["Delivery_Time_Hours"]-df["Expected_Time_Hours"]
df["Cost_Per_KM"]=df["Transport_Cost_INR"]/df["Distance_KM"]

total=len(df)
on=(df["Delivery_Status"].str.lower()=="on time").mean()*100
late=100-on
print("\n--- LOGISTICS KPIs ---")
print("Total Deliveries:",total)
print("On-Time Delivery Rate: %.2f%%"%on)
print("Late Delivery Rate: %.2f%%"%late)
print("Average Delivery Time: %.2f hours"%df["Delivery_Time_Hours"].mean())
print("Average Distance: %.2f km"%df["Distance_KM"].mean())
print("Average Transport Cost: INR %.2f"%df["Transport_Cost_INR"].mean())
print("Overall Cost per KM: INR %.2f"%(df["Transport_Cost_INR"].sum()/df["Distance_KM"].sum()))

# Regression: delivery time prediction
X=df[["Distance_KM","Order_Quantity"]]; y=df["Delivery_Time_Hours"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42)
m=LinearRegression().fit(Xtr,ytr); pred=m.predict(Xte)
print("\n--- REGRESSION ---")
print("MAE:",round(mean_absolute_error(yte,pred),3))
print("RMSE:",round(np.sqrt(mean_squared_error(yte,pred)),3))
print("R2:",round(r2_score(yte,pred),3))

# Clustering
f=df[["Distance_KM","Delivery_Time_Hours","Order_Quantity"]].copy()
z=StandardScaler().fit_transform(f)
km=KMeans(n_clusters=3,random_state=42,n_init=10)
f["Cluster"]=km.fit_predict(z)
f.to_csv(BASE/"outputs/delivery_clusters.csv",index=False)
print("\n--- CLUSTERING ---")
print(f["Cluster"].value_counts().sort_index())

print("\nAnalysis completed. Cluster output saved in outputs/.")
