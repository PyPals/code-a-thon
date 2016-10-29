#!/usr/bin/python

# NOTE: this example requires PyAudio because it uses the Microphone class
from difflib import SequenceMatcher
import speech_recognition as sr

inp1 = 'A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent'.lower()
inp2 = 'The hungry purple dinosaur ate the kind, zingy fox, the jabbering crab, and the mad whale and started vending and quacking'.lower()
inp_list = [inp1, inp2]

def get_transcript(audio, index):
    try:
        transcription = r.recognize_google(audio, show_all = "True")
        # print type(transcription), transcription
        transcription = transcription['alternative']
        acc = []
        for i in transcription:
            res = str(i['transcript'])
            with open('result', 'a+') as f:
                f.write(inp_list[index] + "| " + res + "| " + str(SequenceMatcher(None, inp_list[index], res.lower()).ratio())+"\n")
    except sr.UnknownValueError:
        print("Voice Recognition API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from API service; {0}".format(e))

r = sr.Recognizer()

if __name__ == '__main__':
    for i in inp_list:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.record(source, duration = 15)
            get_transcript(audio, inp_list.index(i))
