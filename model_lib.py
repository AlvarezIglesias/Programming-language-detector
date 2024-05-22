import pickle


def import_random_forest():
    loaded_model = pickle.load(open("random_forest.sav", 'rb'))
    return loaded_model

def import_xgboost():
    loaded_model = pickle.load(open("xgboost.sav", 'rb'))
    return loaded_model

def import_neural_net():
    loaded_model = pickle.load(open("neural_net.sav", 'rb'))
    return loaded_model

def import_naive_bayes():
    loaded_model = pickle.load(open("naive_bayes.sav", 'rb'))
    return loaded_model

def import_text_or_code():
    loaded_model = pickle.load(open("text_or_code.sav", 'rb'))
    return loaded_model
