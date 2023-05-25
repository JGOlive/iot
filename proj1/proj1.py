import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("Lab6-Proj1_Dataset.csv")

# Dataset
    # z score calculation
df_mean = df.mean()
df_std = df.std()
z_scores = abs(df - df_mean)/df_std

df_dataset = df.copy()

'''
#visual represenation of all the points
plt.plot(z_scores)
plt.show()
'''
    # exclude ouliers by a threshold k*std
threshold = 2.6
outliers_std = z_scores > threshold
df_dataset = df_dataset[~outliers_std]
df_dataset.dropna(inplace=True)

z_scores_dataset = z_scores[z_scores <= threshold]

'''
# visual representation of the chosen points
plt.plot(z_scores_dataset)
plt.show()
'''

# Train, Validation, Test split
# 70% train 15% validation 15% test
random_state = 42
valtest_size = 0.3
val_test_ratio = 0.5

cols = [col for col in df_dataset.columns if col not in ["ESLE"]]
data_dataset = df_dataset[cols]
target_dataset = df_dataset["ESLE"]

x_train, x_valtest, y_train, y_valtest = train_test_split(data_dataset, target_dataset, test_size=valtest_size, random_state=random_state)
x_val, x_test, y_val, y_test = train_test_split(x_valtest, y_valtest, test_size=val_test_ratio, random_state=random_state)

x_trainval = pd.concat([x_train, x_val],ignore_index=True, sort=False)
y_trainval = pd.concat([y_train, y_val],ignore_index=True, sort=False)

# NN architecture
mlp = MLPRegressor(hidden_layer_sizes=(6, 8), activation="logistic",solver="sgd", random_state=random_state, max_iter=500)

# Train and Validate
scores = cross_val_score(mlp,x_trainval,y_trainval, cv=10, scoring="neg_root_mean_squared_error")
mean_scores = scores.mean()

print(scores)
print("Validation mean score:",mean_scores)

# Train
mlp.fit(x_train,y_train)

# Test
y_predicted = mlp.predict(x_test)


rmse = mean_squared_error(y_test, y_predicted, squared=False)

mae = mean_absolute_error(y_test,y_predicted)

print("RSME:",rmse)
print("MAE:",mae)

# save the neural network

NN_filename = "NN_Model.pkl"
with open(NN_filename, "wb") as file:
    pickle.dump(mlp,file)