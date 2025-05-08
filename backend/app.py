from flask import Flask, request, jsonify
import torch
from model import ECAPA_gender
from utils.youtube_downloader import download_youtube_audio
from utils.audio_processor import extract_first_10_seconds
from flask_cors import CORS  # Import CORS
import os

app = Flask(__name__)

# Get allowed origins from environment variable or use default
allowed_origins = os.environ.get('CORS_ALLOWED_ORIGINS', '*')
print(f"CORS allowed origins: {allowed_origins}")

# Enable CORS with proper configuration
CORS(app, resources={
    r"/*": {
        "origins": allowed_origins.split(","),
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Load the gender classification model
model = ECAPA_gender.from_pretrained("JaesungHuh/voice-gender-classifier")
model.eval()

# If you are using gpu .... 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Log the incoming request
    print(f"Received request: {request}")
    
    try:
        data = request.json
        video_url = data.get('url')

        if not video_url:
            return jsonify({"error": "No URL provided"}), 400

        print(f"Processing video URL: {video_url}")
        
        # Download audio and extract the first 10 seconds
        audio_file = download_youtube_audio(video_url)
        segment_file = extract_first_10_seconds(audio_file, start_time=0, duration=10)

        with torch.no_grad():
            output = model.predict(segment_file, device=device)
            
        print(f"Analysis result: {output}")
        return jsonify({"gender": output})
    
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)