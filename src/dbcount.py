import cursor as cursor
from processor import processor
p= Processor()
totalgirls = 36
totalboys = 36

def func(campid,gender):
    res= p.interactDB('select','applicant','gender = \'{g}\' and campid = {c}'.format(g=gender,c=campId))
    if res['ok'] == True:
        data = res['result']
        gender_per_camp = len(data)
        print(gender_per_camp)
   else:
        print ('error')
cursor.execute("select count(*) from applicants where gender = 'M'")
print(list(cursor))
from processor import Counter
boys = ["M"]
girls = ["F"]
f = counter(girls)
m = counter(boys)
t = f + m
print "Total applicants", t
gendercap = list(cursor))
print "Count of girls:", gendercap.count('F')
print "Count of boys:", gendercap.count('M')
print "Total applicant for camp", gendercap.count('F')+gendercap.count('M')
gendercap.count("M")
if f < 36
    print "available capacity"
else:
    print "female capacity exceeded"
if m < 36
    print "available capacity"
else:
    print "male capacity exceeded"
p.kill()