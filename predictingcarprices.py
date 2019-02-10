
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')

col_names = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']
cars = pd.read_csv('imports-85.data', names=col_names)

#cars.info()
#cars.head()

cars['normalized-losses'].value_counts()

cars.drop('normalized-losses',axis = 1, inplace = True)

cars.replace("?", np.nan, inplace=True)

#cars.info()

cars.dropna(axis = 0, how = 'any', inplace = True)

cars[['price','peak-rpm','horsepower']] = cars[['price','peak-rpm','horsepower']].astype(int)
cars[['stroke','bore',]] = cars[['stroke','bore',]].astype(float)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

def knn_train_test(df, col, kval):
    X = df[[col]]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    for k in kval:
        knn = KNeighborsRegressor(k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        rmse = mse ** (1/2)
        #print("RMSE of {} for k = {} : {}".format(col,k, rmse))
        plt.xlim([0,10])
        plt.ylim([0,10000])
        plt.xticks([1,3,5,7,9])
        plt.bar(k,rmse)
                         
    #plt.show()      

features = ['highway-mpg', 'city-mpg', 'peak-rpm', 'horsepower', 'engine-size', 'curb-weight', 
            'width', 'length', 'height', 'wheel-base','bore', 'stroke']

for i in features:
    knn_train_test(cars, i, [1, 3, 5, 7, 9])



two_var = ['engine-size', 'horsepower']
three_var = ['engine-size', 'horsepower','width' ] # For 3 variables
four_var = ['engine-size', 'horsepower', 'width', 'highway-mpg'] # For 4 variables
five_var = ['engine-size', 'horsepower', 'width', 'highway-mpg','city-mpg'] # for 5 variables

def knn_train_test1(df, col, k):
    X = df[col]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    knn = KNeighborsRegressor(k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    #print(col)
    #print(y_pred)
    rmse = mse ** (1/2)
    #print("RMSE of {} for k = {} : {}".format(col,k, rmse))

knn_train_test1(cars,two_var, 3)
knn_train_test1(cars, three_var, 3)
knn_train_test1(cars, four_var, 3)
knn_train_test1(cars, five_var, 3)

kval = np.arange(1,26,1) 

def knn_train_test2(df, col, kval):
    X = df[col]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    for k in kval:
        knn = KNeighborsRegressor(k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        rmse = mse ** (1/2)
        #print("RMSE of {} for k = {} : {}".format(col,k, rmse))
        plt.xlim([0,25])
        plt.ylim([0,7000])
        plt.xticks(kval)
        plt.xlabel("K value")
        plt.ylabel("RMSE")
        plt.title("Error graph for each K value")
        plt.bar(k,rmse)
    #plt.show()

knn_train_test2(cars, four_var, kval)

def knn_train_test1(df, col, k,inputd):
    X = df[col]
    y = df['price']
    #print(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    sc_X = StandardScaler()
    print(type(X_test))
   # print(Y_test)
    X = sc_X.fit_transform(X)
    inputd = sc_X.transform(inputd)
    
    knn = KNeighborsRegressor(k)
    knn.fit(X, y)
    y_pred = knn.predict(inputd)
    #mse = mean_squared_error(y_test, y_pred)
    #print(col,"\n")
    print(y_pred,"\n")
    #rmse = mse ** (1/2)
    #print("RMSE of {} for k = {} : {}".format(col,k, rmse))

column=['engine-size','horsepower','width','highway-mpg']
inputdata= [{'engine-size':110,'horsepower':80,'width':60,'highway-mpg':20}]
inputd=pd.DataFrame(inputdata)
print(inputd)
knn_train_test1(cars, column, 4,inputd)


# #### Conclusion

# From the graph, we see that the error is higher when k value goes beyind 10. RMSE is in the lower range when k < 10. 
# Based on this observation, I choose k=4 and these four variables (engine-size, horsepower, width and highway-mpg) for an 
# optimal model for deciding the price of the cars.
