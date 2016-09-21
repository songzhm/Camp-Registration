import os
import sqlite3
import datetime

db_filename = '..\db\camp.db'
schema_filename = '..\db\camp_schema.sql'


db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        decisions = {'1':'acceptance', '2':'conditional acceptance', '3':'denial'}
        
        for key, value in decisions.items():

            conn.execute("""
            insert into decisions (decision_id, decision_description)
            values ({},\'{}\')
            """.format(int(key),str(value))
            )

        bunkhouses = {'1':{'name':'b1','gender':'M'},
        '2':{'name':'b2','gender':'M'},
        '3':{'name':'b3','gender':'M'},
        '4':{'name':'g1','gender':'F'},
        '5':{'name':'g2','gender':'F'},
        '6':{'name':'g3','gender':'F'}}

        for key, value in bunkhouses.items():
            conn.execute("""
            insert into bunkhouses (bunkhouse_id, name,gender)
            values ({},\'{}\',\'{}\')
            """.format(int(key),value['name'],value['gender'])
            )

        tribes = {'1':{'name':'t1'},
        '2':{'name':'t2'},
        '3':{'name':'t3'},
        '4':{'name':'t4'},
        '5':{'name':'t5'},
        '6':{'name':'t6'}}

        for key, value in tribes.items():
            conn.execute("""
            insert into tribes (tribe_id, name)
            values ({},\'{}\')
            """.format(int(key),value['name'])
            )
    
        camps = {'1':{'start_date':datetime.date(2016, 6, 6),'end_date':datetime.date(2016, 6, 19)},
        '2':{'start_date':datetime.date(2016, 7, 4),'end_date':datetime.date(2016, 7, 17)},
        '3':{'start_date':datetime.date(2016, 8, 8),'end_date':datetime.date(2016, 8, 21)}}

        for key, value in camps.items():
            conn.execute("""
            insert into camps (camp_id, start_date,end_date)
            values ({},\'{}\',\'{}\')
            """.format(int(key),value['start_date'],value['end_date'])
            )
            

        
    else:
        print('Database exists, assume schema does, too.')