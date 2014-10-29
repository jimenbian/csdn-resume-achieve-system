#-*- coding: UTF-8 -*- 
import MySQLdb

dbname="FuGDIwGiSqusOWjzLpQu"
api_key="V08h6nAoK5dHGMYV0pthSwFM"
secret_key="HQgnI5yufE49bTizMzoUG2Pgosq3WPin"

def sql_connect():
        
    mydb = MySQLdb.connect(
      host   = "sqld.duapp.com",
      port   = 4050,
      user   = api_key,
      passwd = secret_key,
      db = dbname)
    cursor=mydb.cursor()
    cmd='''CREATE TABLE IF NOT EXISTS resume(user char(20) not null,score float(20) default '0')'''
    cursor.execute(cmd)
    mydb.close()

def add_data(user):
    mydb = MySQLdb.connect(
      host   = "sqld.duapp.com",
      port   = 4050,
      user   = api_key,
      passwd = secret_key,
      db = dbname)
    cursor=mydb.cursor() 
    cmd1='''CREATE TABLE IF NOT EXISTS resumetest(user char(20))'''
    cmd= "insert into resumetest(user) values('garvin')"      
    cursor.execute("INSERT INTO %s(%s) VALUES(%s)"%("resumetest","user","garvin"))
    mydb.close()
