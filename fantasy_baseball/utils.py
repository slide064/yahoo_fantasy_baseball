# encoding: utf-8
from lxml import etree
from typing import Optional, Any
from functools import reduce
import logging

def get_item(name : str, xml : etree._Element):
    #xml = remove_namespaces_qname(xml,namespace = namespace(xml))
    #{x.find(find(name)).text : x.find(find('name')).text for x in testXML.findall(find('team'))}
    return xml.find(f'.//NS:{name}',namespace(xml))

def get_items(name : str, xml : etree._Element):
    #xml = remove_namespaces_qname(xml,namespace = namespace(xml))
    #{x.find(find(name)).text : x.find(find('name')).text for x in testXML.findall(find('team'))}
    return xml.findall(f'.//NS:{name}',namespace(xml))

def namespace(xml : etree._Element) -> dict:
    """
    Removes the namespaces and returns only
    namespaces that are valid
    """
    return {"NS":y for x,y in xml.nsmap.items() if not x}

def remove_namespaces_qname(doc, namespaces = None):
    for el in doc.getiterator():
        # clean tag
        q = etree.QName(el.tag)
        if q is not None:
            if namespaces is not None:
                if q.namespace in namespaces:
                    el.tag = q.localname
            else:
                el.tag = q.localname
            # clean attributes
            for a, v in el.items():
                q = etree.QName(a)
                if q is not None:
                    if namespaces is not None:
                        if q.namespace in namespaces:
                            del el.attrib[a]
                            el.attrib[q.localname] = v
                    else:
                        del el.attrib[a]
                        el.attrib[q.localname] = v
    return doc

def map_values_dict(dict_map: dict, dict_key: str, read_dict_map: dict, read_dict_key: str) -> dict:
    get_nested_dict = deep_get(read_dict_map, read_dict_key)
    print(get_nested_dict)
    def map_dict(dict_map: dict, dict_key: str) -> dict:
        #dict_keys = dict_key.split(":")
        #dicts = get_nested_dicts(dict_map,dict_key)
        return {}
    return map_dict(dict_map, dict_key)

def get_nested_dicts(dict_map: dict, dict_lookup: dict) -> dict:
    return {(dict_lookup.get(k).get("name"),v) for k,v in dict_map.items() if dict_lookup.get(k)}

def get_nested_dicts_test(dict_map: dict, dict_lookup: dict, f: Any = None) -> dict:
    if not f:
        f = lambda x: x
    return {(f(dict_lookup.get(k)),v) for k,v in dict_map.items() if dict_lookup.get(k)}


def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split(":"), dictionary)