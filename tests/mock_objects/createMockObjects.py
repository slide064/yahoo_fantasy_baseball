import logging
import pickle
import fantasy_baseball
import os

YAHOO_USER = os.environ['YAHOO_USER']
YAHOO_SECRET = os.environ['YAHOO_SECRET']

URL = 'https://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.'
LEAGUE = '431'

if __name__ == '__main__':
    league_url = f'{URL}{LEAGUE}'
    account = fantasy_baseball.authenticate(YAHOO_USER,YAHOO_SECRET)
    
    #Read in the league settings
    league_info = account.getURL(f'{league_url}')
    league_settings = account.getURL(f'{league_url}/settings')
    league_standings = account.getURL(f'{league_url}/standings')
    league_scoreboard = account.getURL(f'{league_url}/scoreboard')

    pickle.dump(league_info, open(f'{LEAGUE}_LEAGUE_INFO.pickle','wb'))
    pickle.dump(league_settings, open(f'{LEAGUE}_LEAGUE_SETTINGS.pickle','wb'))
    pickle.dump(league_standings, open(f'{LEAGUE}_LEAGUE_STANDINGS.pickle','wb'))
    pickle.dump(league_scoreboard, open(f'{LEAGUE}_LEAGUE_SCOREBOARED.pickle','wb'))

    