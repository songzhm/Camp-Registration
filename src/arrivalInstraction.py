
class LetterOfAcceptance(object):

    def __init__(self, applicant, camp):
        self.applicant = applicant
        self.camp = camp

    def generateLetter(self):
        res = ''
        if self.applicant.decisionId ==1 :
            res += 'Welcome to '+ camp.name +'! '
            res += 'The camp will start from ' + str(camp.startDate) + ' to '+ \
            str(camp.endDate) + '.\n'

            res += 'Please make sure bring the following forms and equipments:\n'
            res += 'Forms:\n'+ str(Forms()) + '\n'
            res += 'Equipments:\n' + str(Equipments()) + '\n'

        elif self.applicant.decisionId ==2 :
            res += 'Welcome to '+ camp.name +'! '
            res += 'The camp will start from ' + str(camp.startDate) + ' to '+ \
            str(camp.endDate) + '.\n'
            res += 'Your space has been reserved, '
            res += 'but please make sure make the payment before the camp starts.'
            res += 'The camp will start from ' + str(camp.startDate) + ' to '+ \
            str(camp.endDate) + '.\n'

            res += 'Please make sure bring the following forms and equipments:\n'
            res += 'Forms:\n'+ str(Forms()) + '\n'
            res += 'Equipments:\n' + str(Equipments()) + '\n'
        elif self.applicant.decisionId ==3 :
            res += 'Thank you for interesting in camping with us!'
            res += 'However, your application cannot be accepted because we only accept applicant within age 9-18.'
            
        else:
            res += 'Decision has not been made.'

        return res


class Forms(object):
    def __init__(self):
        self.forms = ['medical', 'legal', 'emergency contact']

    def __str__(self):

        res = ''

        for form in forms:
            res+='* '+ form + '\n'

        return res

class Equipments(object):
    def __init__(self):
        self.equipments = ['riding helmet','boots', 'sleeping bag', \
        'water bottle', 'sun screen', 'bug spray', 'lights']
    
    def __str__(self):
        res = ''

        for equipment in equipments:
            res+='* ' + form + '\n'
        
        return res