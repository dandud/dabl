import pandas as pd
from . import db

def table_csv_import (tablename:str, csvfile:str=None):
    '''imports data into specified table name. defaults to csv with table name in app\data\import\init unless file path specified as csvfile parameter'''
    if not isinstance(tablename, str):
        raise TypeError("provided table name is not string")
        return
    
    if csvfile == None:
        filepath = 'app/data/import/init/' + tablename + '.csv'
    else:
        filepath = csvfile

    with open(filepath, 'r', encoding="utf-8") as file:
        data_df = pd.read_csv(file)
    data_df.to_sql(tablename, con=db.engine, index=False, index_label='id', if_exists='replace')