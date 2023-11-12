import numpy as np
from flask import Flask, request, jsonify
import pickle
from PIL import Image

app = Flask(__name__)
model = pickle.load(open(r'download/Trained_Model.sav','rb'))

@app.route('./index')
def home():
    if request.method == 'GET':
        return render_template('index.html', msg='')

    image = request.files['file']
    image = Image.open(image)

    print(image)

    return render_template('index.html', msg='Your image has been uploaded')

def Malaria_Diagnostic_Aid(image):
    image=image.resize(150,150)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image/255
    prediction_prob = model.predict(image)

    if prediction_prob > 0.5: label = 'Parisite detected'
    else: label = 'No Parasite detected'
    return(label,prediction_prob)
