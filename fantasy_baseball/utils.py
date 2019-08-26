# encoding: utf-8
from lxml import etree
from typing import Optional, Any
from functools import reduce
import logging
import logging.config
import json
import os

def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO
):
    """Setup logging configuration

    """
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        print("defaultlevel")

def get_nested_dicts(dict_map: dict, dict_lookup: dict) -> dict:
    return {(dict_lookup.get(k),v) for k,v in dict_map.items() if dict_lookup.get(k)}

def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split(":"), dictionary)

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton(*args, **kw):
        if kw['filename'] not in instances:
            instances[kw['filename']] = cls(*args,**kw)
        return instances[kw['filename']]
    return _singleton

def dataFrame(dict: dict):
    import pandas
    return pandas.DataFrame.from_dict(dict, orient='index')