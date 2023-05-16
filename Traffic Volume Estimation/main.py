import os
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle
with open(r'/home/seetharaman/Documents/flask-python/objects/model.pk1','rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict',methods=["POST","GET"])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_values = [np.array(input_features)]
    names = [['holiday','temp','rain','snow','weather','year','month','day','hours','minutes','seconds']]
    data = pd.DataFrame(features_values, columns = names)
    prediction = int(model.predict(data))
    print(prediction)
    text = "Estimated Traffic Volume is :"
    return render_template("index.html",prediction_text = text + str(prediction))

if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(port=port, debug=True,use_reloader = False)