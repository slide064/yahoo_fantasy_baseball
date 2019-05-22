import unittest
import requests_mock
import os
import fantasy_baseball

YAHOO_USER = os.environ['YAHOO_USER']
YAHOO_SECRET = os.environ['YAHOO_SECRET']

URL = 'https://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.'
LEAGUE = '431'

@requests_mock.Mocker()
class TestLeagues(unittest.TestCase):
    def setUp(self, m):
        
        # Load in all the mock objects
        path = os.path.dirname(__file__)
        
        pass
    
    def no(self):
        pass