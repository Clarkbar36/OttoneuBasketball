import pandas as pd
import datetime
pd.options.mode.chained_assignment = None

date_cols = ['ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM',
             'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']
schedule = pd.read_csv('Static_Files/nba_schedule.csv', parse_dates=date_cols)
roster = pd.read_csv('Static_Files/test_team.csv')

# need to formulate this
weekStart = datetime.datetime(2021, 11, 1)  # '11/1/2021'
weekEnd = datetime.datetime(2021, 11, 7)  # '11/7/2021'

unique_tms = roster.team.unique().tolist()

weeks_games = []
# unique_tms = unique_tms[:1]
for tm in unique_tms:
    tm_sched = schedule[[tm]]
    in_week = (tm_sched[tm] >= weekStart) & (tm_sched[tm] <= weekEnd)
    games = tm_sched.loc[in_week]
    games['team'] = tm
    games = games.rename(columns={games.columns[0]: 'gm_dt'})
    games = games.reset_index(drop=True)
    weeks_games.append(games)

all_weeks_games = pd.concat(weeks_games)

roster_to_join = roster[["player", "position", "team", "injury_status", "Mins", "Fan. Pts"]]

all_cards = roster_to_join.merge(all_weeks_games, on='team', how='right')

all_cards = all_cards.sort_values(by=['player', 'gm_dt'])

all_cards['count'] = all_cards.groupby(['player']).cumcount()+1

#all_cards = all_cards.reset_index(drop = True)

all_cards = all_cards.set_index(['player', 'count'])

## Begin object work below


player_deck = all_cards.values.tolist()
gm_date = player_deck[0][5]
print(gm_date)
gm_date2 = gm_date.strftime("%m/%d/%y")
print(gm_date2)



