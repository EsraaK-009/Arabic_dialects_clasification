from flask import Flask
from flask import request
import numpy as np
from helper_functions.preprocessing import pre_processing
from helper_functions.loading_models import get_models
from keras.preprocessing.sequence import pad_sequences
import os

app = Flask(__name__)
dir_path = os.getcwd()

ml_model,dl_model,tokenizer,encoder = get_models(dir_path)




@app.route("/ml", methods=['POST'])
def ml_predict():

	variable_name = request.get_json( )
	tweet = variable_name ['text']
	text = pre_processing(tweet)
	dialect = list(ml_model.predict([text]))[0]
	return dialect
    	    	
    	
@app.route("/dl", methods=['POST'])
def dl_predict():

		variable_name = request.get_json( )
		tweet = variable_name ['text']
		#tweet = request.args.get('text')
		text = pre_processing(tweet)
		#print(text)
		tokens = tokenizer.texts_to_sequences([text])
		
		#print(tokens)
		padded_tokens = pad_sequences(tokens, padding='post', maxlen=100)
		#print(padded_tokens)
		out = dl_model.predict(padded_tokens)
		#print(out)
		output = np.argmax(out)
		#print(output)
		dialect = list(encoder.inverse_transform([output]))[0]
		return dialect

        
        
        
if __name__ == '__main__':
    app.run(debug=True)
    
    
  
