from .get_url import Reports
from .scoreboard import Scoreboard
from typing import Generator, Set
import logging

class League(object):
    def __init__(self, api, league_str):
        self.logger = logging.getLogger(__name__)
        self.league_id : str = league_str
        self.json_dict : dict = None
        self.api = api
        self.scoreboard = None

    def get_scoreboard(self):
        if self.scoreboard:
            return self.scoreboard
        else:
            self.scoreboard = Scoreboard(self.api, self.league_id)
            return self.scoreboard
        
class LeagueSettings(object):
    def __init__(self, json_dict: dict):
        self.json_dict = json_dict
    
