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

# read files
    ## haberman
haberman_data_file = pd.read_csv("haberman.data",names=["p_age", "year_op", "n_pos_auxn", "surv_stat"])

    ## iris
iris_data_file = pd.read_csv("iris.data",names=["s_length","s_width","p_length","p_width","class"])

# data processing
    ## haberman
haberman_target = haberman_data_file["surv_stat"]
cols = [col for col in haberman_data_file.columns if col not in ["surv_stat"]]
haberman_data = haberman_data_file[cols]

    ## iris

# splitting into train and test sets
haberman_ts = 0.3
haberman_rs = 10   
    ## haberman
        ## split into (train) and (validation + test)
haberman_data_train, haberman_data_valtest, haberman_target_train, haberman_target_valtest = train_test_split(haberman_data,haberman_target, test_size = haberman_ts, random_state = haberman_rs)
        ## plit into (validation) + (test)
haberman_data_val, haberman_data_test, haberman_target_val, haberman_target_test = train_test_split(haberman_data,haberman_target, test_size = 0.5, random_state = haberman_rs)
    ## iris

# Test

# Training using GaussianNB
    ## haberman (Linear SVC, if not working, KNeighbors)
lsvc_haberman = LinearSVC(random_state=0)
lsvc_haberman.fit(haberman_data_train,haberman_target_train)

    ## iris (Linear SVC, if not working, KNeighbors)

# Validation
    ## haberman

# Test
gnb_haberman_predict = lsvc_haberman.predict(haberman_data_test)
# Confusion matrixes
    ## haberman
haberman_cm = confusion_matrix(haberman_target_test, gnb_haberman_predict)
plt.figure(figsize=(8, 6))
sns.heatmap(haberman_cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("True")
