import pymysql.cursors
import pandas as pd
import json

class RDBDataTable:
    def __init__(self, t_name, t_file, key_columns):
        self.t_name = t_name
        self.t_file = t_file
        self.key_columns = key_columns


        self.cnx= pymysql.connect(host='localhost',
                                     user='root',
                                     password='Bailin960203',
                                     port=3306,
                                     db='lenman2017',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)


    def template_to_where_clause(self, t):
        s = ""
        for (k, v) in t.items():
            if s != "":
                s += " AND "
            s += k + "='" + v + "'"

        if s != "":
            s = "WHERE " + s;

        return s

    def find_by_primary_key (self, key_values, values=None):
        res=[]
        for i in range(len(key_values)):
            template = dict(zip(self.key_columns, key_values[i]))
            result = self.find_by_template(template, values)
            if len(result) > 0:
                res.append(result[0])
        return res


    def delete(self, template):
        w = self.template_to_where_clause(template)
        q = "delete from " + self.t_file + " " + w
        print("q = ", q)
        cursor = self.cnx.cursor()
        cursor.execute(q)
        q2 = "select row_count() as count"
        cursor.execute(q2)
        f = cursor.fetchall()
        print("DB delete", f)
        self.cnx.commit()

    def find_by_template(self, t, fields=None):
        if fields is None:
            fields = ['*']

        w = self.template_to_where_clause(t)
        cursor = self.cnx.cursor()
        q = "SELECT " + ",".join(fields) + " FROM " + self.t_file + " " + w + ";"
        print("Query = ", q)
        cursor.execute(q);
        r = cursor.fetchall()
        return r

    def insert(self, row):
        try:
            keys = "(" + ",".join(list(row.keys())) + ") "
            values = "("
            for k in row.keys():
                values += "'" + row[k] + "'" + ","
            values = values[0:-1] + ")"
            q = "insert into " + self.t_file + " " + keys + " " + "values" + values
            print("Q = ", q)
            cursor = self.cnx.cursor()
            cursor.execute(q)
            q2 = "select row_count() as count"
            cursor.execute(q2)
            f = cursor.fetchone()
            print("DB inserted", f)
            self.cnx.commit()
        except pymysql.err.IntegrityError:
            print("What part of unique was not clear.")



'''
def DBRunQuery(q):
    cursor=cnx.cursor()
    print ("Query = ", q)
    cursor.execute(q);
    r = cursor.fetchall()
    #print("Query result = ", r)
    return r
    '''


'''
def test01:
    rdt = RDBDataTable("Foo", "Batting", ['playerID', 'teamID'])
    result = rdt.find_by_primary_key([['willite01', 'BOS'] , ['allisar01','CL1']])
    print("Result = ", json.dumps(result, indent=3))


'''
def test02():
    rdt = RDBDataTable("Foo", "Batting", ['playerID', 'teamID', 'yearID', 'stint'])
    result = rdt.find_by_primary_key([['willite01', 'BOS', '1960', '1']])
    print("Result = ", json.dumps(result, indent=3))

def test03():
    rdt = RDBDataTable("Foo", "People", ['playerID', 'teamID'])
    print(rdt.insert({'playerID': 'Me','birthYear': '1996', 'birthMonth': '2', 'birthDay': '5', 'birthCountry': 'USA', 'birthState': 'AL', 'birthCity': 'Mobile', 'deathYear': '1984', 'deathMonth': '8', 'deathDay': '16', 'deathCountry':'USA', 'deathState': 'GA', 'deathCity': 'Atlanta', 'nameFirst': 'Tommie', 'nameLast': 'Aaron', 'nameGiven': 'Tommie Lee', 'weight': '190', 'height': '75', 'bats': 'R', 'throws': 'R', 'debut': '1962-04-10', 'finalGame': '1971-09-26', 'retroID': 'aarot101', 'bbrefID': 'aaronto01'}))

test03()