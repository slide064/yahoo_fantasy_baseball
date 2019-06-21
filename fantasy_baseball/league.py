from typing import Generator, Set
import logging
from fantasy_baseball.utils import singleton

class League(object):
    def __init__(self, team: dict):
        self._key = team.get('team_key')
        self._id = team.get('team_id')
        self._name = team.get('name')

class Leagues(object):
    def __init__(self, league_dict):
        self.leagues = league_dict.get('league')

    def get_league_names(self) -> Generator:
        return (x.get('name') for y, x in self.leagues.items())
    
    def get_seasons(self) -> Generator:
        return (x.get('season') for y, x in self.leagues.items())

    def get_league_ids(self) -> Generator:
        return (x for x in self.leagues)

    def get_league_set(self) -> Generator:
        return ((x, y['season'], y['name']) for x,y in self.leagues.items())

    def get_filtered(self, season='', name=''):
        """
        Pass it season or name, or both
        """
        return (x for x in self.get_league_set() if season in x[1] and name in x[2])
