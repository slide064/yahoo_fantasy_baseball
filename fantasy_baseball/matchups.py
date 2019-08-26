from lxml import etree
from .utils import remove_namespaces_qname

class Matchups(object):

    def __init__(self):
        self.content = None
        self.matchups_xml = None
        self.matchups = None
    
    def update(self, xml_content):
        root = etree.XML(xml_content.content)
        self.content = remove_namespaces_qname(root)
        self.matchups_xml = self.content[0].find(u'scoreboard').find('matchups').findall("matchup")
        matchups_array = []
        for match in self.matchups_xml:
            matchups_array.append(Matchup(match.find('teams')))
        self.matchups = matchups_array

    def get_matchup_array(self):
        match_array = []
        for matchup in self.matchups:
            match_array.append(matchup.get_matchup_json())
        return match_array

    def get_shortened_string_array(self):
        shortened_array = []
        for x in self.get_matchup_array():
            theString = ""
            theString += str(int(float(x['team_1']['score']))) + " " + x['team_1']['name'][:5]
            theString += " - "
            theString += x['team_2']['name'][:5] + " " + str(int(float(x['team_2']['score'])))
            shortened_array.append(theString)
        return shortened_array
    
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
    
    def get_matchup_json(self):
        mj = {
            'team_1' : {
                'name' : self.team1.name,
                'score' : self.team1.score
            },
            'team_2' : {
                'name' : self.team2.name,
                'score' : self.team2.score
            }
        }
        return mj        

    def __str__(self):
        return self.team1.score + " " + self.team1.name + " --- " + self.team2.name + " " + self.team2.score