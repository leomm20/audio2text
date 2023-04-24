import os
import shutil
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

counter = 0
for file in path.glob('*.*'):
    audio_to_wav(file)
    counter += 1
print(f'\nProcessed {counter} files\n')

if counter > 0:
    r = input('Move files to audios for extract text? (y/n): ')
    if r in ['y', 'Y']:
        for file in Path(path, 'processed').glob('*.*'):
            shutil.move(file, '.\\audios')
        print('Ready!\n')
