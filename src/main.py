import speech_recognition as sr
from pathlib import Path
import os
import sys

print('Sólo funciona con archivos .wav\n')
if len(sys.argv) > 1:
    if not Path(sys.argv[1]).exists():
        print('No existe el directorio')
        exit()
    else:
        ruta = Path(sys.argv[1])
else:
    ruta = Path(os.getcwd(), 'audios')

print(f'Prosigo con ruta {ruta}')

if not ruta.exists():
    print('No existe directorio audios')
    exit()
if not Path(ruta, 'procesados').exists():
    os.mkdir(Path(ruta, 'procesados'))

ls = os.listdir(ruta)
lista = []
[lista.append(el) for el in ls if '.wav' in str(el)]
print('Archivos .wav encontrados: ' + str(len(lista)))
print()

r = sr.Recognizer()
for archivo in ruta.glob('*.wav'):
    print('Archivo:', archivo.name)
    try:
        with sr.AudioFile(str(archivo)) as source:
            audio_data = r.listen(source)
    except:
        print('NO SE PUDO ABRIR EL ARCHIVO!!!\n')
        continue
    # recognize speech using Google Speech Recognition - Sólo para testear, sino, poner la API KEY de google;
    # pasos para conseguirla: https://www.chromium.org/developers/how-tos/api-keys/
    try:
        text = r.recognize_google(audio_data, language='es-AR', show_all=True)
        texto = 'Texto: ' + text['alternative'][0]['transcript'] + '\n'
        texto = texto + 'Aproximación: ' + str(round(float(text['alternative'][0]['confidence']) * 100, 2)) + '%'
        with open(Path(ruta, 'procesados', archivo.stem + '.txt'), 'w') as f:
            f.write(texto)
        os.rename(archivo, Path(ruta, 'procesados', archivo.name))
        print(texto)
        print('*' * 50)
    except sr.UnknownValueError:
        print("No se entendió el audio")
    except sr.RequestError as e:
        print("Error de comunicación con el servicio Reconocimiento de Voz de Google; {0}".format(e))
    except:
        print('Error genérico')
