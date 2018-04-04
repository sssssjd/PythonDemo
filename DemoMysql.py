#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
#open connect
conn1 = mysql.connector.connect(user = 'root',password = 'root123',database = 'test')
cursor = conn1.cursor()
#create table user
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#insert record
cursor.execute('insert into user (id,name) value(%s,%s)',['1','Michael'])
cursor.rowcount
#commit
conn1.commit()
cursor.close()

cursor = conn1.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn1.close