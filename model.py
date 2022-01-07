import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  

url = "./data.csv"
s_data = pd.read_csv(url)

s_data.head(10)

X = s_data.iloc[:, :-1].values  
y = s_data.iloc[:, 1].values

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

def predict(age):
    own_pred = regressor.predict([[age]])
    sleep = own_pred[0]
    return sleep


