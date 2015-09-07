import webbrowser

part_1 = 'http://tts.voicetech.yandex.net/generate?text="'
part_2 = input()
part_3 = '"&format=mp3&lang=ru-RU&speaker=zahar&drunk=True&key=2ddb24a0-130a-4334-90c1-67c669b525d3'

webbrowser.open(part_1 + part_2 + part_3, new=0, autoraise=True)