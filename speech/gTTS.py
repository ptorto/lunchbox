from google.cloud import speech
from google.cloud.speech import enums ##necesario?
from google.cloud.speech import types ##necesario?
from google.cloud import texttospeech
import os

# definimos la ruta de las credenciales de GOOGLE Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/bin/Smart-Lunchbox-test-c81910c2b633.json"

def googleTTS(text):
    client = texttospeech.TextToSpeechClient()
    input_text=texttospeech.types.SynthesisInput(text=text)
    
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='es-ES',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
    
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding = texttospeech.enums.AudioEncoding.MP3)
    
    response = client.synthesize_speech(input_text, voice, audio_config)
    
    with open('temp/output.mp3', 'wb') as out:
        out.write(response.audio_content)
        os.system('mpg123 temp/output.mp3')
