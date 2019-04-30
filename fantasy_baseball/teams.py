from lxml import etree
import utils as utils

class Matchups(object):

    def __init__(self):
        self.content = None
        self.matchups_xml = None
        self.matchups = None

    
    def update(self, xml_content):
        root = etree.XML(xml_content.content)
        self.content = utils.remove_namespaces_qname(root)
        self.matchups_xml = self.content[0].find(u'scoreboard').find('matchups').findall("matchup")
        matchups_array = []
        for match in self.matchups_xml:
            matchups_array.append(Matchup(match.find('teams')))
        self.matchups = matchups_array
    
    def __str__(self):
        return_str = ""
        for x in self.matchups:
            return_str = return_str + x.__str__() + "\n"
        return return_str


class Team(object):

    def __init__(self,matchup_data):
        self.name = matchup_data.find('name').text
        self.score = matchup_data.find('team_points').find('total').text

class Matchup(object):
    
    def __init__(self,matchup):
        matchups = matchup.findall('team')
        self.team1 = Team(matchups[0])
        self.team2 = Team(matchups[1])

    def __str__(self):
        return self.team1.score + " " + self.team1.name + " --- " + self.team2.name + " " + self.team2.score