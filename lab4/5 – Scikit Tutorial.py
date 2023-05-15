import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix

sales_data = pd.read_csv("WA_Fn-UseC_-Sales-Win-Loss.csv")

#head and tail stuff
head_sales = sales_data.head(n=2)
tail_sales = sales_data.tail(n=2)
dtypes_sales = sales_data.dtypes
print(dtypes_sales)

# from the tutorial (1)
# set the background colour of the plot to white
sns.set(style="whitegrid", color_codes=True)
# setting the plot size for all plots
sns.set(rc={'figure.figsize':(11.7,8.27)})
# create a countplot
sns.countplot(x="Route To Market", data = sales_data, hue = "Opportunity Result")
# Remove the top and down margin
sns.despine(offset=10, trim=True)
# display the plotplt.show()
plt.show()

# from the tutorial (2)
# setting the plot size for all plots
sns.set(rc={'figure.figsize':(16.7,13.27)})
# plotting the violinplot
sns.violinplot(x="Opportunity Result",y="Client Size By Revenue", hue="Opportunity Result", data=sales_data);
plt.show()

# from the tutorial (3) not needed
# create the Labelencoder object
#le = preprocessing.LabelEncoder()
# convert the categorical columns into numeric
#encoded_value = le.fit_transform(["paris", "paris", "tokyo", "amsterdam"])
#print(encoded_value)

# from the tutorial (4)