import speech_recognition as sr
from pathlib import Path
import os
import sys


print('\nOnly works with .wav files!\n')
if len(sys.argv) > 1:
    if not Path(sys.argv[1]).exists():
        print('Path not found')
        exit()
    else:
        path = Path(sys.argv[1])
else:
    path = Path(os.getcwd(), 'audios')

print(f'Will continue with {path} path\n')

language = 'es-AR'
if len(sys.argv) > 2:
    if sys.argv[2].lower() == 'en-us':
        language = 'en-US'

if not path.exists():
    print('"audios" path not found')
    os.mkdir('audios')
    print('directory "audios" created, put your audio files in there')
    exit()
if not Path(path, 'processed').exists():
    os.mkdir(Path(path, 'processed'))

ls = os.listdir(path)
list_ = []
[list_.append(el) for el in ls if '.wav' in str(el)]
print('.wav files found: ' + str(len(list_)))
print()

r = sr.Recognizer()
for file in path.glob('*.wav'):
    print('File:', file.name)
    try:
        with sr.AudioFile(str(file)) as source:
            audio_data = r.listen(source)
    except:
        print("CAN'T OPEN THE FILE!!!\n")
        continue
    # recognize speech using Google Speech Recognition - Just for testing! For production use Google API KEY;
    # you can get it on https://www.chromium.org/developers/how-tos/api-keys/
    try:
        g_text = r.recognize_google(audio_data, language=language, show_all=True)
        texto = 'Text: ' + g_text['alternative'][0]['transcript'] + '\n'
        texto = texto + 'Approximation: ' + str(round(float(g_text['alternative'][0]['confidence']) * 100, 2)) + '%'
        with open(Path(path, 'processed', file.stem + '.txt'), 'w') as f:
            f.write(texto)
        os.rename(file, Path(path, 'processed', file.name))
        print(texto)
        print('*' * 50)
    except sr.UnknownValueError:
        print("\nGoogle doesn't understand speech")
    except sr.RequestError as e:
        print("\nCommunication error. Google Voice Recognition Service doesn't respond; {0}".format(e))
    except Exception as e:
        print('\nGeneric error', e)
