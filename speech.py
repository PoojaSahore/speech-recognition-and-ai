import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True

def echo(text):
    subprocess.call('echo ' + text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format =   pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print('Listening...')
    play_audio('audio/wet.wav')

    with sr.Microphone() as source:
        print('Say something...')
        audio = r.listen(source, timeout=1, phrase_time_limit=8)
    play_audio('audio/suppressed.wav')

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print('Couldn\'t understand...')

    # global running
    # if command == 'quit':
    #     running = False

    if command in ['quit', 'exit', 'bye', 'goodbye']:
        global running
        running = False
    
    echo('You said: ' + command)
    cmd.discover(command)

while running == True:
    initSpeech()