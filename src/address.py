class Address(object):
    def __init__(self, line1, line2, city, state, zipCode):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def __str__(self):
        return 'Line 1:' + self.line1 + '\n' + 'Line 2:' + self.line2 + \
        '\n' + 'City:' + self.city + '\n' + 'Sate: ' + self.state + '\n' + \
        'Zip Code: ' + str(self.zipCode)

    def __repr__(self):
        return str(self)

# add = [Address('asdfas','asdfa','asdfasd','asdfa',91712),Address('asdfas','asdfa','asdfasd','asdfa',91712)]

# print(add)