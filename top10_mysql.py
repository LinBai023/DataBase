import pandas as pd
import pymysql.cursors

cnx= pymysql.connect(host='localhost',
                    user='root',
                    password='Bailin960203',
                    port=3306,
                    db='lenman2017',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)

def run_q(q):
    cursor=cnx.cursor()
    print ("Query = ", q)
    cursor.execute(q);
    r = cursor.fetchall()
    print("Query result = ", r)
    return r

q = "SELECT \
        Batting.playerID, \
        (SELECT People.nameFirst FROM People WHERE People.playerID=Batting.playerID) as first_name, \
        (SELECT People.nameLast FROM People WHERE People.playerID=Batting.playerID) as last_name, \
        sum(Batting.h)/sum(batting.ab) as career_average, \
        sum(Batting.h) as career_hits, \
        sum(Batting.ab) as career_at_bats,\
        min(Batting.yearID) as first_year, \
        max(Batting.yearID) as last_year \
        FROM \
        Batting \
        GROUP BY \
        playerId \
        HAVING \
        career_at_bats > 200 AND last_year >= 1960 \
        ORDER BY \
        career_average DESC \
        LIMIT 10;"

r = run_q(q)
r = pd.DataFrame.from_dict(r)
print(r)