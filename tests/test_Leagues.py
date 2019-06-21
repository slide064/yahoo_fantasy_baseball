import unittest
import logging
import requests_mock
import os
import fantasy_baseball
import fantasy_baseball.league as league
import fantasy_baseball.get_url as get_url
import fantasy_baseball.utils

YAHOO_USER = os.environ['YAHOO_USER']
YAHOO_SECRET = os.environ['YAHOO_SECRET']

class TestLeagues(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        account = fantasy_baseball.authenticate(YAHOO_USER, YAHOO_SECRET)
        self.getjson = account.getJSON()
        
    def test_get_leagues(self):
        parameters = {"LEAGUE":"88.l.8017"}
        all_seasons : dict = self.getjson(get_url.Reports.ALL_LEAGUES, **parameters)
        parameters["LEAGUE"] = next(iter(all_seasons.get("league")))
        league_settings : dict = self.getjson(get_url.Reports.SETTINGS,**parameters)
        leagues = league.Leagues(all_seasons)
        pass


if __name__ == '__main__':
    unittest.main()