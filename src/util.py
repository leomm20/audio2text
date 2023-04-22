import subprocess

# run the FFmpeg command to convert the MP3/M4A file to WAV
subprocess.run(["ffmpeg", "-i", "Grabación.m4a", "grabacion.wav"])

