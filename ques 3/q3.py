#!/usr/bin/python
import speech_recognition as sr
# from os import path
import os
import pydub
import json


with open('fwd/dictionery.json') as json_data:
    d  = json.load(json_data)#['data']

WAV_EXT = 'wav'

def get_text(f_name):
    if f_name.find('.') != -1:
        name, ext = f_name.split('.')
    else:
        return
    audio = pydub.AudioSegment.from_file(f_name, ext)
    out_name = name+'.'+WAV_EXT
    audio.export(out_name, format = WAV_EXT)
    r = sr.Recognizer()
    with sr.AudioFile(out_name) as source:
        audio = r.record(source)
    try:
        transcription = r.recognize_google(audio)
        print f_name, transcription
        with open('result', 'a+') as f:
            f.write(f_name + " " + transcription)
            f.write('\n')
        countMatches = [0]*len(d["data"])
        for i in xrange(len(d["data"])):
            for j in d["data"][i]["tags"]:
                if j in transcription:
                    countMatches[i] = countMatches[i] + 1
            for j in d['data'][i]["keywords"]:
                if j in transcription:
                    countMatches[i] = countMatches[i] + 1
        print d["data"][countMatches.index(max(countMatches))]["link"]

    except sr.UnknownValueError:
        print "Audio not understood"
    except sr.RequestError, e:
        print "Couldn't request results from API Service; {0}".format(e)
    os.remove(out_name)

if __name__ == '__main__':
    # path = raw_input('Enter path')
    path = 'fwd/q3data'
    files = os.listdir(path)
    files.sort()
    os.chdir(path)
    for f_name in files:
        get_text(f_name)