#isto significa código que foi comentado com o fim de não dar prints de demasiada informação
# isto significa comentários no código
#^ este espaço indica a diferenca
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
import yellowbrick
from yellowbrick.classifier import ClassificationReport

sales_data = pd.read_csv("WA_Fn-UseC_-Sales-Win-Loss.csv")

#head and tail stuff
head_sales = sales_data.head(n=2)
tail_sales = sales_data.tail(n=2)
dtypes_sales = sales_data.dtypes

# from the tutorial (1)
# set the background colour of the plot to white
#sns.set(style="whitegrid", color_codes=True)
# setting the plot size for all plots
#sns.set(rc={'figure.figsize':(11.7,8.27)})
# create a countplot
#sns.countplot(x="Route To Market", data = sales_data, hue = "Opportunity Result")
# Remove the top and down margin
#sns.despine(offset=10, trim=True)
# display the plotplt.show()
#plt.show()

# from the tutorial (2)
# setting the plot size for all plots
#sns.set(rc={'figure.figsize':(16.7,13.27)})
# plotting the violinplot
#sns.violinplot(x="Opportunity Result",y="Client Size By Revenue", hue="Opportunity Result", data=sales_data);
#plt.show()

# from the tutorial (3) not needed
# create the Labelencoder object
#le = preprocessing.LabelEncoder()
# convert the categorical columns into numeric
#encoded_value = le.fit_transform(["paris", "paris", "tokyo", "amsterdam"])
#print(encoded_value)

# from the tutorial (4)
print("Supplies Subgroup' : ",sales_data['Supplies Subgroup'].unique())
print("Region : ",sales_data['Region'].unique())
print("Route To Market : ",sales_data['Route To Market'].unique())
print("Opportunity Result : ",sales_data['Opportunity Result'].unique())
print("Competitor Type : ",sales_data['Competitor Type'].unique())
print("'Supplies Group : ",sales_data['Supplies Group'].unique())

# from the tutorial (5)
# create the Labelencoder object
le = preprocessing.LabelEncoder()
#convert the categorical columns into numeric
sales_data['Supplies Subgroup'] = le.fit_transform(sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])
#display the initial records
print(sales_data.head(n = 3))

# from the tutorial (6)
# select columns other than 'Opportunity Number','Opportunity Result'
cols = [col for col in sales_data.columns if col not in ['Opportunity Number','Opportunity Result']]
# dropping the 'Opportunity Number'and 'Opportunity Result' columns
data = sales_data[cols]
#assigning the Oppurtunity Result column as target
target = sales_data['Opportunity Result']
print(data.head(n=3))

# from the tutorial (7)
#split data set into train and test sets
data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.30, random_state = 10)

# from the tutorial (8) GaussianNB
#create an object of the type GaussianNB
gnb = GaussianNB()
#train the algorithm on training data and predict using the testing data
gnb_pred = gnb.fit(data_train, target_train).predict(data_test)
#print(pred.tolist())
#print the accuracy score of the model
print("Naive-Bayes accuracy : ",accuracy_score(target_test, gnb_pred, normalize = True))

# from the tutorial (9) LinearSVC
#create an object of type LinearSVC
svc_model = LinearSVC(random_state=0)
#train the algorithm on training data and predict using the testing data
svc_pred = svc_model.fit(data_train, target_train).predict(data_test)
#print the accuracy score of the model
print("LinearSVC accuracy : ",accuracy_score(target_test, svc_pred, normalize = True))

# from the tutorial (10) K-Neighbors
#create object of the lassifier
neigh = KNeighborsClassifier(n_neighbors=3)
#Train the algorithm
neigh.fit(data_train, target_train)
# predict the response
neigh_pred = neigh.predict(data_test)
# evaluate accuracy
print("KNeighbors accuracy score : ",accuracy_score(target_test, neigh_pred))

# from the tutorial (11) GaussianNB figure
# Instantiate the classification model and visualizer
visualizer = ClassificationReport(gnb, classes=['Won','Loss'])
visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
visualizer.score(data_test, target_test) # Evaluate the model on the test data
g = visualizer.poof() # Draw/show/poof the data

#from the tutorial (12) LinearSVC
# Instantiate the classification model and visualizer
visualizer = ClassificationReport(svc_model, classes=['Won','Loss'])
visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
visualizer.score(data_test, target_test) # Evaluate the model on the test data
g = visualizer.poof() # Draw/show/poof the data

#from the tutorial (13) KNeighborsClassifier
# Instantiate the classification model and visualizer
visualizer = ClassificationReport(neigh, classes=['Won','Loss'])
visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
visualizer.score(data_test, target_test) # Evaluate the model on the test data
g = visualizer.poof() # Draw/show/poof the data