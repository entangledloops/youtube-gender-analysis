import os
import librosa
import soundfile as sf

def extract_first_10_seconds(audio_file_path, output_file_path):
    if not os.path.exists(audio_file_path):
        raise FileNotFoundError(f"The audio file {audio_file_path} does not exist.")
    
    # Load the audio file
    audio, sr = librosa.load(audio_file_path, sr=None, duration=10)
    
    # Save the first 10 seconds to a new file
    sf.write(output_file_path, audio, sr)
    
    return output_file_path