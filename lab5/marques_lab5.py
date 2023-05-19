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

    ## iris
iris_data_file = pd.read_csv("iris.data",names=["s_length","s_width","p_length","p_width","class"])

