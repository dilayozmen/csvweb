#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
class CSVFILE():
    def __init__(self):
        self.d={}
        self.csvFile=''
        self.firstline=[]
    #defField defines keys of d
    def defField(self):
        with open(self.csvFile) as fp:
            reader=csv.reader(fp)
            self.firstline=list(next(reader))
            for key in self.firstline:
                self.d[str(key)]=[] #keys of d and firstline fields of csv
        #return firstline

    def readCSV(self):
        self.defField()
        dictReader=csv.DictReader(open(self.csvFile, 'r'), delimiter = ',', quotechar = '"')
        for i in dictReader:
            for key in i:
                 self.d[key].append(i[str(key)])

    def display(self,df):
        self.csvFile=df
        self.readCSV()
        return self.d
