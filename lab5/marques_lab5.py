#imports
import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import yellowbrick
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix
from sklearn import preprocessing
from yellowbrick.classifier import ClassificationReport

#reading the files and meter indice na 1º linha
    ## haberman
haberman_data_file = pd.read_csv("haberman.data",names=["p_age", "year_op", "n_pos_auxn", "surv_stat"])

'''
    ## iris
iris_data_file = pd.read_csv("iris.data",names=["s_length","s_width","p_length","p_width","class"])
'''

#HABERMAN
#dividir colunas de data e de objetivo
cols = [col for col in haberman_data_file.columns if col not in ["surv_stat"]]
data_haberman = haberman_data_file[cols]
target_haberman = haberman_data_file["surv_stat"]

#dividir treino e teste
data_train, data_test, target_train, target_test = train_test_split(data_haberman,target_haberman, test_size = 0.20, random_state = 10)

print("data_train")
print(data_train.head())
print("target train")
print(target_train.head())


# LINEAR SVC

svc_model = LinearSVC(random_state=0)
#train the algorithm on training data and predict using the testing data
pred = svc_model.fit(data_train, target_train).predict(data_test)
#print the accuracy score of the model
print("LinearSVC accuracy : ",accuracy_score(target_test, pred, normalize = True))

#Instantiate the classification model and visualizer
visualizer = ClassificationReport(svc_model, classes=['Won','Loss'])
visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
visualizer.score(data_test, target_test) # Evaluate the model on the test data
g = visualizer.poof() # Draw/show/poof the data

