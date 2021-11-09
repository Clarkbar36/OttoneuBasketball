import pandas as pd

schedule = pd.read_csv('../Static_Files/nba_schedule.csv')
roster = pd.read_csv('../Static_Files/test_team.csv')

# need to build gameCard class?  IGNORE
gameCard = []
weeklyDeck = []
# need to grab list of players from roster  ** ALEX **


for player in roster:
    # get player name   ** ALEX **
    # get player team   ** ALEX **
    # get position      ** ALEX **
    # get fppg          ** ALEX **
    # get a list of dates according to player team  ** ALEX **
    # for each date in schedule where TEAM = 'BOS'
    # if date > weekStart and date < weekEnd
    gameCard.append(playerName)
    gameCard.append(playerTeam)
    gameCard.append(playerPos)
    gameCard.append(fppg)
    gameCard.append(date)

    weeklyDeck.append(gameCard)  # will become list of all games per player
    gameCard.clear()  # empty gameCard so that we can rebuild with next player /date
