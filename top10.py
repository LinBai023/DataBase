import csv
from collections import defaultdict
import csv
import json
import copy


class CSVDataTable:

    data_dir = '/Users/zs/4111/DataBase/'

# initialize the class
    def __init__(self, t_name, t_file, key_column):
        self.table_name = t_name
        self.file_name = t_file
        self.key_columns = key_column
        self.columns = None
        self.rows = None
        self.dic={}
        self.new_dic={}
        self.new_dic2={}
        self.nameset=set()

# read the csv file as dictionary

    def __str__(self):
        result = ""
        result += "Name: {}, File: {}, No.of columns:{},Key: {}".format(self.table_name, self.file_name,len(self.rows),self.key_columns)
        result += "\n"
        result += "Columns = " + str(self.columns)
        result += "\nRow = \n"
        for r in self.rows:
            result += str(r) + "\n"
        return result


    # load the file by the file name into class instance data

    def load(self):
        file_address=self.data_dir+self.file_name

        with open(file_address, 'r') as csvfile:
            reader= csv.DictReader(csvfile)
# initialize the column and row: column is the list of keys, and row is the data storage
            for row in reader:
                if self.columns is None:
                    self.columns = list(row.keys())
                if self.rows is None:
                    self.rows = []
                self.rows.append(row)

    def delete(self):
        for row in self.rows:
            if int(row['yearID']) >= 1960:
                self.nameset.add(row['playerID'])

    def mapping(self):
        for row in self.rows:
            if row['playerID'] in self.nameset and row['playerID'] in self.dic.keys():
                self.dic[row['playerID']][0]+= int(row['AB'])
                self.dic[row['playerID']][1]+= int(row['H'])
            elif row['playerID'] in self.nameset and row['playerID'] not in self.dic.keys():
                self.dic[row['playerID']]=[int(row['AB']), int(row['H'])]


    def select(self):
        for k in self.dic.keys():
            if self.dic[k][0]>200:
                self.new_dic[k]=self.dic[k]
        #return self.new_dic

    def calculation(self):
        for i in self.new_dic:
            self.new_dic2[i]= self.new_dic[i][1]/self.new_dic[i][0]
        return self.new_dic2

    def sort(self):
        d= sorted(self.new_dic2.items(), key=lambda k: k[1], reverse=True)
        return d

csvt = CSVDataTable("People", "Batting.csv", ['playerID'])
csvt.load()
csvt.delete()
csvt.mapping()
csvt.select()
csvt.calculation()
csvt.sort()
print(csvt.sort())

