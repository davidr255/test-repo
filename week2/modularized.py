#!/usr/bin/env python3

import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('test2.db',
                            check_same_thread=False)
        self.cursor     = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self,type_,value,traceback):
        if self.connection:
            if self.cursor:
                self.connection.commit()
                self.cursor.close()
            self.connection.close()

    def create_table(self,table_name):
        self.cursor.execute(
            f'DROP TABLE IF EXISTS {table_name};'
            )
        self.cursor.execute(
            f'''CREATE TABLE {table_name}(
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );''')

    def add_column(self,table_name,column_name,column_type):
        self.cursor.execute(
            f'''ALTER TABLE {table_name}
            ADD COLUMN {column_name} {column_type};''')


if __name__ == '__main__':
    framework = {'table_name':'uber',
                 'columns':[
                    {'column_name':'last_price',
                     'column_type':'FLOAT'}]}
    with Database() as db:
        db.create_table(framework['table_name'])
        for _ in framework['columns']:
            db.add_column(
                framework['table_name'],
                _['column_name'],
                _['column_type'])
