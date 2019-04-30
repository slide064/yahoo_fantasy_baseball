from auth import Auth
from teams import Matchups

class Account(object):

    def __init__(self,auth_obj):
        self.client = auth_obj
        self.matchups = Matchups()

    def get_matchups(self):
        """ 
        Returns json object of all matchups 
        """
        r = self.client.get_url('https://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.8017/scoreboard')
        self.matchups.update(r)
        print(self.matchups)
    
    def get_teams(self):
        """
        Returns json object of all the teams
        """
        return 0