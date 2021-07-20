from flask import Flask,jsonify,request
from classifier import get_prediction

app=Flask(__name__)
@app.route('/predict-digit',methods=['POST'])

def predict_data():
    image=request.files.get('digit')
    prediction=get_prediction(image)

    return jsonify({
        'prediction':prediction#key name, value


    }),200#port#request is successful

if __name__ == '__main__':
    app.run(debug=True)#It will check and display error



