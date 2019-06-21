#!/usr/bin/python

import unittest
import fantasy_baseball.utils as utils
import fantasy_baseball.utils_xml as parse_xml
import logging
import pickle
import json
from lxml import etree
import os
import pandas

LEAGUE = '431'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
MO_PATH = os.path.dirname(__file__) + "\\mock_objects\\"
PARENT_ROOT=os.path.abspath(os.path.join(SITE_ROOT, os.pardir))


class UtilsTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        with open(PARENT_ROOT + "\\fantasy_baseball\\xml_config.json",'r') as loadJson:
            self.json_file = json.load(loadJson)
        with open(f'{MO_PATH}{LEAGUE}_LEAGUE_STANDINGS.pickle','rb') as loadJson:
            self.xml_standings = pickle.load(loadJson)
        with open(f'{MO_PATH}{LEAGUE}_LEAGUE_SETTINGS.pickle','rb') as loadJson:
            self.xml_settings = pickle.load(loadJson)
    
    def test_namespace(self):
        xml_file = etree.XML(self.xml_standings.content)
        #logging.debug(utils.namespace(xml_file))
        #logging.debug(utils.get_item('team',xml_file))
        #logging.debug(utils.get_items('teams',xml_file))
        pass
    
    def test_parseStandings(self):
        key = self.json_file['standings']
        xml_file = etree.XML(self.xml_standings.content)
        #jsony = parse_xml.parseXML(key, xml_file)
        #print(json.dumps(jsony,indent=4))

    def test_parseSettings(self):
        key = self.json_file['settings']
        xml_file = etree.XML(self.xml_standings.content)
        #jsony = parse_xml.parseXML(key, xml_file)
        #print(json.dumps(jsony,indent=4))

    def test_StandingsNames(self):
        settings_key = self.json_file['settings']
        standings_key = self.json_file['standings']
        xml_file_settings = etree.XML(self.xml_settings.content)
        xml_file_standings = etree.XML(self.xml_standings.content)
        json_settings = parse_xml.parseXML(settings_key, xml_file_settings)
        json_standings = parse_xml.parseXML(standings_key, xml_file_standings)
        stats_lookup = {x:y.get("name") for x,y in utils.deep_get(json_settings, "stat_categories:stats:stat").items() }
        stats_mapped = \
            dict( \
                (key, dict( utils.get_nested_dicts(value.get("team_stats").get("stat"), \
                     stats_lookup) \
                         ) ) \
                         for key, value in json_standings.get("team").items() \
             )
        df = utils.dataFrame(stats_mapped)
        print(df)

if __name__ == '__main__':
    unittest.main()