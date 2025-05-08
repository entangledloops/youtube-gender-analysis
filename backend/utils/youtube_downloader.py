import os
import subprocess
import tempfile

def download_youtube_audio(youtube_url):
    with tempfile.TemporaryDirectory() as temp_dir:
        # Construct the command to download audio from YouTube
        command = [
            'youtube-dl', 
            '-x', 
            '--audio-format', 'wav', 
            '--output', os.path.join(temp_dir, '%(title)s.%(ext)s'), 
            youtube_url
        ]
        
        # Execute the command
        subprocess.run(command, check=True)
        
        # Find the downloaded audio file
        for file in os.listdir(temp_dir):
            if file.endswith('.wav'):
                return os.path.join(temp_dir, file)
    
    return None