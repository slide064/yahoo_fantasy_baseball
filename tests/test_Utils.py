#!/usr/bin/python

import unittest
import fantasy_baseball.utils as utils
import fantasy_baseball.parse_xml as parse_xml
import logging
import pickle
import json
from lxml import etree
import os

URL = 'https://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.'
LEAGUE = '431'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
MO_PATH = os.path.dirname(__file__) + "\\mock_objects\\"
PARENT_ROOT=os.path.abspath(os.path.join(SITE_ROOT, os.pardir))


class UtilsTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        with open(PARENT_ROOT + "\\fantasy_baseball\\xml_config.json",'r') as loadJson:
            self.json_file = json.load(loadJson)
    
    def test_namespace(self):
        with open(f'{MO_PATH}{LEAGUE}_LEAGUE_STANDINGS.pickle','rb') as loadJson:
            xml_pickle = pickle.load(loadJson)
        xml_file = etree.XML(xml_pickle.content)
        #logging.debug(utils.namespace(xml_file))
        #logging.debug(utils.get_item('team',xml_file))
        #logging.debug(utils.get_items('teams',xml_file))
        pass
    
    def test_parseStandings(self):
        with open(f'{MO_PATH}{LEAGUE}_LEAGUE_STANDINGS.pickle','rb') as loadJson:
            xml_pickle = pickle.load(loadJson)
        key = self.json_file['standings']
        xml_file = etree.XML(xml_pickle.content)
        #jsony = parse_xml.parseXML(key, xml_file)
        #print(json.dumps(jsony,indent=4))

    def test_parseSettings(self):
        with open(f'{MO_PATH}{LEAGUE}_LEAGUE_SETTINGS.pickle','rb') as loadJson:
            xml_pickle = pickle.load(loadJson)
        key = self.json_file['settings']
        xml_file = etree.XML(xml_pickle.content)
        #jsony = parse_xml.parseXML(key, xml_file)
        #print(json.dumps(jsony,indent=4))

    def test_StandingsNames(self):
        with open(f'{MO_PATH}{LEAGUE}_LEAGUE_SETTINGS.pickle','rb') as loadJson:
            xml_settings = pickle.load(loadJson)
        with open(f'{MO_PATH}{LEAGUE}_LEAGUE_STANDINGS.pickle','rb') as loadJson:
            xml_standings= pickle.load(loadJson)
        settings_key = self.json_file['settings']
        standings_key = self.json_file['standings']
        xml_file_settings = etree.XML(xml_settings.content)
        xml_file_standings = etree.XML(xml_standings.content)
        json_settings = parse_xml.parseXML(settings_key, xml_file_settings)
        json_standings = parse_xml.parseXML(standings_key, xml_file_standings)
        get_nested_dict = utils.deep_get(json_settings, "stat_categories:stats:stat")
        print( \
            dict( \
                utils.get_nested_dicts( json_standings.get("team").get("388.l.431.t.3").get("team_stats").get("stat"),get_nested_dict) \
                ) \
            )
        print( json.dumps(
            dict( \
                (key, dict( utils.get_nested_dicts_test(value.get("team_stats").get("stat"), \
                     get_nested_dict \
                     , lambda x: x.get("name") ) \
                         ) ) \
                         for key, value in json_standings.get("team").items() \
             ) \
            ,indent=4))
        
        #print(utils.map_values_dict(json_standings,"team:**:team_stats:stat:*",json_settings,"stat_categories:stats:stat"))
        


if __name__ == '__main__':
    unittest.main()