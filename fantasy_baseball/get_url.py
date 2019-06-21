import fantasy_baseball.utils_xml as utils_xml
from typing import Any
from enum import Enum
import json
import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
JSON_PATH = os.path.dirname(__file__) + "\\xml_config.json"

default = {
    "LEAGUE" : "431"
}

class Reports(Enum):
    ALL_LEAGUES = "all_leagues"
    STANDINGS = "standings"
    SETTINGS = "settings"
    SCOREBOARD = "scoreboard"

def get_url(get_function: Any):
    with open(JSON_PATH,'r') as openfile:
        json_config = json.load(openfile)
    def get_json(report_type: Reports,filters = '', **kwargs):
        rp = json_config.get(report_type.value)
        content_dict = utils_xml.parseRequest(rp.get("json_key"), get_function(rp.get("URL").format(**kwargs)+ filters))
        return content_dict
    return get_json