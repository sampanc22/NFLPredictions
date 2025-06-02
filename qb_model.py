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

data = pd.read_excel("./Data/qb_data.xlsx", sheet_name="overall")
data = data.iloc[:, 3:-11]
print(data)
# I was just testing random weights to evaluate QB performance metrics
# sample_weights = {
#     'Age': 0.05,
#     'Yds': 0.95,
#     'Cmp%': 0.70,
#     'TD%': 0.45,
#     'Int%': 0.80,
#     'Y/A': 0.4,
#     'AY/A': 0.3,
#     'Y/C': 0.3,
#     'Y/G': 0.85,
#     'Rate': 0.65,
#     'Sk%': 0.45
# }
#
# data['Overall Score'] = (data[list(sample_weights.keys())] * pd.Series(sample_weights)).sum(axis=1)
#
# # Rank quarterbacks by overall score
# ranked_data = data.sort_values(by='Overall Score', ascending=False)
#
# # Plot overall scores
# plt.figure(figsize=(10, 6))
# plt.barh(ranked_data['Player'], ranked_data['Overall Score'], color='skyblue')
# plt.xlabel('Overall Score')
# plt.ylabel('Player')
# plt.title('QB Rankings by Overall Score')
# plt.gca().invert_yaxis()  # Invert y-axis to display highest score at the top
# plt.show()

# from https://www.footballdb.com/stats/qb-seasons.html?yr=2023&type=reg
records = [.647, .706, .706, .647, .750, .625, .529, .600, .529, .500,
           .600, .235, .529, .647, .812, .533, .538, .385, .467, .125,
           .462, .385, .250, .500, .500, .364, .500, .182, .583, .571,
           .333, .375, .800, .375]

X_train, X_test, y_train, y_test = train_test_split(data, records, test_size=0.2, random_state=42)

rmses = {}

# linear regression model
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)
y_pred_linear = linear_regression.predict(X_test)
rmses["Linear Regression"] = root_mean_squared_error(y_test, y_pred_linear)

# ridge regression model
ridge_regression = Ridge(random_state=42)
ridge_regression.fit(X_train, y_train)
y_pred_ridge = ridge_regression.predict(X_test)
rmses["Ridge Regression"] = root_mean_squared_error(y_test, y_pred_ridge)

# elastic net model
elastic_net = ElasticNet(random_state=42, max_iter=10000)
elastic_net.fit(X_train, y_train)
y_pred_elastic_net = elastic_net.predict(X_test)
rmses["Elastic Net"] = root_mean_squared_error(y_test, y_pred_elastic_net)

# support vector regression model
svr = SVR()
svr.fit(X_train, y_train)
y_pred_svr = svr.predict(X_test)
rmses["SVR"] = root_mean_squared_error(y_test, y_pred_svr)

# decision tree regression model
decision_tree_regression = DecisionTreeRegressor(random_state=42)
decision_tree_regression.fit(X_train, y_train)
y_pred_decision_tree = decision_tree_regression.predict(X_test)
rmses["Decision Tree Regression"] = root_mean_squared_error(y_test, y_pred_decision_tree)

# random forest regression model
random_forest_regression = RandomForestRegressor(n_estimators=1000, random_state=42)
random_forest_regression.fit(X_train, y_train)
y_pred_forest = random_forest_regression.predict(X_test)
rmses["Random Forest Regression"] = root_mean_squared_error(y_test, y_pred_forest)

# plot y_test vs y_pred
plt.scatter(range(len(y_test)), y_test, label='Actual', marker='o')
plt.scatter(range(len(y_pred_forest)), y_pred_forest, label='Predicted', marker='x')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Actual vs Predicted Values')
plt.legend()
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