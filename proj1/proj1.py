import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("Lab6-Proj1_Dataset.csv")
test_set = pd.read_csv("Lab6-Proj1_TestSet.csv")

# Dataset
    # z score calculation
df_mean = df.mean()
df_std = df.std()
z_scores = abs(df - df_mean)/df_std

df_dataset = df

'''
#visual represenation of all the points
plt.plot(z_scores)
plt.show()
'''
    # exclude ouliers by a threshold k*std
threshold = 2.6
df_dataset[z_scores <= threshold]
z_scores_dataset = z_scores[z_scores <= threshold]

'''
# visal representation of the chosen points
plt.plot(z_scores_dataset)
plt.show()
'''

# Train, Validation, Test split
# 60% train 15% validation 15% test
random_state = 42
val_test_size = 0.3
test_size = 0.5
x_train, x_valtest, y_train, y_valtest = train_test_split(df_dataset["Anchor_Ratio","Transmission_Range","Node_Density","Step_Size","Iterations"], df_dataset["ESLE"], test_size=val_test_size, random_state=random_state)
x_validation, x_test, y_validation, y_test = train_test_split(x_valtest, y_valtest, test_size=test_size, random_state=random_state)

# NN architecture

