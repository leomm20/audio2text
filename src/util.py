import subprocess
from pathlib import Path

file = 'audio.m4a'

new_file = str(Path(file).stem) + '.wav'
# run the FFmpeg command to convert the MP3/M4A file to WAV
subprocess.run(["ffmpeg", "-i", file, new_file])

