from lxml import etree
from .utils import get_item, get_items
import sys

def parseXML(dict_key : dict, xml: etree._Element) -> dict:
    """
    Reads the XML and returns a dict with
    in the same format.
    """
    passDict : dict = {}
    for key, value in dict_key.items():
        if '/' not in key:
            if not isinstance(value, dict):
                passDict.update({key : get_item(key, xml).text})
            else:
                passDict.update({ key : parseXML(value, get_item(key, xml) ) })
        else:
            current_dict = {}
            key_name = key.split("/")
            if not isinstance(value, dict):
                for subKey in get_items(key_name[0], xml):
                    current_dict.update({get_item(key_name[1],subKey).text : get_item(value,subKey).text })
            else:
                for items in get_items(key_name[0], xml):
                    item_id = get_item(key_name[1], items).text
                    current_dict.update({ item_id : parseXML(value, items) })
                #    parseXML(key, items)
            passDict.update({key_name[0] : current_dict})
    return passDict