.wav to text converter with speech_recognition
It works in command line too!

In util.py you have a mp3/m4a/and more* converter if you need

* to find out the accepted extension files:
execute 'ffmpeg -formats' in terminal

---------------------------------------------------

1.Extract ffmpeg_copy_in_c_root.zip to c:\ffmpeg
2.Add c:\ffmpeg\bin in path (you can execute add_ffmpeg_to_path.bat)
3.pip install speech_recognition
4.Save .wav files in some path (ex: c:\audios)
5.In terminal: cd [path_to_audio2text]\src
6.Execute python main.py [optional: [path_to_audio2text]]
(you can put your audio files in src\audios and just execute python.main.py)