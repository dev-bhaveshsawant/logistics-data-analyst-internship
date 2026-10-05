import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("logistics_data_week3.csv")

features = ["Region", "Transport_Mode", "Shipment_Volume", "Distance_km", "Transportation_Cost"]
target = "Delivery_Time_days"
X, y = df[features], df[target]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["Region", "Transport_Mode"]),
    ("num", "passthrough", ["Shipment_Volume", "Distance_km", "Transportation_Cost"])
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

models = {
    "Linear Regression": Pipeline([("pre", preprocessor), ("model", LinearRegression())]),
    "Random Forest": Pipeline([("pre", preprocessor),
        ("model", RandomForestRegressor(n_estimators=200, max_depth=8,
                                        min_samples_leaf=2, random_state=42))])
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(name)
    print("MAE:", round(mean_absolute_error(y_test, pred), 3))
    print("RMSE:", round(mean_squared_error(y_test, pred) ** 0.5, 3))
    print("R2:", round(r2_score(y_test, pred), 3))
    print()

# 5-fold cross-validation for Random Forest
model = models["Random Forest"]
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = []
for train_idx, test_idx in kf.split(X):
    model.fit(X.iloc[train_idx], y.iloc[train_idx])
    pred = model.predict(X.iloc[test_idx])
    scores.append(mean_squared_error(y.iloc[test_idx], pred) ** 0.5)
print("5-Fold CV RMSE:", round(sum(scores) / len(scores), 3))
