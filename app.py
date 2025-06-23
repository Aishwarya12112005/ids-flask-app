import gdown

url = "https://drive.google.com/uc?id=1NzqLuyVud-gphTpecXncMK6oGuWRv9JJ"
output_path = "ids_model.pkl"

gdown.download(url, output_path, quiet=False)

# Then your ML model is loaded
import joblib
model = joblib.load(output_path)