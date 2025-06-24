from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("ids_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[f'feature{i}']) for i in range(1, 5)]
        prediction = model.predict([features])[0]
        result = "Intrusion Detected" if prediction == 1 else "Normal Traffic"
    except:
        result = "Error in input. Please check all fields."
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
