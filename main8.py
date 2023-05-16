import json

import pandas as pd

data = pd.read_csv('EPL_Set.csv')
pd.set_option('display.max_columns', 11)


def get_data(HomeTeam, Season=None, option=None):
    new_data = data.loc[:, ['HomeTeam', 'Season', 'FTR', 'FTHG']]
    data_json_convert = new_data.to_json(orient='records')
    data_HomeTeam = json.loads(data_json_convert)
    # nr_value = HomeTeam
    # data_HomeTeam = data_json_convert_new_json[]

    if option == 'FTR' and HomeTeam == "Arsenal" and Season == '2017-18':
       data_HomeTeam = [d["FTR","Arsenal"] for d in data_HomeTeam]
    if option == "FTHG":
        data_HomeTeam =[d['FTHG'] for d in data_HomeTeam]


    # hometeamValue = data_HomeTeam['HomeTeam']
    # HomeTeam = hometeamValue
    return data_HomeTeam


if __name__ == "__main__":
    print(get_data(HomeTeam="Arsenal", Season = '2017-18', option="FTR"))

