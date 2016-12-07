import datetime
from src.address import *

class Person(object):
    def __init__(self,firstName, lastName,age,gender,dateOfBirth,email):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.email = email
    
    # def __str__(self):
    #     return 'First Name: ' + self.firstName + '\n' + 'Last Name: ' + \
    #     self.lastName + '\n' + 'Age: ' + self.age + '\n' + 'Gender: ' + \
    #     self.gender + '\n' + 'Date of Birth: ' + self.dateOfBirth + '\n' + \
    #     'Email: ' + self.email
    
    # def __repr__(self):
    #     return str(self)


# class Employee(Person):
#     def __init__(self,firstName, lastName, age, gender, dateOfBirth, \
#     email, position, userName = "xxx", password = "xxx"):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age
#         self.gender = gender
#         self.dateOfBirth = dateOfBirth
#         self.email = email
#         self.position = position
#         self.__userName = userName
#         self.__password = password
    
#     def __str__(self):
#         return 'First Name: ' + self.firstName + '\n' + 'Last Name: ' + \
#         self.lastName + '\n' + 'Age: ' + str(self.age) + '\n' + 'Gender: ' + \
#         self.gender + '\n' + 'Date of Birth: ' + self.dateOfBirth + '\n' + \
#         'Email: ' + self.email + '\n' + 'position: ' + self.position 
    
#     def __repr__(self):
#         return str(self)

#     def setUserName(userName):
#         self.__userName = userName
    
#     def setPassword(password):
#         self.__password = password
    
#     def getUserName(self):
#         return self.__userName
    
#     def getPassword(self):
#         return self.__password

class Applicant(Person):
    def __init__(self,firstName, lastName,age,gender,dateOfBirth,email, \
    homePhone, cellPhone,emergencyContactPhone, emergencyContactName, \
    line1, line2, city, state, zipCode, \
    payment=False, applicationDate=datetime.datetime.now(), \
    reviewDate=datetime.datetime.now(),  decisionId=0, \
    formsChecked=False, equipmentsChecked=False, campId=0, bunkhouseId=0, \
    tribeId=0):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.homePhone = homePhone
        self.cellPhone = cellPhone
        self.emergencyContactPhone = emergencyContactPhone
        self.emergencyContactName = emergencyContactName
        self.payment = payment
        self.applicationDate = applicationDate
        self.reviewDate = reviewDate
        self.decisionId = decisionId
        self.formsChecked = formsChecked
        self.equipmentsChecked = equipmentsChecked
        self.campId = campId
        self.bunkhouseId = bunkhouseId
        self.tribeId = tribeId
        self.address = Address(line1, line2, city, state, zipCode)


# emp = Employee('aaa', 'aaaa', 1, 'M', 'asdfasdf', 'asd', 'asdfasdf')

