import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Lab6-Proj1_Dataset.csv")
test_set = pd.read_csv("Lab6-Proj1_TestSet.csv")

# Dataset

df_mean = df.mean()
df_std = df.std()

z_scores = abs(df - df_mean)/df_std

df_dataset = df

'''
plt.plot(z_scores)
plt.show()
'''

threshold = 2.6
df_dataset[z_scores <= threshold]
z_scores_dataset = z_scores[z_scores <= threshold]
print(df_dataset)

'''
plt.plot(z_scores_dataset)
plt.show()
'''

# idk what's next
# use df_dataset