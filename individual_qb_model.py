import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

# Load data for each quarterback into a dictionary
qb_data = pd.read_excel("./Data/qb_data.xlsx", sheet_name=None)

# Remove the sheet named "overall" if it exists
qb_data.pop("overall", None)

# Combine data for all quarterbacks into a single DataFrame
all_qbs_data = pd.concat(qb_data.values(), keys=qb_data.keys())

# Reset index to avoid having a multi-index
all_qbs_data.reset_index(drop=True, inplace=True)


# Data Preprocessing
def preprocess_data(df):
    df['Rush Y/A'].fillna(0, inplace=True)
    df['Cmp%'].fillna(0, inplace=True)
    df['TD%'].fillna(0, inplace=True)
    df['Int%'].fillna(0, inplace=True)
    df['Y/A'].fillna(0, inplace=True)
    df['Rate'].fillna(0, inplace=True)
    df['Sk%'].fillna(0, inplace=True)
    df['Fmb'].fillna(0, inplace=True)
    df['Result'] = df['Result'].apply(lambda result: 1 if result.startswith('W') else 0)


preprocess_data(all_qbs_data)

# Split data and target variables
X = all_qbs_data.iloc[:, 5:]  # Features
y = all_qbs_data['Result']    # Target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

rmses = {}

# linear regression model
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)
y_pred_linear_proba = linear_regression.predict(X_test)
y_pred_linear = np.where(y_pred_linear_proba >= 0.5, 1, 0)
print(classification_report(y_test, y_pred_linear))
rmses["Linear Regression"] = root_mean_squared_error(y_test, y_pred_linear)

# ridge regression model
ridge_regression = Ridge(random_state=42)
ridge_regression.fit(X_train, y_train)
y_pred_ridge_proba = ridge_regression.predict(X_test)
y_pred_ridge = np.where(y_pred_ridge_proba >= 0.5, 1, 0)
print(classification_report(y_test, y_pred_ridge))
rmses["Ridge Regression"] = root_mean_squared_error(y_test, y_pred_ridge)

# elastic net model
elastic_net = ElasticNet(random_state=42, max_iter=10000)
elastic_net.fit(X_train, y_train)
y_pred_elastic_net_proba = elastic_net.predict(X_test)
y_pred_elastic_net = np.where(y_pred_elastic_net_proba >= 0.5, 1, 0)
print(classification_report(y_test, y_pred_elastic_net))
rmses["Elastic Net"] = root_mean_squared_error(y_test, y_pred_elastic_net)

# support vector regression model
svr = SVR()
svr.fit(X_train, y_train)
y_pred_svr_proba = svr.predict(X_test)
y_pred_svr = np.where(y_pred_svr_proba >= 0.5, 1, 0)
print(classification_report(y_test, y_pred_svr))
rmses["SVR"] = root_mean_squared_error(y_test, y_pred_svr)

# decision tree regression model
decision_tree_regression = DecisionTreeRegressor(random_state=42)
decision_tree_regression.fit(X_train, y_train)
y_pred_decision_tree_proba = decision_tree_regression.predict(X_test)
y_pred_decision_tree = np.where(y_pred_decision_tree_proba >= 0.5, 1, 0)
print(classification_report(y_test, y_pred_decision_tree))
rmses["Decision Tree Regression"] = root_mean_squared_error(y_test, y_pred_decision_tree)

# random forest regression model
random_forest_regression = RandomForestRegressor(n_estimators=1000, random_state=42)
random_forest_regression.fit(X_train, y_train)
y_pred_forest_proba = random_forest_regression.predict(X_test)
y_pred_forest = np.where(y_pred_forest_proba >= 0.5, 1, 0)
print(classification_report(y_test, y_pred_forest))
rmses["Random Forest Regression"] = root_mean_squared_error(y_test, y_pred_forest)

# plot y_test vs y_pred
# import matplotlib.pyplot as plt

# Plot actual vs predicted values
plt.figure(figsize=(18, 6))
plt.scatter(range(len(y_test)), y_test, label='Actual', marker='o')
plt.scatter(range(len(y_pred_linear)), y_pred_linear, label='Predicted', marker='x')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Actual vs Predicted Values (Linear Regression)')
plt.legend()
plt.grid(True)
plt.show()


models = list(rmses.keys())
rmse_vals = list(rmses.values())

# Plot RMSE for each model
plt.bar(models, rmse_vals, color='skyblue')

# Add labels and title
plt.xlabel('Model')
plt.ylabel('RMSE')
plt.title('RMSE for Different Models')

plt.xticks(rotation=90, ha='center')

# Set xticks alignment to center
# plt.xticks(ha='center')

# Show plot
plt.tight_layout()
plt.show()

