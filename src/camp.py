class Camp(object):
    def __init__(self, id, name, startDate, endDate, totalCapacity):
        self.id = id
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.totalCapacity = totalCapacity

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

