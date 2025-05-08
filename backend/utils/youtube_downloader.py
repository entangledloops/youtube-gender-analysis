import os
import tempfile
import subprocess
import shutil

def download_youtube_audio(url):
    """
    Download audio from a YouTube video URL using yt-dlp.
    
    Args:
        url: YouTube video URL
        
    Returns:
        Path to the downloaded audio file (WAV format)
    """
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    temp_output = os.path.join(temp_dir, "audio")
    
    try:
        # Prepare the yt-dlp command
        command = [
            "yt-dlp",
            "-x",  # Extract audio
            "--audio-format", "wav",  # Convert to WAV
            "--audio-quality", "0",  # Highest quality
            "-o", f"{temp_output}.%(ext)s",  # Output filename template
            url
        ]
        
        # Run the command
        print(f"Downloading audio from: {url}")
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            raise Exception(f"Failed to download audio: {result.stderr}")
        
        # The file will be named audio.wav in the temp directory
        output_path = f"{temp_output}.wav"
        
        if not os.path.exists(output_path):
            files = os.listdir(temp_dir)
            if len(files) > 0:
                # If the exact filename isn't found, try to find any WAV file
                for file in files:
                    if file.endswith(".wav"):
                        output_path = os.path.join(temp_dir, file)
                        break
            else:
                raise FileNotFoundError("No output file was created")
                
        return output_path
        
    except Exception as e:
        print(f"Error downloading YouTube audio: {str(e)}")
        # Clean up temp directory on error
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise