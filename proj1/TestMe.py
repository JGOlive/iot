import numpy as np
import pandas as pd
import pickle
import sklearn
from sklearn.metrics import mean_squared_error

df = pd.read_csv("Lab6-Proj1_TestSet.csv")

NN_filename = "NN_Model.pkl"
with open(NN_filename, "rb") as file:
    nn_model = pickle.load(file)

# remove lines with missing information
test_df = df.dropna()

# convert dataframe to numeric
test_df = test_df.apply(pd.to_numeric)
'''
print(test_df.dtypes)
print(test_df)
'''
# remove ouliers by a threshold k*std
# z score calculation
test_mean = test_df.mean()
test_std = test_df.std()
z_scores = abs(test_df - test_mean)/test_std
# remove outliers
threshold = 2.8
outliers_std = z_scores > threshold
test_df = test_df[~outliers_std]
test_df.dropna(inplace=True)

#split into x and y
cols = [col for col in test_df.columns if col not in ["ESLE"]]
x_test = test_df[cols]
y_test = test_df["ESLE"]

# Use the model to predict values
y_predicted = nn_model.predict(x_test)

rmse = mean_squared_error(y_test, y_predicted, squared=False)

print("ESLE Predicted:")
print(y_predicted)

print("RMSE:", rmse)