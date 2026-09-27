# Logistics Data Analyst Internship – Week 1

## Strategic Planning and Data Exploration in Logistics

**Prepared By:** Bhavesh Sawant
**Program:** B.Sc. Computer Science
**Project Area:** Logistics Data Analysis
**Week:** 1
**Tools:** Python, Pandas, NumPy, Scikit-learn

---

## 1. Project Overview

This project is developed as part of a Logistics Data Analyst Internship Week 1 task.

The project focuses on strategic planning and data exploration in a regional last-mile logistics scenario. The analysis uses logistics delivery data to understand delivery performance, transportation costs, delivery time, and delivery patterns.

Python and machine learning techniques are used to calculate important logistics KPIs, predict delivery time using Linear Regression, and group similar delivery records using K-Means Clustering.

---

## 2. Problem Statement

Logistics companies handle large amounts of operational data related to deliveries, distances, transportation costs, order quantities, and delivery times.

Without proper data analysis, it can be difficult to identify:

* Delayed deliveries
* Transportation cost variations
* Inefficient delivery patterns
* Delivery-time trends
* Groups of similar delivery operations

This project uses data analysis and machine learning techniques to extract useful information from logistics delivery data and support data-driven decision-making.

---

## 3. Project Objectives

The main objectives of this project are:

* To understand logistics delivery data.
* To clean and preprocess the dataset.
* To calculate important logistics KPIs.
* To analyze delivery time and transportation cost.
* To measure on-time and late delivery performance.
* To predict delivery time using Linear Regression.
* To identify similar delivery patterns using K-Means Clustering.
* To generate an output dataset for further analysis.
* To provide a foundation for future logistics optimization.

---

## 4. Logistics Scenario

The project considers a regional last-mile logistics company that delivers products from a central location to different customers.

The dataset contains information related to:

* Order date
* Distance
* Delivery time
* Expected delivery time
* Transportation cost
* Order quantity
* Delivery status

The analysis is performed on the available demonstration dataset.

> **Note:** The dataset used in this project is intended for demonstration and internship analysis purposes. It should not be interpreted as confidential or real company data.

---

## 5. Dataset

The dataset is stored inside the `data` directory.

### Dataset File

```text
data/logistics_data.csv
```

### Important Columns

| Column                | Description                             |
| --------------------- | --------------------------------------- |
| `Order_Date`          | Date of the order                       |
| `Distance_KM`         | Delivery distance in kilometers         |
| `Delivery_Time_Hours` | Actual delivery time                    |
| `Expected_Time_Hours` | Expected delivery time                  |
| `Transport_Cost_INR`  | Transportation cost in INR              |
| `Order_Quantity`      | Quantity of products ordered            |
| `Delivery_Status`     | Delivery status such as On Time or Late |

---

## 6. Data Preprocessing

The Python program performs several preprocessing operations before analysis.

### Operations performed

1. Converts the order date into a datetime format.
2. Removes duplicate records.
3. Converts numerical columns into numeric data types.
4. Handles invalid numerical values.
5. Removes rows containing missing values in required numerical columns.
6. Calculates delivery delay.
7. Calculates transportation cost per kilometer.

### Additional Features

The project calculates:

```text
Delay_Hours
Cost_Per_KM
```

These features help in understanding delivery performance and transportation efficiency.

---

## 7. Key Performance Indicators (KPIs)

The project calculates the following logistics KPIs:

### Total Deliveries

Number of delivery records available in the dataset.

### On-Time Delivery Rate

Percentage of deliveries completed on or before the expected delivery time.

### Late Delivery Rate

Percentage of deliveries completed after the expected delivery time.

### Average Delivery Time

Average time required to complete deliveries.

### Average Distance

Average distance travelled for the deliveries.

### Average Transportation Cost

Average transportation cost per delivery.

### Overall Cost per Kilometer

Total transportation cost divided by total delivery distance.

---

## 8. Machine Learning Methodologies

### 8.1 Linear Regression

Linear Regression is used to predict delivery time.

#### Input Features

* Distance in kilometers
* Order quantity

#### Target Variable

```text
Delivery_Time_Hours
```

The dataset is divided into training and testing sets using an 80:20 split.

The model is evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

---

### 8.2 K-Means Clustering

K-Means Clustering is used to identify groups of similar delivery records.

The clustering model uses:

* Distance
* Delivery time
* Order quantity

Before clustering, the features are standardized using `StandardScaler`.

The model creates **3 clusters**.

The clustering results are saved to:

```text
outputs/delivery_clusters.csv
```

---

## 9. Project Results

The analysis was performed on **30 delivery records**.

### Logistics KPI Results

| KPI                    |      Result |
| ---------------------- | ----------: |
| Total Deliveries       |          30 |
| On-Time Delivery Rate  |      73.33% |
| Late Delivery Rate     |      26.67% |
| Average Delivery Time  |  3.26 hours |
| Average Distance       |   110.50 km |
| Average Transport Cost | INR 1317.67 |
| Overall Cost per KM    |   INR 11.92 |

---

## 10. Regression Results

The Linear Regression model produced the following evaluation results:

| Metric   | Result |
| -------- | -----: |
| MAE      |   0.11 |
| RMSE     |   0.13 |
| R² Score |  0.993 |

These metrics describe the model's performance on the test data from this dataset. The results should not be assumed to represent performance on a larger or different real-world logistics dataset.

---

## 11. Clustering Results

The K-Means model generated three clusters:

| Cluster   | Number of Records |
| --------- | ----------------: |
| Cluster 0 |                13 |
| Cluster 1 |                11 |
| Cluster 2 |                 6 |

The generated clustering result is stored in:

```text
outputs/delivery_clusters.csv
```

---

## 12. Project Workflow

The overall workflow of the project is:

```text
Data Collection
       ↓
Data Cleaning
       ↓
Data Preprocessing
       ↓
Exploratory Analysis
       ↓
KPI Calculation
       ↓
Linear Regression
       ↓
K-Means Clustering
       ↓
Output Generation
       ↓
Reporting
```

---

## 13. Project Structure

```text
logistics-data-analyst-internship/
│
├── data/
│   └── logistics_data.csv
│
├── outputs/
│   └── delivery_clusters.csv
│
├── .gitignore
├── README.md
├── logistics_analysis.py
└── requirements.txt
```

---

## 14. Technologies Used

### Programming Language

* Python 3

### Libraries

* Pandas
* NumPy
* Scikit-learn

### Machine Learning

* Linear Regression
* K-Means Clustering
* StandardScaler

### Development and Version Control

* Python IDLE
* GitHub

---

## 15. Requirements

The required Python libraries are listed in:

```text
requirements.txt
```

Main dependencies include:

```text
pandas
numpy
scikit-learn
```

---

## 16. Installation

Clone the repository:

```bash
git clone https://github.com/dev-bhaveshsawant/logistics-data-analyst-internship.git
```

Move into the project directory:

```bash
cd logistics-data-analyst-internship
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## 17. How to Run

Run the main Python file:

```bash
python logistics_analysis.py
```

The program will display:

* Logistics KPIs
* Regression evaluation metrics
* Clustering results

The clustering output will automatically be saved as:

```text
outputs/delivery_clusters.csv
```

---

## 18. Sample Output

```text
--- LOGISTICS KPIs ---
Total Deliveries: 30
On-Time Delivery Rate: 73.33%
Late Delivery Rate: 26.67%
Average Delivery Time: 3.26 hours
Average Distance: 110.50 km
Average Transport Cost: INR 1317.67
Overall Cost per KM: INR 11.92

--- REGRESSION ---
MAE: 0.11
RMSE: 0.13
R2: 0.993

--- CLUSTERING ---
Cluster
0    13
1    11
2     6
```

---

## 19. Expected Business Insights

The analysis can help identify:

* Overall delivery performance.
* The proportion of delayed deliveries.
* Average transportation requirements.
* Average delivery costs.
* Relationships between distance, order quantity, and delivery time.
* Groups of similar delivery operations.

These insights can support logistics planning and further analysis.

---

## 20. Limitations

This project has several limitations:

* The dataset contains only 30 delivery records.
* The dataset is intended for demonstration and internship purposes.
* Real-time traffic conditions are not included.
* Weather conditions are not included.
* Vehicle capacity constraints are not included.
* Delivery time windows are not modeled.
* Route optimization is not implemented in the current version.
* Machine learning results may change when a larger or different dataset is used.

---

## 21. Future Improvements

Future versions of the project can include:

* Larger real-world logistics datasets.
* Real-time traffic information.
* Route optimization algorithms.
* Vehicle capacity constraints.
* Delivery time-window analysis.
* Interactive dashboards.
* Delivery delay prediction.
* Transportation cost optimization.
* Real-time logistics monitoring.
* Advanced machine learning models.

---

## 22. Conclusion

This project demonstrates how data analysis and machine learning can be applied to logistics operations.

The project performs data preprocessing, KPI calculation, delivery-time prediction, and delivery-pattern clustering using Python.

Linear Regression is used to predict delivery time based on distance and order quantity, while K-Means Clustering is used to group similar delivery records.

The project provides a structured foundation for further development of logistics analytics, predictive modeling, and route optimization solutions.

---

## 23. References

1. Python Documentation
2. Pandas Documentation
3. NumPy Documentation
4. Scikit-learn Documentation
5. Public logistics and supply-chain datasets and research resources

---

## 24. Author

**Bhavesh Sawant**
B.Sc. Computer Science
Logistics Data Analyst Internship – Week 1
