from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

webpages = {
            "TEN": "https://www.pro-football-reference.com/players/H/HenrDe00/gamelog/2022/",
            "LVR": "https://www.pro-football-reference.com/players/J/JacoJo01/gamelog/2022/",
            "CLE": "https://www.pro-football-reference.com/players/C/ChubNi00/gamelog/2022/",
            "NYG": "https://www.pro-football-reference.com/players/B/BarkSa00/gamelog/2022/",
            "PIT": "https://www.pro-football-reference.com/players/H/HarrNa00/gamelog/2022/",
            "MIN": "https://www.pro-football-reference.com/players/C/CookDa01/gamelog/2022/",
            "DET": "https://www.pro-football-reference.com/players/W/WillJa06/gamelog/2022/",
            "PHI": "https://www.pro-football-reference.com/players/S/SandMi01/gamelog/2022/",
            "CAR": "https://www.pro-football-reference.com/players/M/McCaCh01/gamelog/2022/",
            "SFO": "https://www.pro-football-reference.com/players/M/McCaCh01/gamelog/2022/",
            "DAL": "https://www.pro-football-reference.com/players/E/ElliEz00/gamelog/2022/",
            "SEA": "https://www.pro-football-reference.com/players/W/WalkKe00/gamelog/2022/",
            "MIA": "https://www.pro-football-reference.com/players/M/MostRa00/gamelog/2022/",
            "NOR": "https://www.pro-football-reference.com/players/K/KamaAl00/gamelog/2022/",
            "JAX": "https://www.pro-football-reference.com/players/E/EtieTr00/gamelog/2022/",
            "HOU": "https://www.pro-football-reference.com/players/P/PierDa01/gamelog/2022/",
            "GNB": "https://www.pro-football-reference.com/players/J/JoneAa00/gamelog/2022/",
            "ATL": "https://www.pro-football-reference.com/players/A/AllgTy00/gamelog/2022/",
            "CIN": "https://www.pro-football-reference.com/players/M/MixoJo00/gamelog/2022/",
            "NWE": "https://www.pro-football-reference.com/players/S/StevRh00/gamelog/2022/",
            "WAS": "https://www.pro-football-reference.com/players/R/RobiBr01/gamelog/2022/",
            "LAC": "https://www.pro-football-reference.com/players/E/EkelAu00/gamelog/2022/",
            "CAR_": "https://www.pro-football-reference.com/players/F/ForeDO00/gamelog/2022/",
            "CHI": "https://www.pro-football-reference.com/players/M/MontDa01/gamelog/2022/",
            "DAL_": "https://www.pro-football-reference.com/players/P/PollTo00/gamelog/2022/",
            "IND": "https://www.pro-football-reference.com/players/T/TaylJo02/gamelog/2022/",
            "TAM": "https://www.pro-football-reference.com/players/F/FourLe00/gamelog/2022/",
            "LAR": "https://www.pro-football-reference.com/players/A/AkerCa00/gamelog/2022/",
            "GNB_": "https://www.pro-football-reference.com/players/D/DillAJ00/gamelog/2022/",
            "ARI": "https://www.pro-football-reference.com/players/C/ConnJa00/gamelog/2022/",
            "SFO_": "https://www.pro-football-reference.com/players/C/ConnJa00/gamelog/2022/",
            "MIA_": "https://www.pro-football-reference.com/players/C/ConnJa00/gamelog/2022/",
            "NOR_": "https://www.pro-football-reference.com/players/M/MurrLa00/gamelog/2022/",
            "DEN_": "https://www.pro-football-reference.com/players/M/MurrLa00/gamelog/2022/",
            "CHI_": "https://www.pro-football-reference.com/players/H/HerbKh00/gamelog/2022/",
            "ATL_": "https://www.pro-football-reference.com/players/P/PattCo00/gamelog/2022/",
            "WAS_": "https://www.pro-football-reference.com/players/G/GibsAn00/gamelog/2022/",
            "DET_": "https://www.pro-football-reference.com/players/S/SwifDA00/gamelog/2022/",
            "KAN": "https://www.pro-football-reference.com/players/P/PachIs00/gamelog/2022/",
            "BUF": "https://www.pro-football-reference.com/players/S/SingDe00/gamelog/2022/",
            "TAM_": "https://www.pro-football-reference.com/players/W/WhitRa01/gamelog/2022/"
            }

rb_dict = {}


def read_file(homepage):
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
    df = df.iloc[:, list(range(20)) + [-13]]

    df.columns.values[5] = "Home/Away"
    df.columns.values[4] = "Team"
    df.columns.values[-2] = "Catch%"
    df.columns.values[15] = "RecYds"
    df.columns.values[17] = "RecTD"

    relevant_stats = ['Att', 'Yds', 'TD', 'Y/A', 'Tgt', 'Rec', 'RecYds', 'Y/R', 'RecTD', 'Catch%', 'Fmb']

    # if data doesn't have a fumbles category, set column to 0s
    if df.columns.values[-1] != 'Fmb':
        df = df.assign(Fmb=0)

    df = df[['Date', 'Team', 'Home/Away', 'Opp', 'Result'] + relevant_stats]

    df['Result'] = df['Result'].apply(lambda result: 1 if result.startswith('W') else 0)

    for i in relevant_stats:
        df[i] = pd.to_numeric(df[i], errors='coerce').fillna(0)

    # Filter out unplayed games
    df = df[df['Att'] != 0]

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

    if team_name in rb_dict:
        rb_dict[team_name].append(temp)
    else:
        rb_dict[team_name] = [temp]

print(rb_dict)