import pandas as pd
import numpy as np

def pull_roster(lgID, tmID):

    ottoneu_tbl = pd.read_html("https://ottoneu.fangraphs.com/basketball/%s/lineup/%s" % (lgID, tmID))[0]
    ottoneu_tbl = ottoneu_tbl[ottoneu_tbl.Name != "-"]
    ottoneu_tbl[['firstName', 'lastName', 'suffix', 'position', 'salary', 'placeholder', 'placeholder2', 'game']] = \
    ottoneu_tbl[
        "Name"].str.split(" ", n=7, expand=True)
    ottoneu_tbl['team'] = np.where(ottoneu_tbl.suffix.str.isupper(), ottoneu_tbl["suffix"], ottoneu_tbl['position'])
    ottoneu_tbl['position'] = np.where(ottoneu_tbl['position'] == ottoneu_tbl['team'], ottoneu_tbl["salary"],
                                       ottoneu_tbl['position'])
    ottoneu_tbl['injury_status'] = np.where(ottoneu_tbl['salary'].str.contains("GTD|O"), ottoneu_tbl["salary"],
                                            np.where(ottoneu_tbl['placeholder'].str.contains("GTD|O"),
                                                     ottoneu_tbl["placeholder"], ""))
    ottoneu_tbl['salary'] = np.where(ottoneu_tbl['salary'].str.contains("\$"), ottoneu_tbl["salary"],
                                     np.where(ottoneu_tbl['placeholder'].str.contains("\$"), ottoneu_tbl["placeholder"],
                                              ottoneu_tbl['placeholder2']))
    ottoneu_tbl['suffix'] = np.where(ottoneu_tbl.suffix.str.isupper(), ' ', ottoneu_tbl["suffix"])
    ottoneu_tbl["player"] = ottoneu_tbl["firstName"] + ' ' + ottoneu_tbl["lastName"] + ' ' + ottoneu_tbl["suffix"]
    ottoneu_tbl = ottoneu_tbl.drop(
        columns=['placeholder', 'placeholder2', 'game', 'firstName', 'lastName', 'suffix', 'Position', 'Name'])
    cols_to_move = ['player', 'position', 'salary', 'team', 'injury_status']
    ottoneu_tbl = ottoneu_tbl[cols_to_move + [col for col in ottoneu_tbl.columns if col not in cols_to_move]]
    ottoneu_tbl = ottoneu_tbl.reset_index(drop = True)
    ottoneu_tbl.player = ottoneu_tbl.player.str.strip()
    ottoneu_tbl.fillna('', inplace=True)

    return(ottoneu_tbl)

user_lgID = '20'
user_tmID = '81'

roster = pull_roster(user_lgID, user_tmID)

#ottoneu_tbl.to_csv('Static_Files/test_team.csv', index=False)
