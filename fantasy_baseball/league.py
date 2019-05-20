import logging

class League(object):
    def __init__(self, id):
        self._id = id
        teams = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    

if __name__ == '__main__':
    league = League('8017')
    print(league.id)
    