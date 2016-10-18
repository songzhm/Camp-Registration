
class LetterOfAcceptance(object):

    def __init__(self, decisionId, camp):
        self.decisionId = decisionId
        self.camp = camp

    def generateLetter(self):
        res = ''
        if self.decisionId ==1 :
            res += 'Welcome to '+ self.camp.name +'! '
            res += 'The camp will start from ' + str(self.camp.startDate) + ' to '+ \
            str(self.camp.endDate) + '.\n'

            res += 'Please make sure bring the following forms and equipments:\n'
            res += 'Forms:\n'+ str(Forms()) + '\n'
            res += 'Equipments:\n' + str(Equipments()) + '\n'

        elif self.decisionId ==2 :
            res += 'Welcome to '+ self.camp.name +'! '
            res += 'The camp will start from ' + str(self.camp.startDate) + ' to '+ \
            str(self.camp.endDate) + '.\n'
            res += 'Your space has been reserved, '
            res += 'but please make sure make the payment before the camp starts.'


            res += 'Please make sure bring the following forms and equipments:\n'
            res += 'Forms:\n'+ str(Forms()) + '\n'
            res += 'Equipments:\n' + str(Equipments()) + '\n'
        elif self.decisionId ==3 :
            res += 'Thank you for interesting in camping with us!'
            res += '\nHowever, your application cannot be accepted because we only accept applicant within age 9-18 and when there is enough empty space in the camp you interested.'
            
        else:
            res += 'Decision has not been made.'

        return res


class Forms(object):
    def __init__(self):
        self.forms = ['medical', 'legal', 'emergency contact']

    def __str__(self):

        res = ''

        for form in self.forms:
            res+='* '+ form + '\n'

        return res

class Equipments(object):
    def __init__(self):
        self.equipments = ['riding helmet','boots', 'sleeping bag', \
        'water bottle', 'sun screen', 'bug spray', 'lights']
    
    def __str__(self):
        res = ''

        for equipment in self.equipments:
            res+='* ' + equipment + '\n'
        
        return res