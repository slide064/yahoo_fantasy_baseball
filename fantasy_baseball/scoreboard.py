import logging
from .get_url import Reports

class Scoreboard:
    def __init__(self, api, league_id):
        self.api = api
        self.league_id = league_id
        self.weeks : dict = {}

    def get_json(self):
        return self.api(Reports.SCOREBOARD,**{"LEAGUE":self.league_id})
    
