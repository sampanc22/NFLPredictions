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

qb_file_path = "./Data/qb_data.xlsx"
rb_file_path = "./Data/rb_data.xlsx"


qb_dict = {"LVR": "aidan_o'connell", "TAM": "baker_mayfield", "SFO": "brock_purdy", "CAR": "bryce_young",
           "HOU": "cj_stroud", "DAL": "dak_prescott", "NOR": "derek_carr", "ATL": "desmond_ridder",
           "IND": "garnder_minshew", "SEA": "geno_smith", "CIN": "joe_burrow", "PHI": "jalen_hurts",
           "DET": "jared_goff", "CLE": "joe_flacco", "GNB": "jordan_love", "BUF": "josh_allen", "CHI": "justin_fields",
           "LAC": "justin_herbert", "PIT": "kenny_pickett", "MIN": "kirk_cousins", "ARI": "kyler_murray",
           "BAL": "lamar_jackson", "NWE": "mac_jones", "LAR": "matthew_stafford", "KAN": "patrick_mahomes",
           "DEN": "russell_wilson", "WAS": "sam_howell", "JAX": "trevor_lawrence", "MIA": "tua_tagovailoa",
           "TEN": "will_levis", "NYJ": "zach_wilson", "TEN_": "ryan_tannehill", "MIN_": "joshua_dobbs",
           "ARI_": "joshua_dobbs", "CIN_": "jake_browning"}

rb_dict = {"NYG": "saquon_barkley", "DAL": "tony_pollard", "GNB": "aaron_jones", "GNB_": "aj_dillon",
           "MIN": "alexander_mattison", "NOR": "alvin_kamara", "CHI": "khalil_herbert", "LAR": "kyren_williams",
           "CAR": "miles_sanders", "PIT": "najee_harris", "MIA": "raheem_mostert", "LAC": "austin_ekeler",
           "ATL": "bijan_robinson", "NYJ": "breece_hall", "WAS": "brian_robinson",
           "SFO": "christian_mccaffrey", "CAR_": "chuba_hubbard", "HOU": "dameon_pierce", "PHI": "dandre_swift",
           "DET": "david_montgomery", "TEN": "derrick_henry", "HOU_": "devin_singletary", "MIA_": "devon_achane",
           "CHI_": "donta_foreman", "NWE": "ezekiel_elliot", "BAL": "gus_edwards", "KAN": "isiah_pacheco",
           "NOR_": "jamaal_williams", "ARI": "james_conner", "BUF": "james_cook", "DEN": "javonte_williams",
           "PIT_": "jaylen_warren", "CLE": "jerome_ford", "CIN": "joe_mixon", "IND": "jonathan_taylor",
           "LVR": "josh_jacobs", "LAC_": "joshua_kelley", "CLE_": "kareem_hunt", "SEA": "kenneth_walker",
           "TAM": "rachaad_white", "NWE_": "rhamondre_stevenson", "DAL_": "rico_dowdle",
           "JAX": "travis_etienne", "MIN_": "ty_chandler", "TEN_": "tyjae_spears", "ATL_": "tyler_allgeier",
           "SEA_": "zach_charbonnet", "IND_": "zack_moss", "LVR_": "zamir_white"}

qb_data = {}
rb_data = {}

X = []
y = []

for team, player in qb_dict.items():
    temp = {player: pd.read_excel(qb_file_path, sheet_name=player)}
    team_name = team.strip("_")
    if team_name in qb_data:
        qb_data[team_name][player] = pd.read_excel(qb_file_path, sheet_name=player)
    else:
        qb_data[team_name] = temp.copy()

for team, player in rb_dict.items():
    temp = {player: pd.read_excel(rb_file_path, sheet_name=player)}
    team_name = team.strip("_")
    if team_name in rb_data:
        rb_data[team_name][player] = pd.read_excel(rb_file_path, sheet_name=player)
    else:
        rb_data[team_name] = temp.copy()


def preprocess_qb_data(df):
    df['Rush Y/A'].fillna(0, inplace=True)
    df['Cmp%'].fillna(0, inplace=True)
    df['TD%'].fillna(0, inplace=True)
    df['Int%'].fillna(0, inplace=True)
    df['Y/A'].fillna(0, inplace=True)
    df['Rate'].fillna(0, inplace=True)
    df['Sk%'].fillna(0, inplace=True)
    df['Fmb'].fillna(0, inplace=True)
    df['Result'] = df['Result'].apply(lambda result: 1 if result.startswith('W') else 0)


def preprocess_rb_data(df):
    df['Y/A'].fillna(0, inplace=True)
    df['Y/R'].fillna(0, inplace=True)
    df['Catch%'] = df['Catch%'].str.rstrip('%').astype(float) / 100
    df['Catch%'].fillna(0, inplace=True)
    df['Y/Tch'].fillna(0, inplace=True)
    df['Result'] = df['Result'].apply(lambda result: 1 if result.startswith('W') else 0)


def get_opponent_qb_stats(date, team):
    if team not in qb_data:
        return None
    qb_df = qb_data[team]
    for player_name, player_df in qb_df.items():
        opponent_df = player_df[player_df['Date'] == date]
        if len(opponent_df) > 0:
            stats = opponent_df.iloc[0]
            return stats
    return None


def get_rb_stats(date, team):
    if team not in rb_data:
        return None
    rb_df = rb_data[team]
    for player_name, player_df in rb_df.items():
        rb_team_df = player_df[player_df['Date'] == date]
        if len(rb_team_df) > 0:
            stats = rb_team_df.iloc[0]
            return stats
    return None


for player_data in qb_data.values():
    for df in player_data.values():
        preprocess_qb_data(df)

for player_data in rb_data.values():
    for df in player_data.values():
        preprocess_rb_data(df)

for team, data in qb_data.items():
    for player, df in data.items():
        for index, row in df.iterrows():
            date = row['Date']
            team = row['Team']
            opp = row['Opp']
            result = row['Result']
            cmp_percentage = row['Cmp%']
            yards = row['Yds']
            td = row['TD']
            td_percentage = row['TD%']
            int_percentage = row['Int%']
            yards_per_attempt = row['Y/A']
            rating = row['Rate']
            sack_percentage = row['Sk%']
            rush_attempts = row['RushAtt']
            rush_yards = row['RushYds']
            rush_td = row['RushTD']
            rush_yards_per_attempt = row['Rush Y/A']
            fumbles = row['Fmb']

            opponent_qb_stats = get_opponent_qb_stats(date, opp)
            team_rb_stats = get_rb_stats(date, team)
            opponent_rb_stats = get_rb_stats(date, opp)

            if opponent_qb_stats is not None and team_rb_stats is not None and opponent_rb_stats is not None:
                X.append([cmp_percentage - opponent_qb_stats['Cmp%'], yards - opponent_qb_stats['Yds'],
                          td - opponent_qb_stats['TD'], td_percentage - opponent_qb_stats['TD%'],
                          int_percentage - opponent_qb_stats['Int%'], yards_per_attempt - opponent_qb_stats['Y/A'],
                          rating - opponent_qb_stats['Rate'], sack_percentage - opponent_qb_stats['Sk%'],
                          rush_attempts - opponent_qb_stats['RushAtt'], rush_yards - opponent_qb_stats['RushYds'],
                          rush_td - opponent_qb_stats['RushTD'], rush_yards_per_attempt - opponent_qb_stats['Rush Y/A'],
                          fumbles - opponent_qb_stats['Fmb'], team_rb_stats['Yds'] - opponent_rb_stats['Yds'],
                          team_rb_stats['TD'] - opponent_rb_stats['TD'], team_rb_stats['Y/A'] - opponent_rb_stats['Y/A']
                          , team_rb_stats['Tgt'] - opponent_rb_stats['Tgt'],
                          team_rb_stats['Rec'] - opponent_rb_stats['Rec'],
                          team_rb_stats['RecYds'] - opponent_rb_stats['RecYds'],
                          team_rb_stats['Y/R'] - opponent_rb_stats['Y/R'],
                          team_rb_stats['RecTD'] - opponent_rb_stats['RecTD'],
                          team_rb_stats['Catch%'] - opponent_rb_stats['Catch%'],
                          team_rb_stats['Fmb'] - opponent_rb_stats['Fmb']])

                y.append(result)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
