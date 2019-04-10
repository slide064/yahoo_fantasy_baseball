import Assets.keys as keys
from fantasy_baseball.auth import Auth
import fantasy_baseball.utils as utils
from lxml import etree

client = Auth(keys)
r = client.get_url('https://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.8017/scoreboard')
root = etree.XML(r.content)
cleaned =  utils.remove_namespaces_qname(root)
print(cleaned[0].find(u'scoreboard').find('matchups').findall("matchup"))