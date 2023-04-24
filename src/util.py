import os
import subprocess
from pathlib import Path


def audio_to_wav(audio_file):
    if not Path(audio_file.parent, 'processed').exists():
        os.mkdir(Path(audio_file.parent, 'processed'))
    try:
        new_file = str(Path(audio_file).stem) + '.wav'
        # run the FFmpeg command to convert the MP3/M4A file to WAV
        subprocess.run(["ffmpeg", "-i", audio_file, Path(audio_file.parent, 'processed', audio_file.stem+'.wav')])
    except:
        print('Error! Check environment variables! Add c:\\ffmpeg\\bin to path')


path = Path(os.getcwd(), 'audios_to_be_converted')
if not path.exists():
    print(f'Path {path} not found')
    exit()

for file in path.glob('*.*'):
    audio_to_wav(file)
