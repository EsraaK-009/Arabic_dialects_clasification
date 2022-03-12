import pickle
import os
from keras.models import model_from_json
from joblib import load



def get_models(dir_path):
    ml_model = load(dir_path +'/models/SVCModel.joblib')
    json_file = open(dir_path +'/models/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    dl_model = model_from_json(loaded_model_json)
    # load weights into new model
    dl_model.load_weights(dir_path +'/models/model.h5')
    
    # getting tokenizer and encoder
    with open(dir_path+'/models/tokenizer.pickle', 'rb') as handle:
    	tokenizer = pickle.load(handle)
    with open(dir_path+'/models/encoder.pkl', 'rb') as handle:
    	encoder = pickle.load(handle)   
    return ml_model,dl_model,tokenizer,encoder
    
    
    
    



