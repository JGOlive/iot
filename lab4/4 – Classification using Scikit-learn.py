import numpy as np
import scipy as sp
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier

iris = pd.read_csv("iris.data", names=["s_length","s_width","p_length","p_width","class"])

# x_train são dados de entrada para treino, y_train sao os dados de saída para treino
# x_test são os dados de entrada para teste, y_teste são os dadso de saída para teste
# test_size é a razão absoluta da porção dos dados que é utilizada para teste
# random state é para o valor inicial 
x_train, x_test, y_train, y_test = train_test_split(iris[["s_length","s_width","p_length","p_width"]], iris["class"], test_size=0.2, random_state=42)

### KNeighbors
# trainar o amigo
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

KN_y_pred = knn.predict(x_test)

KN_results = pd.DataFrame({"Actual":y_test, "Predicted":KN_y_pred})
print("KNeighbors")
print(KN_results)

### SVM

### Linear SVC

### Naive Bayes
gnb = GaussianNB()
gnb.fit(x_train,y_train)

GNB_y_pred = gnb.predict(x_test)

GNB_results = pd.DataFrame({"Actual":y_test, "Predicted":GNB_y_pred})
print("Naive Bayes")
print(KN_results)