import joblib
import gdown
import os

# Google Drive file ID
file_id = "1NzqLuyVud-gphTpecXncMK6oGuWRv9JJ"
output_path = "model.pkl"

# Download the model only if not already downloaded
if not os.path.exists(output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)

# Load the model
model = joblib.load(output_path)

# Your usual Flask app code here...
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Model loaded successfully!"

if __name__ == '__main__':
    app.run()
