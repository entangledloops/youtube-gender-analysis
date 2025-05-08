# YouTube Gender Analysis Project

This project is a web application that analyzes the gender of a speaker in a YouTube video. It consists of a frontend built with React and a backend powered by Flask. The application allows users to input a YouTube video URL, extracts the audio from the first 10 seconds of the video, and uses a pre-trained model to determine the speaker's gender.

## Project Structure

The project is organized into two main directories: `frontend` and `backend`.

### Frontend

- **public/index.html**: The main HTML file for the frontend application.
- **src/App.js**: The main component that manages the application state and renders the form and result display.
- **src/components/AnalysisForm.js**: A component that contains the form for inputting the YouTube URL and submitting the analysis request.
- **src/components/ResultDisplay.js**: A component that displays the result of the gender analysis.
- **src/styles/**: Contains CSS files for styling the application.
- **package.json**: Configuration file for the frontend application.

### Backend

- **app.py**: The main entry point for the backend application, setting up the Flask server and defining API endpoints.
- **model.py**: Contains the logic for loading the gender classification model and making predictions.
- **utils/youtube_downloader.py**: Functions for downloading audio from YouTube videos.
- **utils/audio_processor.py**: Functions for processing the downloaded audio to extract the first 10 seconds.
- **requirements.txt**: Lists the dependencies required for the backend application.
- **README.md**: Documentation specific to the backend application.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-gender-analysis
   ```

2. Set up the backend:
   - Navigate to the `backend` directory:
     ```
     cd backend
     ```
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory:
     ```
     cd ../frontend
     ```
   - Install the required Node.js packages:
     ```
     npm install
     ```

### Running the Application

1. Start the backend server:
   ```
   cd backend
   python app.py
   ```

2. Start the frontend application:
   ```
   cd ../frontend
   npm start
   ```

3. Open your web browser and go to `http://localhost:3000` to access the application.

## Usage

1. Enter a YouTube video URL in the provided input field.
2. Click the "Analyze" button to submit the request.
3. The application will process the audio and display the predicted gender of the speaker.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.