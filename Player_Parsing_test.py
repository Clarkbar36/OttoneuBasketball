import pandas as pd
import numpy as np

lgID = '20'
tmID = '81'

ottoneu_tbl = pd.read_html("https://ottoneu.fangraphs.com/basketball/%s/lineup/%s" % (lgID, tmID))[0]
ottoneu_tbl = ottoneu_tbl[ottoneu_tbl.Name != "-"]
ottoneu_tbl[['firstName', 'lastName', 'suffix', 'position', 'salary', 'placeholder', 'placeholder2', 'game']] = ottoneu_tbl[
    "Name"].str.split(" ", n=7, expand=True)
ottoneu_tbl['team'] = np.where(ottoneu_tbl.suffix.str.isupper(), ottoneu_tbl["suffix"], ottoneu_tbl['position'])
ottoneu_tbl['position'] = np.where(ottoneu_tbl['position'] == ottoneu_tbl['team'], ottoneu_tbl["salary"],
                                   ottoneu_tbl['position'])
ottoneu_tbl['injury_status'] = np.where(ottoneu_tbl['placeholder'].str.contains("GTD|O"), ottoneu_tbl["placeholder"], "")
ottoneu_tbl['salary'] = np.where(ottoneu_tbl['salary'].str.contains("\$"), ottoneu_tbl["salary"],
                                 np.where(ottoneu_tbl['placeholder'].str.contains("\$"), ottoneu_tbl["placeholder"], ottoneu_tbl['placeholder2']))
ottoneu_tbl['suffix'] = np.where(ottoneu_tbl.suffix.str.isupper(), ' ', ottoneu_tbl["suffix"])
ottoneu_tbl["player"] = ottoneu_tbl["firstName"] + ' ' + ottoneu_tbl["lastName"] + ' ' + ottoneu_tbl["suffix"]
ottoneu_tbl = ottoneu_tbl.drop(columns=['placeholder', 'placeholder2', 'game', 'firstName', 'lastName', 'suffix', 'Position', 'Name'])
