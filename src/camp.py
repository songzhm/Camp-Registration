class Camp(object):
    def __init__(self, id, name, tribes, bunkhouses, startDate, endDate):
        self.id = id
        self.name = name
        self.tribes = tribes
        self.bunkhouses = bunkhouses
        self.startDate = startDate
        self.endDate = endDate

class Bunkhouse(object):
    def __init__(self, id, name, campers):
        self.id = id
        self.name = name
        self.campers = campers

class Tribe(object):
    def __init__(self, id, name, campers):
        self.id = id
        self.name = name
        self.campers = campers

