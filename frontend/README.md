# Frontend Documentation for YouTube Gender Analysis Project

This project is a web application that allows users to analyze the gender of a speaker in a YouTube video. The application consists of a frontend built with React and a backend powered by Flask.

## Features

- Accepts a YouTube video URL.
- Analyzes the first 10 seconds of audio from the video.
- Displays the predicted gender of the speaker.

## Getting Started

### Prerequisites

- Node.js and npm should be installed on your machine.

### Installation

1. Navigate to the frontend directory:
   ```
   cd youtube-gender-analysis/frontend
   ```

2. Install the dependencies:
   ```
   npm install
   ```

### Running the Application

To start the development server, run:
```
npm start
```
This will launch the application in your default web browser at `http://localhost:3000`.

### Project Structure

- **public/index.html**: Main HTML file for the application.
- **src/App.js**: Main component that manages application state.
- **src/components/AnalysisForm.js**: Component for the form to input YouTube URL.
- **src/components/ResultDisplay.js**: Component to display the analysis result.
- **src/styles/**: Contains CSS files for styling the application.

### Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

### License

This project is licensed under the MIT License. See the LICENSE file for details.