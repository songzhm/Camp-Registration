class Camp(object):
    def __init__(self, id, name, startDate, endDate,totalCapacity):
        self.id = id
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.numberOfGirlBunkhouses = 3
        self.numberOfBoyBunkhouses = 3
        self.totalGrilNumber = 36
        self.totalBoyNumber = 36
        self.totalCapacity = totalCapacity

class Bunkhouse(object):
    def __init__(self, id, name,gender):
        self.id = id
        self.name = name
        self.gender = gender
        self.campers = []

class Tribe(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.campers = []
