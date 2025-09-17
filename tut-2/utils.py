import pickle

def load_ml_model(path="./model.pkl"):
    with open(path,'rb') as f:
        model = pickle.load(f)
    return model