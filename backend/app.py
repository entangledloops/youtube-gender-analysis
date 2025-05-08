from flask import Flask, request, jsonify
import torch
from model import ECAPA_gender
from utils.youtube_downloader import download_youtube_audio
from utils.audio_processor import extract_first_10_seconds
from flask_cors import CORS  # Import CORS
import os
import sys
import traceback

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
print("Loading gender classification model...")
try:
    model = ECAPA_gender.from_pretrained("JaesungHuh/voice-gender-classifier")
    model.eval()

    # If you are using gpu .... 
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    model.to(device)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    traceback.print_exc()
    # Continue anyway, as the model might load later

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
        try:
            print(f"Downloading audio from URL: {video_url}")
            audio_file = download_youtube_audio(video_url)
            print(f"Audio downloaded to: {audio_file}")
            
            print(f"Extracting first 10 seconds from: {audio_file}")
            segment_file = extract_first_10_seconds(audio_file, start_time=0, duration=10)
            print(f"Audio segment extracted to: {segment_file}")
            
            # Check if files exist
            if not os.path.exists(audio_file):
                return jsonify({"error": "Failed to download audio file"}), 500
            if not os.path.exists(segment_file):
                return jsonify({"error": "Failed to extract audio segment"}), 500
        except Exception as e:
            print(f"Error in audio processing pipeline: {e}")
            traceback.print_exc()
            return jsonify({"error": f"Audio processing error: {str(e)}"}), 500

        try:
            print(f"Predicting gender from audio segment: {segment_file}")
            with torch.no_grad():
                output = model.predict(segment_file, device=device)
                
            print(f"Analysis result: {output}")
            return jsonify({"gender": output})
        except Exception as e:
            print(f"Error in model prediction: {e}")
            traceback.print_exc()
            return jsonify({"error": f"Model prediction error: {str(e)}"}), 500
    
    except Exception as e:
        print(f"Unhandled error processing request: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up temporary files
        try:
            if 'audio_file' in locals() and os.path.exists(audio_file):
                os.remove(audio_file)
                print(f"Removed temporary file: {audio_file}")
            if 'segment_file' in locals() and os.path.exists(segment_file):
                os.remove(segment_file)
                print(f"Removed temporary file: {segment_file}")
        except Exception as e:
            print(f"Error cleaning up temporary files: {e}")

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    """Simple endpoint to verify the server is running"""
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)