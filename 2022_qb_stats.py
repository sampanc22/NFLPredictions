from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

webpages = {"KAN": "https://www.pro-football-reference.com/players/M/MahoPa00/gamelog/2022/",
            "LAC": "https://www.pro-football-reference.com/players/H/HerbJu00/gamelog/2022/",
            "TAM": "https://www.pro-football-reference.com/players/B/BradTo00/gamelog/2022/",
            "MIN": "https://www.pro-football-reference.com/players/C/CousKi00/gamelog/2022/",
            "CIN": "https://www.pro-football-reference.com/players/B/BurrJo01/gamelog/2022/",
            "DET": "https://www.pro-football-reference.com/players/G/GoffJa00/gamelog/2022/",
            "BUF": "https://www.pro-football-reference.com/players/A/AlleJo02/gamelog/2022/",
            "SEA": "https://www.pro-football-reference.com/players/A/AlleJo02/gamelog/2022/",
            "JAX": "https://www.pro-football-reference.com/players/L/LawrTr00/gamelog/2022/",
            "PHI": "https://www.pro-football-reference.com/players/H/HurtJa00/gamelog/2022/",
            "GNB": "https://www.pro-football-reference.com/players/R/RodgAa00/gamelog/2022/",
            "MIA": "https://www.pro-football-reference.com/players/T/TagoTu00/gamelog/2022/",
            "DEN": "https://www.pro-football-reference.com/players/W/WilsRu00/gamelog/2022/",
            "LVR": "https://www.pro-football-reference.com/players/C/CarrDe02/gamelog/2022/",
            "NYG": "https://www.pro-football-reference.com/players/J/JoneDa05/gamelog/2022/",
            "HOU": "https://www.pro-football-reference.com/players/M/MillDa02/gamelog/2022/",
            "IND": "https://www.pro-football-reference.com/players/R/RyanMa00/gamelog/2022/",
            "NWE": "https://www.pro-football-reference.com/players/J/JoneMa05/gamelog/2022/",
            "NOR": "https://www.pro-football-reference.com/players/D/DaltAn00/gamelog/2022/",
            "DAL": "https://www.pro-football-reference.com/players/P/PresDa01/gamelog/2022/",
            "CLE": "https://www.pro-football-reference.com/players/B/BrisJa00/gamelog/2022/",
            "TEN": "https://www.pro-football-reference.com/players/T/TannRy00/gamelog/2022/",
            "SFO": "https://www.pro-football-reference.com/players/G/GaroJi00/gamelog/2022/",
            "PIT": "https://www.pro-football-reference.com/players/P/PickKe00/gamelog/2022/",
            "ARI": "https://www.pro-football-reference.com/players/M/MurrKy00/gamelog/2022/",
            "CHI": "https://www.pro-football-reference.com/players/F/FielJu00/gamelog/2022/",
            "BAL": "https://www.pro-football-reference.com/players/J/JackLa00/gamelog/2022/",
            "ATL": "https://www.pro-football-reference.com/players/M/MariMa01/gamelog/2022/",
            "CAR": "https://www.pro-football-reference.com/players/M/MayfBa00/gamelog/2022/",
            "LAR": "https://www.pro-football-reference.com/players/S/StafMa00/gamelog/2022/",
            "LAR_": "https://www.pro-football-reference.com/players/M/MayfBa00/gamelog/2022/",
            "WAS": "https://www.pro-football-reference.com/players/H/HeinTa00/gamelog/2022/",
            "WAS_": "https://www.pro-football-reference.com/players/W/WentCa00/gamelog/2022/",
            "NYJ": "https://www.pro-football-reference.com/players/W/WilsZa00/gamelog/2022/",
            "SFO_": "https://www.pro-football-reference.com/players/P/PurdBr00/gamelog/2022/",
            "PIT_": "https://www.pro-football-reference.com/players/T/TrubMi00/gamelog/2022/",
            "NYJ_": "https://www.pro-football-reference.com/players/W/WhitMi01/gamelog/2022/"}

qb_dict = {}


def read_file(homepage):
    # time.sleep(5)
    url = urlopen(homepage)
    stats = BeautifulSoup(url, features='html.parser')

    col_headers = stats.find_all('tr')[1]
    col_headers = [i.getText() for i in col_headers.findAll('th')]
    rows = stats.find_all('tr')[2:]

    data = []

    for i in range(17):
        if rows[i].find('td') is None:
            continue
        data.append([col.getText() for col in rows[i].findAll('td')])

    df = pd.DataFrame(data, columns=col_headers[1:])
    df = df.iloc[:, list(range(24)) + [-12]]

    df.columns.values[5] = "Home/Away"
    df.columns.values[4] = "Team"
    df.columns.values[12] = "Pass Yds"
    df.columns.values[-2] = "RushTD"
    df.columns.values[-3] = "Rush Y/A"
    df.columns.values[-4] = "RushYds"
    df.columns.values[-5] = "RushAtt"
    df.columns.values[-8] = "SkYds"

    relevant_stats = ['Cmp', 'Att', 'Pass Yds', 'TD', 'Int', 'Y/A', 'Rate', 'Sk', 'RushAtt', 'RushYds', 'RushTD',
                      'Rush Y/A', 'Fmb']

    # if data doesn't have a fumbles category, set column to 0s
    if df.columns.values[-1] != 'Fmb':
        df = df.assign(Fmb=0)

    df = df[['Date', 'Team', 'Home/Away', 'Opp', 'Result'] + relevant_stats]

    df['Result'] = df['Result'].apply(lambda result: 1 if result.startswith('W') else 0)

    # Convert relevant stats columns to numbers and fill missing values with 0
    for i in relevant_stats:
        df[i] = pd.to_numeric(df[i], errors='coerce').fillna(0)

    # Filter out unplayed games
    df = df[df['Att'] != 0]

    df.columns.values[7] = 'Yds'

    # Add certain columns
    df['Cmp%'] = (df['Cmp'] / df['Att'] * 100).round(2)
    df['TD%'] = (df['TD'] / df['Att'] * 100).round(2)
    df['Int%'] = (df['Int'] / df['Att'] * 100).round(2)
    df['Sk%'] = (df['Sk'] / df['Att'] * 100).round(2)

    for i in range(len(df['Home/Away'].values)):
        if df['Home/Away'].values[i] == '@':
            df['Home/Away'].values[i] = 'Away'
        else:
            df['Home/Away'].values[i] = 'Home'

    return df


for team, homepage in webpages.items():
    time.sleep(3)
    team_name = team.strip("_")
    temp = read_file(homepage)
    if team_name in qb_dict:
        qb_dict[team_name].append(temp)
    else:
        qb_dict[team_name] = [temp]

print(qb_dict)
