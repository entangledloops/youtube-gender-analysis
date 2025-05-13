import os
import tempfile
import librosa
import soundfile as sf

def extract_first_10_seconds(audio_file_path, start_time=0, duration=10):
    """
    Extract a segment of audio from the given file.
    
    Args:
        audio_file_path: Path to the audio file
        start_time: Start time in seconds
        duration: Duration of segment in seconds
        
    Returns:
        Path to the extracted segment
    """
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError(f"The audio file {audio_file_path} does not exist.")
    
    # Load the audio file with specified duration
    try:
        audio, sr = librosa.load(audio_file_path, sr=None, offset=start_time, duration=duration)
    except Exception as e:
        print(f"Error loading audio file: {str(e)}")
        raise
    
    # Create a temporary file for the segment
    temp_file = tempfile.mktemp(suffix=".wav")
    
    # Save the segment
    sf.write(temp_file, audio, sr)
    
    return temp_file