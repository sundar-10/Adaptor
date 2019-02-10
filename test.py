import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import IO
import csv
import json
import psycopg2
import pickle
def ml(data,db_name,table_name,column_names=['m1','m2'],predict_names=['correctoutput','predictedoutput'],params=''):
	from sklearn.model_selection import train_test_split
	CSV_COLUMN_NAMES = ['M1', 'M2','M3','M4','sQ1','sQ2','sQ3','sQ4','sQ5','TQ1','TQ2','TQ3','TQ4','TQ5','Species']
	SPECIES = ['DropOut', 'PG','Job']
	y_name='correctoutput'
	"""
	train = pd.read_csv(train_path, na[mes=CSV_COLUMN_NAMES, header=0)
	train_x, train_y = train.drop(['Species'],axis=1), train.pop(y_name)

	test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
	test_x, test_y = test, test.pop(y_name)
	"""
	
	#IO.addpredcol(db_name,table_name)
		
		#print(data)
	train,test= train_test_split(data, test_size=0.2, random_state=42)
	#print("kjasbdjsadjsa")
	#print(train)
	train_x = pd.DataFrame(train,columns=column_names)
	train_y=pd.DataFrame(train,columns=predict_names)
	
	test_x = pd.DataFrame(test,columns=column_names)
	test_y=pd.DataFrame(test,columns=predict_names)
	#print(train_y)
	#cars.info()
	import sklearn
	import sklearn.tree
	from sklearn.tree import DecisionTreeClassifier
	linreg = LinearRegression()
	linreg.fit(train_x, train_y)
	filename = 'finalized_model.sav'
	IO.jsonfile(filename,db_name,table_name,predict_names,column_names)
	
		
	pickle.dump(linreg, open(filename, 'wb'))
	loaded_model = pickle.load(open(filename, 'rb'))
	result = loaded_model.predict(test_x)
	y_pred =np.uint8(np.round(result))
	
	#print(y_pred)
	
	#IO.alttable()
	IO.addpred(np.shape(train_x)[0],np.shape(test_x)[0],y_pred)
	return (np.sqrt(metrics.mean_squared_error(test_y, y_pred)))
#ml('test','stud') 

def disp():
	print("kajndjsnf")