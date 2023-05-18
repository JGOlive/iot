import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix

#ler ficheiro e adicionar indice
iris = pd.read_csv("iris.data", names=["s_length","s_width","p_length","p_width","class"])

# x_train são dados de entrada para treino, y_train sao os dados de saída para treino
# x_test são os dados de entrada para teste, y_teste são os dadso de saída para teste
# test_size é a razão absoluta da porção dos dados que é utilizada para teste
# random state é para o valor inicial(seed)
test_size = 0.9  #mudar para 0.1
random_state=42
x_train, x_test, y_train, y_test = train_test_split(iris[["s_length","s_width","p_length","p_width"]], iris["class"], test_size=test_size, random_state=random_state)

### KNeighbors
# treinar o amigo
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

KN_y_pred = knn.predict(x_test)

KN_accuracy = accuracy_score(y_test, KN_y_pred)
KN_recall = recall_score(y_test, KN_y_pred, average="weighted")
KN_precision = precision_score(y_test, KN_y_pred, average="weighted")
print("KNeighbors")
KN_cm = confusion_matrix(y_test,KN_y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(KN_cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("True")
#KN_results = pd.DataFrame({"Actual":y_test, "Predicted":KN_y_pred})
#print(KN_results)
print("Accuracy:", KN_accuracy)
print("Recall:", KN_recall)
print("Precision:", KN_precision)
plt.show()
print("--------------------------")



### Linear SVC
svc = LinearSVC()
svc.fit(x_train,y_train)

SVC_y_pred = svc.predict(x_test)

print("SVC")
SVC_accuracy = accuracy_score(y_test, SVC_y_pred)
SVC_recall = recall_score(y_test, SVC_y_pred, average="weighted")
SVC_precision = precision_score(y_test, SVC_y_pred, average="weighted")
print("KNeighbors")
SVC_cm = confusion_matrix(y_test,SVC_y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(SVC_cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("True")
#SVC_results = pd.DataFrame({"Actual":y_test, "Predicted":SVC_y_pred})
#print(SVC_results)
print("Accuracy:", SVC_accuracy)
print("Recall:", SVC_recall)
print("Precision:", SVC_precision)
plt.show()
print("--------------------------")



### Naive Bayes
gnb = GaussianNB()
gnb.fit(x_train,y_train)

GNB_y_pred = gnb.predict(x_test)

print("GNB")
GNB_accuracy = accuracy_score(y_test, GNB_y_pred)
GNB_recall = recall_score(y_test, GNB_y_pred, average="weighted")
GNB_precision = precision_score(y_test, GNB_y_pred, average="weighted")
print("KNeighbors")
GNB_cm = confusion_matrix(y_test,GNB_y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(GNB_cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("True")
#GNB_results = pd.DataFrame({"Actual":y_test, "Predicted":GNB_y_pred})
#print(GNB_results)
print("Accuracy:", GNB_accuracy)
print("Recall:", GNB_recall)
print("Precision:", GNB_precision)
plt.show()
print("--------------------------")