import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score
import numpy as np
import pickle

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
val_test_size = 0.3
test_size = 0.5

cols = [col for col in df_dataset.columns if col not in ["ESLE"]]
data_dataset = df_dataset[cols]
target_dataset = df_dataset["ESLE"]

x_train, x_valtest, y_train, y_valtest = train_test_split(data_dataset, target_dataset, test_size=val_test_size, random_state=random_state)
x_validation, x_test, y_validation, y_test = train_test_split(x_valtest, y_valtest, test_size=test_size, random_state=random_state)

# NN architecture
mlp = MLPRegressor(hidden_layer_sizes=(6, 8), activation="logistic",solver="sgd", random_state=42, max_iter=500)

# Train the NN
mlp.fit(x_train,y_train)

# Validate
scores = cross_val_score(mlp,x_validation,y_validation, cv=10)
mean_scores = scores.mean()

print(scores)
print(mean_scores)

# Test
y_prediciton = mlp.predict(x_test)

e = abs(y_prediciton - y_test)

rsme = np.sqrt(sum(np.square(e))/np.size(e))

mae = sum(e)/np.size(e)

print("RSME:",rsme)
print("MAE:",mae)

# save the neural network

NN_filename = "NN_Model.pkl"
with open(NN_filename, "wb") as file:
    pickle.dump(mlp,file)