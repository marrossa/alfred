import sys
import os
import json
import configparser
import io
import requests
import pprint
import glob
import pyttsx3

def transcribe_file(speech_file, textFile):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='es-MX')

    response = client.recognize(config, audio)
    fileContent = open(textFile, 'w')
    for index, result in enumerate(response.results):
        responseIndex = result.alternatives[0].transcript.encode('utf-8', 'strict')
        print(responseIndex)
        fileContent.write(str(responseIndex))
    fileContent.close()

def query(query_text):
    from watson_developer_cloud import DiscoveryV1

    # Loads the config file to read the configuration variables
    config = configparser.ConfigParser()
    config.read('config.file')

    discovery = DiscoveryV1(
        username = config['watson']['username'],
        password = config['watson']['password'],
        version = config['watson']['version']
    )

    qopts = {'query': query_text, 'filter': ''}
    my_query = discovery.query(config['watson']['environment_id'], config['watson']['prod_collection_id'], qopts)
    #print(json.dumps(my_query, indent=2))
    json_res = json.loads(json.dumps(my_query, indent=2))
    if not json_res['results']:
        res = "No existen resultados para la busqueda"
    else:
        res = json_res['results'][0]['text']
    print(res)
    return res

def text_to_speech(text):
    from gtts import gTTS
    from playsound import playsound

    language = 'es'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')

if __name__ == '__main__':
    print("\n\n")
    print("*****************************************")
    print("*   W E L C O M E    T O   A L F R E D  *")
    print("*****************************************")
    print("\n")
    print("Please select one question:")
    index = 1
    for filename in glob.iglob('questions/*.wav'):
        print('[%s] - %s' % (index, filename))
        index +=1
    answer = input("Your answer: ")
    while (int(answer) < 1 or int(answer) > int(index)):
        answer = input("Invalid number, please try again: ")
    filename = "questions/Pregunta"+str(answer)+".wav"
    print("\n")
    print('Using google cloud service to transcribe: %s' % filename)
    textfilename = "Question"+str(answer)+".txt"
    transcribe_file(filename, textfilename)

    #Read the filename
    #with open('Question01.txt') as f:
    with open(textfilename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    res_txt = ' '.join(content)
    print("\n")
    print('Your question is: %s' % res_txt)
    print("Using Discovery Watson to get the best answer...")
    res_query = query(res_txt)
    print("\n")
    print('Response from watson: %s' % res_query)
    text_to_speech(res_query)
