from lxml import etree
import logging
import sys

def parseRequest(dict_key: dict, request):
    cont = etree.XML(request.content)
    return parseXML(dict_key, cont)

def parseXML(dict_key : dict, xml: etree._Element) -> dict:
    """
    Reads the XML and returns a dict in the same structure as the 
    dict_key.
    """
    passDict : dict = {}
    for key, value in dict_key.items():
        # Treat special cases. Often these are multiple items
        # that need to be mapped to an internal key or 
        # multiple items that need to be stored in a set
        if '/' in key:
            current_dict = {}
            key_name = key.split("/")
            if not isinstance(value, dict):
                for subKey in get_items(key_name[0], xml):
                    current_dict.update({get_item(key_name[1],subKey).text : get_item(value,subKey).text })
            else:
                for items in get_items(key_name[0], xml):
                    item_id = get_item(key_name[1], items).text
                    current_dict.update({ item_id : parseXML(value, items) })
            passDict.update({key_name[0] : current_dict})
        elif '*' in key:
            key_name : str = key.split('*')
            #TODO allow for the option of a set of dicts with no key
            #Example - matchups*matchup
            passDict.update({key_name[0] : tuple({key_name[1] : parseXML(value,x)} for x in get_items(key_name[1], xml) )})
        else:
            if not isinstance(value, dict):
                mappedValues = getTextValue(get_item)(key.split("|"), xml)
                passDict.update(next(mappedValues))
            else:
                passDict.update({ key : parseXML(value, get_item(key, xml) ) })
    return passDict

def getTextValue(f):
    def returnKeyValue(keys, xml):
        def returnValidText(key):
            a = None
            try:
                a = f(key,xml).text
            except:
                logging.warning(f'{key} not found in list')
            return a
        return ({key:returnValidText(key)} for key in keys if returnValidText(key))
    return returnKeyValue

def get_item(name : str, xml : etree._Element):
    return xml.find(f'.//NS:{name}',namespace(xml))

def get_items(name : str, xml : etree._Element):
    return xml.findall(f'.//NS:{name}',namespace(xml))

def namespace(xml : etree._Element) -> dict:
    """
    Removes the namespaces and returns only
    namespaces that are valid
    """
    return {"NS":y for x,y in xml.nsmap.items() if not x}