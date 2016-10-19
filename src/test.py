from processor import *
import csv
from pprint import pprint

file = open('applicants.csv','r') 

reader = csv.reader(file)

rawData = list(reader)

cols = rawData[0]
data = rawData[1::]

applicants = []

for record in data:
    d = {}
    for i in range(len(cols)):
        d[cols[i]] = record[i]
    applicants.append(d)


p = Processor()

for applicant in applicants:
    p.addNewApplicant(applicant)

res = p.interacteDB('select','applicant','gender = \'M\'')



# print(p.camps)
p.kill()

# print("processor is running, counting for 5")
# for i in range(5):
#     print(i+1)
#     time.sleep(1)



# p.kill()