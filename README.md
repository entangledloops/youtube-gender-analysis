# Backend README for YouTube Gender Analysis Project

This README file provides information about the backend of the YouTube Gender Analysis project. The backend is responsible for processing requests from the frontend, analyzing audio from YouTube videos, and determining the gender of the speaker using a pre-trained model.

## Project Structure

The backend consists of the following files:

- **app.py**: The main entry point for the Flask application. It sets up the server and defines the API endpoints.
- **model.py**: Contains the logic for loading the gender classification model and predicting the gender based on audio input.
- **utils/youtube_downloader.py**: Functions for downloading audio from a YouTube video using the provided URL.
- **utils/audio_processor.py**: Functions for processing the downloaded audio to extract the first 10 seconds for analysis.
- **requirements.txt**: Lists the dependencies required for the backend application.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-gender-analysis/backend
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. The server will be running at `http://localhost:5000`. The frontend will send requests to this endpoint to analyze the audio.

## API Endpoint

- **POST /analyze**: Accepts a JSON payload with a YouTube video URL. It returns the predicted gender of the speaker in the audio.

## Model Loading

The gender classification model is loaded once when the server starts, ensuring efficient reuse for each request.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.