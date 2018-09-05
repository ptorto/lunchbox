from google.cloud import speech
from google.cloud.speech import enums ##necesario?
from google.cloud.speech import types ##necesario?
from google.cloud import texttospeech
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/bin/Smart-Lunchbox-test-c81910c2b633.json"


def googleSTT(file):
    client = speech.SpeechClient()
# Loads the audio into memory
    with io.open('speech/temp/'+file, 'rb') as audio_file:
        content = audio_file.read() 
        audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='es-MX')
# Detects speech in the audio file
    response = client.recognize(config, audio)
    return response.results[0].alternatives[0].transcript.encode('UTF-8')
