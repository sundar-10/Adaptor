#!/usr/bin/python
#from six.moves import configparser
from configparser import ConfigParser
 
 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db


print(np.shape(test_x))
print(y_pred[0])
n=np.shape(train_x)[0]
k=np.shape(test_x)[0]
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