import pandas as pd
import psycopg2 
import pandas.io.sql as psql
import subprocess

import json
def inp(db_name,table_name,pas):
    connection=psycopg2.connect(database=db_name, user = "postgres", password = pas, host = "localhost")
    df=""
    df=pd.read_sql_query("SELECT *FROM "+table_name+" where flag=0",connection)
    return df


def alttable():
    conn=psycopg2.connect(database="test", user = "postgres", password = "sundar10", host = "localhost") 
    cur = conn.cursor()

    cur.execute(
           "ALTER TABLE stud ADD COLUMN id SERIAL PRIMARY KEY;"
        
    )
    conn.commit()
    conn.close()
def jsonfile(filename,db_name,table_name,predict_names,column_names):#
    data1={}
    data1['data']=[]
    data1['data'].append({
        'file_name':filename,
        "db_name":db_name,
        "table_name":table_name,
        "predict_names":predict_names,
        "column_names":column_names
    })
    #f=open('data.txt','w+')
    with open('data.txt', 'w+') as outfile:
        json.dump(data1, outfile)
        
def addpred(n,k,y_pred):
    n=int(n+1)
    k=int(k+n+1)
    print(type(n))
    conn=psycopg2.connect(database="test", user = "postgres", password = "sundar10", host = "localhost") 
    cur = conn.cursor()
    sql="""Update stud set predictedoutput=%s where id= %s"""
    for i in range(n,k):
        pred=y_pred[i-n-1]
        cur.execute(sql,(int(pred),int(i)))
        conn.commit()   

    conn.close()
def gettables():
    conn=psycopg2.connect(database="test", user = "postgres", password = "sundar10", host = "localhost") 
    cur = conn.cursor()
    cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
    ar=[]
    tables=[]
    for table in cur.fetchall():
        #print("    ajhbdsd     ",table)
        ar.append(table)
    for i in ar:
        tables.append(i[0])        
    print(tables)        
#gettables()          
def get_database_info(host='localhost', user='postgres'):
    records, _ = subprocess.Popen(['psql','-lA','-F\x02','-R\x01','-h',host,'-U',user ],stdout=subprocess.PIPE).communicate()
    records = records.decode("utf-8").split('\x01')
    header = records[1].split('\x02')
    #print(header)

    d=[dict(zip(header,line.split('\x02'))) for line in records[2:-1]]
    databases=[]
    #print(d)
    for i in d:
        databases.append(i['Name'])
    #print(databases)    

#get_database_info('localhost','postgres')   
def columnnames(): 
    conn=psycopg2.connect(database="test", user = "postgres", password = "sundar10", host = "localhost") 
    cursor = conn.cursor()
    cursor.execute("select column_name from information_schema.columns where table_name='stud'")
    column_names = [row[0] for row in cursor]
    print(column_names) 



def getdb():
    #files=file_name
    import importlib
    my_module = importlib.import_module('os.path')

    #model = getattr(__import__('.Home.IIT', fromlist=[model_name]), model_name)
    #import importlib
    #import sys
    #module=(importlib.import_module(files))
    #pint("sajdshjdbsahd         ",module)#
    #fname='disp'
    #handler = getattr(sys.modules[module], fname)
    #eval(handler)
    #header_handlers['test']()
    #print(func)
    #func()
#getdb()
def variablefile():
    a='test.py'
    import importlib
    i=importlib.import_module(a)
    #i.disp()
    print("hi")

#variablefile()  
def flag1(db_name='test',table_name='stud',column_names='m1',predict_names='m2'):
    conn=psycopg2.connect(database=db_name, user = "postgres", password = "sundar10", host = "localhost") 
    cursor = conn.cursor()
    #cursor.execute("select column_name from information_schema.columns where table_name='"+table_name+"'")
    fl=1
    cursor.execute("UPDATE "+table_name+" SET flag=1")
    conn.commit()
    #column_names = [row[0] for row in cursor] 
    #cursor.execute("select * from "+table_name+" where flag = 1")
    #column_names = [row [0] for row in cursor] 
    #print(column_names)
#flag1()  
def addpredcol(db_name,table_name):
    conn=psycopg2.connect(database="test", user = "postgres", password = "sundar10", host = "localhost") 
    cur = conn.cursor()

    cur.execute(
           "ALTER TABLE stud ADD COLUMN predictedoutput integer;"
        
    )
    conn.commit()    
         
def cpy(file):
    with open(file) as f:
        with open("out.py", "w") as f1:
            for line in f:
                f1.write(line)
cpy("test.py")