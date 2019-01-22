'''
Created on 16 de jan de 2019

@author: 01456231650
'''
import sqlite3

from dao.basedao import BaseDao

class ItemDao (BaseDao):
    def insert(self, row):
        sql = "insert into item values (?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(sql, row)
        cursor.close()
        self.conn.commit()        
    
    def find_all(self):
        try:
            sql = "select * from item"
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except sqlite3.OperationalError:
            self.__create_table()
            self.__insert_some_data()
            print("[DEBUG] Create table ITEM and inserted some data")
            return self.find_all()

    def __create_table(self):
        sql = """create table item (
            id integer primary key,
            codigo integer not null,
            nome varchar(30) not null)"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        cursor.close()

    def __insert_some_data(self):
        for i in range(1,6):
            row = (i, i*100, "Produto%d"%i)
            self.insert(row)    