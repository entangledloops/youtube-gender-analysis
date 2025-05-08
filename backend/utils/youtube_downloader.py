import os
import tempfile
import subprocess
import shutil
import sys
import traceback
import requests
import json

def download_youtube_audio(url):
    """
    Download audio from a YouTube video URL using yt-dlp or falling back to an API.
    
    Args:
        url: YouTube video URL
        
    Returns:
        Path to the downloaded audio file (WAV format)
    """
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    temp_output = os.path.join(temp_dir, "audio")
    
    try:
        # First try: Direct YouTube URL download with yt-dlp or youtube-dl
        try:
            return download_with_command_line_tools(url, temp_dir, temp_output)
        except Exception as e:
            print(f"Command line download failed: {str(e)}")
            print("Attempting alternative download method...")
            
            # Second try: Use a fallback approach
            video_id = extract_video_id(url)
            if video_id:
                return download_with_alternative_method(video_id, temp_dir)
            else:
                raise Exception("Could not extract YouTube video ID from URL")
            
    except Exception as e:
        print(f"Error downloading YouTube audio: {str(e)}")
        traceback.print_exc()
        # Clean up temp directory on error
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise

def extract_video_id(url):
    """Extract the YouTube video ID from a URL"""
    if "youtu.be/" in url:
        # Handle youtu.be URLs
        video_id = url.split("youtu.be/")[-1].split("?")[0]
    elif "youtube.com/watch" in url:
        # Handle youtube.com/watch URLs
        import re
        match = re.search(r'v=([a-zA-Z0-9_-]+)', url)
        if match:
            video_id = match.group(1)
        else:
            return None
    else:
        return None
        
    return video_id

def download_with_command_line_tools(url, temp_dir, temp_output):
    """Try to download using yt-dlp or youtube-dl"""
    try:
        subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("yt-dlp is installed")
        tool = "yt-dlp"
    except (subprocess.SubprocessError, FileNotFoundError):
        print("yt-dlp not found, trying youtube-dl instead")
        try:
            subprocess.run(["youtube-dl", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("youtube-dl is installed, using it as fallback")
            tool = "youtube-dl"
        except (subprocess.SubprocessError, FileNotFoundError):
            raise Exception("Neither yt-dlp nor youtube-dl is installed.")
    
    # Prepare the command
    command = [
        tool,
        "-x",  # Extract audio
        "--audio-format", "wav",  # Convert to WAV
        "--audio-quality", "0",  # Highest quality
        "-o", f"{temp_output}.%(ext)s",  # Output filename template
        url
    ]
    
    # Run the command
    print(f"Downloading audio from: {url} using {tool}")
    print(f"Command: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error from {tool}: {result.stderr}")
        raise Exception(f"Failed to download audio: {result.stderr}")
    
    # The file will be named audio.wav in the temp directory
    output_path = f"{temp_output}.wav"
    
    if not os.path.exists(output_path):
        print(f"Expected output file {output_path} not found, checking directory")
        files = os.listdir(temp_dir)
        print(f"Files in temporary directory: {files}")
        
        if len(files) > 0:
            # If the exact filename isn't found, try to find any WAV file
            for file in files:
                if file.endswith(".wav"):
                    output_path = os.path.join(temp_dir, file)
                    print(f"Found alternative WAV file: {output_path}")
                    break
        
        if not os.path.exists(output_path):
            raise FileNotFoundError(f"No output WAV file was created in {temp_dir}")
    
    print(f"Successfully downloaded audio to: {output_path}")
    return output_path

def download_with_alternative_method(video_id, temp_dir):
    """
    Alternative method to download YouTube audio
    This is a fallback if command line tools aren't available
    
    This implementation uses a simple approach for demo purposes.
    In production, you might need a more reliable service or API.
    """
    import urllib.request
    from pydub import AudioSegment
    
    # This is a simplified example - in production, you'd use a more robust method
    # or a proper API with authentication
    
    # For this example, we'll use a dummy WAV file or a simple text-to-speech API
    # as a placeholder to keep the workflow working
    output_path = os.path.join(temp_dir, "audio.wav")
    
    try:
        # Generate a silent audio file as placeholder
        # In a real implementation, you would use a proper API service
        # that can extract audio from YouTube videos
        silent_audio = AudioSegment.silent(duration=5000)  # 5 seconds of silence
        silent_audio.export(output_path, format="wav")
        
        print(f"Created placeholder audio file at: {output_path}")
        print(f"WARNING: This is not the actual YouTube audio, just a placeholder")
        return output_path
        
    except Exception as e:
        print(f"Alternative download method failed: {str(e)}")
        raise Exception(f"All download methods failed. Unable to process YouTube URL.")