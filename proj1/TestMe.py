import pandas as pd
import pickle

df = pd.read_csv("Lab6-Proj1_TestSet.csv")

NN_filename = "NN_Model.pkl"
with open(NN_filename, "rb") as file:
    nn_model = pickle.load(file)

# remove lines with missing information
test_file = df.dropna()



print(test_file)