from typing import Generator, Set
from fantasy_baseball.get_url import Reports
from .league import League
import logging

class Leagues(object):
    def __init__(self, api):
        self.api = api
        self.json_dict = api(Reports.ALL_LEAGUES).get('league')

    def get_league_names(self) -> Generator:
        return (x.get('name') for y, x in self.json_dict.items())
    
    def get_seasons(self) -> Generator:
        return (x.get('season') for y, x in self.json_dict.items())

    def get_league_ids(self) -> Generator:
        return (x for x in self.json_dict)

    def get_league_set(self) -> Generator:
        return ((x, y['season'], y['name']) for x,y in self.json_dict.items())

    def get_filtered(self, season='', name=''):
        """
        Pass it season or name, or both
        """
        return (x for x in self.get_league_set() if season in x[1] and name in x[2])

    def get_league(self,league_id):
        return League(self.api, league_id)
