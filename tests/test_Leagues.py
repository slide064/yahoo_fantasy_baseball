import unittest
import logging
import requests_mock
import os
import json
import fantasy_baseball
import fantasy_baseball.get_url as get_url
import fantasy_baseball.utils

YAHOO_USER = os.environ['YAHOO_USER']
YAHOO_SECRET = os.environ['YAHOO_SECRET']

class TestLeagues(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.account = fantasy_baseball.authenticate(YAHOO_USER, YAHOO_SECRET)
        
    def test_get_leagues(self):
        leagues = self.account.getLeagues()
        league = leagues.get_league(list(leagues.get_league_ids())[0])
        scoreboard = league.get_scoreboard()
        thescoreboard = scoreboard.get_json()
        print(json.dumps(thescoreboard,indent=3))
        pass


if __name__ == '__main__':
    unittest.main()