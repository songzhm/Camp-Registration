from src.processor import Processor
import pandas 
from datetime import datetime
from src.person import Applicant

# df = pandas.read_excel('randomdata.xlsx')
df=pandas.read_csv('randomdata.csv')
df.fillna('',inplace=True)
p = Processor()

for index, row in df.iterrows():
    if row['firstName']:
        firstName = row['firstName']
        lastName = row['lastName']
        gender = row['gender']
        dateOfBirth =datetime.strptime(str(row['dateOfBirth']), '%m/%d/%Y').date()
        age =datetime.now().year - dateOfBirth.year
        email = row['email']
        homePhone = row['homePhone']
        cellPhone = row['cellPhone']
        campId = row['campId']
        line1 = row['line1']
        line2 = row['line2']
        city = row['city']
        state = row['state']
        zipCode = row['zipCode']
        emergencyContactName = row['emergencyContactName']
        emergencyContactPhone = row['emergencyContactPhone']
        applicationDate = datetime.strptime(str(row['applicationDate']), '%m/%d/%Y').date()
        reviewDate = datetime.strptime(str(row['reviewDate']), '%m/%d/%Y').date()
        payment = row['payment']
        decisionId = row['decisionId']
        formsChecked = row['formsChecked']
        equipmentsChecked = row['equipmentsChecked']
        bunkhouseId = row['bunkhouseId']
        tribeId = row['tribeId']

        a = Applicant(firstName = firstName,lastName = lastName,age = age,gender = gender,\
        dateOfBirth = dateOfBirth,email = email, homePhone = homePhone, cellPhone = cellPhone,\
        emergencyContactPhone = emergencyContactPhone,emergencyContactName = emergencyContactName,\
        line1 = line1,line2 = line2,city = city,state = state,zipCode = zipCode,payment = payment,
        applicationDate = applicationDate,
        reviewDate = reviewDate,decisionId = decisionId,formsChecked = formsChecked,\
        equipmentsChecked = equipmentsChecked,campId = campId,bunkhouseId = bunkhouseId,\
        tribeId = tribeId)
        
        res = p.addNewApplicant(a)

# p.checkSpaceAvilibility(1,"M")

p.kill()
