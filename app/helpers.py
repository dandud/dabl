import pandas as pd
from . import db

def table_exists (tablename:str):
    if not isinstance(tablename, str):
        raise TypeError("provided table name is not string")
        return

    tables = db.engine.table_names()

    if tablename in tables:
        return True
    else:
        return False

def table_csv_import (tablename:str, csvfile:str=None):
    '''imports data into specified table name. defaults to csv with table name in app\data\import\init unless file path specified as csvfile parameter'''
    if not isinstance(tablename, str):
        raise TypeError("provided table name is not string")
        return
    
    if not table_exists(tablename):
        raise NameError("provided table name does not exist in database")
        return

    if csvfile == None:
        filepath = 'app/data/import/init/' + tablename + '.csv'
    else:
        filepath = csvfile

    with open(filepath, 'r', encoding="utf-8") as file:
        data_df = pd.read_csv(file)
    data_df.to_sql(tablename, con=db.engine, index=False, index_label='id', if_exists='replace')

def table_csv_export (tablename:str, csvfile:str=None):
    '''export data into specified csv file. defaults to destination app\data\export unless file path specified as csvfile parameter'''
    if not isinstance(tablename, str):
        raise TypeError("provided table name is not string")
        return
    
    if not table_exists(tablename):
        raise NameError("provided table name does not exist in database")
        return

    if csvfile == None:
        filepath = 'app/data/export/' + tablename + '.csv'
    else:
        filepath = csvfile

    data_df = pd.read_sql_table(tablename)
    data_df.to_csv(csvfile)