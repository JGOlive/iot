import numpy as np
import scipy as sp
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

iris = pd.read_csv("iris.data", names=["s_length","s_width","p_length","p_width","class"])

X_train, X_test, y_train, y_test = train_test_split(iris[["s_length","s_width","p_length","p_width"]], iris["class"], test_size=0.2, random_state=42)

print(X_test)