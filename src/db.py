import datetime
import os
import sqlite3


class DB(object):
    def __init__(self, dbFile, schemaFile):
        
        self.dbFile = dbFile
        self.schemaFile = schemaFile

        db_is_new = not os.path.exists(self.dbFile)

        

        with sqlite3.connect(self.dbFile) as conn:
            if db_is_new:
                print('Creating schema')
                with open(self.schemaFile, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)

                print('Inserting initial data')

                decisions = {'1':'acceptance', '2':'conditional acceptance', '3':'denial','4':'waiting list'}
                
                for key, value in decisions.items():

                    conn.execute("""
                    insert into decision (id, description)
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
                    insert into bunkhouse (id, name,gender)
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
                    insert into tribe (id, name)
                    values ({},\'{}\')
                    """.format(int(key),value['name'])
                    )
            
                camps = \
                {'1':{'startDate':datetime.date(2016, 6, 6),\
                'endDate':datetime.date(2016, 6, 19), 'totalCapacity':72 ,\
                'name': 'c1'},
                '2':{'startDate':datetime.date(2016, 7, 4), \
                'endDate':datetime.date(2016, 7, 17), 'totalCapacity':72,\
                'name': 'c2'},
                '3':{'startDate':datetime.date(2016, 8, 8),\
                'endDate':datetime.date(2016, 8, 21), 'totalCapacity':72,\
                'name': 'c3'}}

                for key, value in camps.items():
                    conn.execute("""
                    insert into camp (id, name, startDate, endDate, totalCapacity)
                    values ({},\'{}\',\'{}\',\'{}\',\'{}\')
                    """.format(int(key),value['name'],value['startDate'],value['endDate'], value['totalCapacity'])
                    )
                    

                
            else:
                print('Database exists, assume schema does, too.')

        self.conn = sqlite3.connect(self.dbFile)
        self.cursor = self.conn.cursor()


    def disconnect(self):
        self.conn.close()
        return 0
    
    def insert(self, tableName, data):
        '''
        data is a list of dict, data must be a list
        '''

        ok = False
        result = {}

        duplicatedRecords = []


        sampleRecord = data[0]
        
        cols = list(sampleRecord.keys())
        
        queryStatement = "insert or ignore into " + str(tableName) + \
        " (" + ", ".join(map(str,cols)) + ") values ("
        try:
            for record in data:
                # test to see if this record exists
                # compose the where condition
                
                conditionList = []
                condition = ""

                for key, value in record.items():
                    conditionList.append(str(key)+"="+"\'"+str(value)+"\'")
                
                condition = "and ".join(conditionList)


                res = self.select(tableName,condition)
                if len(res['result'])>0:
                    duplicatedRecords.append(record)
                else:
                
                    query = queryStatement
                    values = list(record.values())
                    values = ['\''+str(x)+'\'' for x in values]
                    query += ', '.join(map(str, values)) + ')'
                    self.cursor.execute(query)

            self.conn.commit()

            ok = True
            msg = str(len(data)-len(duplicatedRecords)) + ' record(s) ' + \
            'inserted, and ' + str(len(duplicatedRecords)) + \
            ' record(s) exist already.'
            result = {'msg': msg}

            return {'ok':ok,'result':result}
        except Exception as e:
            print(e)
            result = {'msg': 'error happend in db insert process'}
            
            return {'ok':ok,'result':result}





            
    def select(self, tableName, condition):
        '''
        condition is a string, which is the conditions in where clause
        '''
        ok = False
        result = []
        if condition=='':
            queryStatement = "select * from " + tableName
        else:
            queryStatement = "select * from "+ tableName + " where " + condition

        # try:

        self.cursor.execute('PRAGMA TABLE_INFO({})'.format(tableName))

        # collect names in a list
        names = [tup[1] for tup in self.cursor.fetchall()]


        self.cursor.execute(queryStatement)

        allRows = self.cursor.fetchall()
        
        ok = True
        
        if len(allRows)>0:
            for row in allRows:
                dic = {}
                for i in range(len(names)):
                    dic[str(names[i])] = row[i]
                result.append(dic)
                

        return {'ok':ok,'result':result}

        # except:
        #     return {'ok':ok,'result':result}

    def update(self, tableName, data):
        '''
        data is a dict which contains two elements:
        1. data that need to ne updated in a dict 
        2. conditions in a dict
        '''

        ok = False
        result = {}

        newData = data['newData']
        conditions = data['conditions']

        queryStatement = "update {} set ".format(tableName)
        
        l = []
        for key, value in newData.items():
            l.append(str(key)+"=(\"" + str(value) + "\")" )
        
        queryStatement+= ", ".join(map(str,l)) + " where "
        
        l = []
        for key,value in conditions.items():
            l.append(str(key) + "=" +"\"" + str(value) + "\"")
        
        queryStatement += " and ".join(map(str,l))

        print(queryStatement)

        self.cursor.execute(queryStatement)

        self.conn.commit()

        ok = True

        return {'ok':ok,'result':result}
    
    def delete(self, tableName, data):
        '''
        data is a dict, key is column name and value is lookup value
        '''
        ok = False
        result = {}

        queryStatement = "delete from "+ tableName + " where "
        l = []
        for key,value in data.items():
            l.append(str(key) + "=" +"\"" + str(value) + "\"")
        
        queryStatement += " and ".join(map(str,l))

        try:

            self.cursor.execute(queryStatement)

            self.conn.commit()
            ok = True
            

            return {'ok':ok,'result':result}

        except:
            return {'ok':ok,'result':result}








# db = DB('/db/camp.db','/db/Camp_schema.sql')

# data = [{'startDate':'2018-06-06','endDate':'2019-07-07', 'totalCapacity':36},\
# {'startDate':'2016-06-06','endDate':'2016-07-07', 'totalCapacity':36},\
# {'startDate':'2016-06-06','endDate':'2016-07-07', 'totalCapacity':36}]

# print(db.insert('camp', data))

# data = {'startDate':'2016-06-06','endDate':'2016-07-07'}

# db.select('camp',data)

# data = {'newData': {'startDate':'2018-06-06','endDate':'2018-07-07'},\
# 'conditions':{'campId':4}}

# db.update('camp',data)

# data = {'startDate':'2016-06-06','endDate':'2016-07-07'}

# db.delete('camp',data)



# db.disconnect()
