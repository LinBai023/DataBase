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
        #print("Query result = ", r)
        return r

#def insert(self, row):



'''
def DBRunQuery(q):
    cursor=cnx.cursor()
    print ("Query = ", q)
    cursor.execute(q);
    r = cursor.fetchall()
    #print("Query result = ", r)
    return r
    '''



rdt = RDBDataTable("Foo", "Batting", ['playerID', 'teamID'])
result = rdt.find_by_primary_key([['willite01', 'BOS'],['allisar01','CL1']])
print("Result = ", json.dumps(result, indent=3))
