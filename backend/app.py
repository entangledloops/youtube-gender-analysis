from flask import Flask, request, jsonify
import torch
from model import ECAPA_gender
from utils.youtube_downloader import download_youtube_audio
from utils.audio_processor import extract_first_10_seconds

app = Flask(__name__)

# Load the gender classification model
model = ECAPA_gender.from_pretrained("JaesungHuh/voice-gender-classifier")
model.eval()

# If you are using gpu .... 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    video_url = data.get('url')

    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    # Download audio and extract the first 10 seconds
    audio_file = download_youtube_audio(video_url)
    segment_file = extract_first_10_seconds(audio_file, start_time=0, duration=10)

    with torch.no_grad():
        output = model.predict(segment_file, device=device)

    return jsonify({"gender": output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)