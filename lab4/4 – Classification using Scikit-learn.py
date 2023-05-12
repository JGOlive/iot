import numpy as np
import scipy as sp
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.neighbors import KneighborsClassifier


X_train, X_test, y_train, y_test = train_test_split(iris[["s_length","s_width","p_length","p_width"]], iris["class"], test_size=0.2, random_state=42)