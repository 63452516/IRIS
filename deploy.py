from flask import Flask, render_template, request

import pickle

app = Flask(__name__)
model= pickle.load(open('irismodel.sav','rb'))

@app.route('/')
def home():
    result =''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST' , 'GET'])
def predict():
        
        sepal_length = float(request.form['SepalLengthCm'])
        sepal_width = float(request.form['SepalWidthCm'])
        petal_length = float(request.form['PetalLengthCm'])
        petal_width = float(request.form['PetalWidthCm'])
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        
        return render_template('index.html', **locals())

if __name__ ==  '__main__':
    app.run(debug=True)