import pickle

NN_filename = "NN_Model.pkl"
with open(NN_filename, "rb") as file:
    nn_model = pickle.load(file)