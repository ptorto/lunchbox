######## -- INICIO -- bibliotecas Generales ###########################
import io # control audio files for translation.
import os  # Firebase, Google STT cred.
import time
import argparse
import sys
import thread
######## -- FIN-- bibliotecas Generales ###########################

from models.LUNCHBOX import LunchBox
from models.KID import Kid

from speech.gTTS import googleTTS ##TextToSpeech de google cloud ##
from speech.gSTT import googleSTT ##SpeechToText de google cloud ##

global kid
global lunchBox


def main():
    
    ##revisar si tenemos registro##
    loadData()

        
    #NO - ir inicializacion
    
    #SI - empezar
        #estar revisando constantemente conexion a internet (cada 10 seg)
        #estar viendo la hora del dia
        #modo online y modo ofline
        #modo standby modo prendido

def inicialSetup():
    ##hacer conexion por BT y luego por wifi
    lunchBox = LunchBox()
    
    googleTTS('hola, soy la nueva lochera.')
    googleTTS('Vamos a comenzar con la configuracion.')
    googleTTS('Por favor, dime tu nombre.')
    
    intentos = 0
    while intentos<3
        try:
            os.system('arecord -r 16000 -f S16_LE speech/temp/setup.wav -d 3')
            kid = Kid(googleSTT('setup.wav'))
            break
        except:
            googleTTS('No entendi, por favor, repite tu nombre')
            intentos+=1
            if intentos == 2:
                

    googleTTS('Mucho gusto, '+kid.getName()+', ahora dime, ¿cuantos anios tienes?')
    os.system('arecord -r 16000 -f S16_LE speech/temp/setup.wav -d 3')

    kid.setAge(googleSTT('setup.wav'))

    googleTTS('Ya se que tienes '+kid.getAge()+'aniotes')
    googleTTS('Ahora dime, '+kid.getName()+', ¿cual es tu color favorito?')
    os.system('arecord -r 16000 -f S16_LE speech/temp/setup.wav -d 3')

    kid.setFavColor(googleSTT('setup.wav'))
    
    ##crear nino, lunchbox y cargar datos a app y subir a FireBase
    ##


################################################################
###CARGAR INFORMACION DE LUNCHBOX DESDE ARCHIVOS (SI EXISTEN)###
################################################################
    
def loadData():
    try:
        with open('bin/kid.pkl', 'rb') as input:
            kid = cPickle.load(input)
            try:
                with open('bin/lunchBox.pkl', 'rb') as input:
                    lunchBox = cPickle.load(input)
            except:
                print('no tengo archivo lunchBox')
    except:
        inicialSetup()


main()
