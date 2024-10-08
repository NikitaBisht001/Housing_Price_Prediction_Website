import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

#!pip install patool

import patoolib

patoolib.extract_archive('/content/drive/MyDrive/HousingPrices.zip')

data_set = pd.read_csv('/content/Housing.csv')

data_set.head()

data_set.info()

data_set.dtypes

non_integer_columns = data_set.select_dtypes(exclude=['int64'])
print(non_integer_columns.columns)
label_encoders = {}
for column in non_integer_columns.columns:
    label_encoders[column] = LabelEncoder()
    data_set[column] = label_encoders[column].fit_transform(data_set[column])
print(data_set.head(9))

X= data_set[['area', 'bedrooms', 'bathrooms', 'stories','mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea','furnishingstatus']]
Y = data_set['price']
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=104, test_size=0.2, shuffle=True)

X_train.head()
X_train.info()

Model_1 = LinearRegression()
Model_1.fit(X_train, y_train)
y_pred = Model_1.predict(X_test)
#print("Predicted price for this data is", y_pred)
mse1 = mean_squared_error(y_test, y_pred)
r2_1 = r2_score(y_test, y_pred)
print("Mean Squared Error_1:", mse1)
print("R-squared_1:", r2_1)
# out of all the model linear regression gives the best result

'''Model_2 = Ridge()
Model_2.fit(X_train, y_train)
y_pred = Model_2.predict(X_test)
mse2 = mean_squared_error(y_test, y_pred)
r2_2 = r2_score(y_test, y_pred)
print("Mean Squared Error_2:", mse2)
print("R-squared_2:", r2_2)

Model_3 = Lasso()
Model_3.fit(X_train, y_train)
y_pred = Model_3.predict(X_test)
mse3 = mean_squared_error(y_test, y_pred)
r2_3 = r2_score(y_test, y_pred)
print("Mean Squared Error_3:", mse3)
print("R-squared_3:", r2_3)

Model_4 = DecisionTreeRegressor()
Model_4.fit(X_train, y_train)
y_pred = Model_4.predict(X_test)
mse4 = mean_squared_error(y_test, y_pred)
r2_4 = r2_score(y_test, y_pred)
print("Mean Squared Error_4:", mse4)
print("R-squared_4:", r2_4)'''

import pickle
with open('Model_1.pkl', 'wb') as f:
    pickle.dump(Model_1, f)

# Download the model as i am using colab for the coding and training of the model so i used google.colab library to down load it
from google.colab import files
files.download('Model_1.pkl')

