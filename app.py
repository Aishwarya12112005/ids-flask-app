import joblib
import requests
import io

def download_model_from_gdrive(share_url):
    file_id = share_url.split('/d/')[1].split('/')[0]
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(download_url)
    if response.status_code != 200:
        raise Exception("Failed to download model from Google Drive.")
    return joblib.load(io.BytesIO(response.content))

# Load model from Google Drive
share_link = "https://drive.google.com/file/d/1NzqLuyVud-gphTpecXncMK6oGuWRv9JJ/view?usp=sharing"
model = download_model_from_gdrive(share_link)
