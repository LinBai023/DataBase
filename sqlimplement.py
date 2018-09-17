import pymysql.cursors
import pandas as pd
import json

cnx= pymysql.connect(host='localhost',
                     user='root',
                     password='Bailin960203',
                     port=3306,
                     db='lenman2017',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

def DBRunQuery(q):
    cursor=cnx.cursor()
    print ("Query = ", q)
    cursor.execute(q);
    r = cursor.fetchall()
    #print("Query result = ", r)
    return r

result = DBRunQuery("select * from people where playerid='willite01'")
print("The result is of type: ", list(result))
print("OK. The answer is an instance of the class 'tuple.'")