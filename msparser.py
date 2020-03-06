import pandas as pa 
from sqlalchemy import create_engine 
import urllib
import pyodbc
import json

class Parser:

    def __init__(self):
        pass

    def engine(self):
        with open("conf.json") as f:
            js = json.load(f)
        drv = 'DRIVER={4};SERVER={0};DATABASE={1};UID={2};PWD={3}'.format(js["host"], js["database"], js["user"], js["password"], "{SQL Server Native Client 11.0}")
        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % urllib.parse.quote_plus(drv))

    def parse(self, fl="data.csv", delimiter=",", index="Id", table="geysers"):
        # use usecols=[] to filter what colums are needed
        data = pa.read_csv(fl, sep=delimiter, index_col=index)
        ng = self.engine()
        data.to_sql(table, con=ng, if_exists='append')

    def getAllData(self, table="geysers"):
        ng = self.engine()
        print(pa.read_sql_table(table, con=ng))

    def getQuery(self, qr="Select Id from geysers"):
        ng = self.engine()
        print(pa.read_sql_query(qr, con=ng))

#Some other examples
# filter dataframe data:
# print(data.filter(["DisplayName"]))

