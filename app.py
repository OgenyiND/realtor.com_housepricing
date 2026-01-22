import pickle
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the full package
model_package = pickle.load(open('reg_model4.pkl', 'rb'))

model = model_package['model']
scaler = model_package['scaler']
features = model_package['features']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']

    X = pd.DataFrame([data], columns=features)
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)

    return jsonify(float(prediction[0]))

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]

    X = pd.DataFrame([data], columns=features)
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)

    return render_template(
        'home.html',
        prediction_text=f"The Predicted House Price is: ${prediction[0]:,.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)