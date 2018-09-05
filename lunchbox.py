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
    googleTTS('hola, soy la nueva lochera')
    googleTTS('Vamos a comenzar con la configuracion')
    googleTTS('Por favor, dime tu nombre')    
    os.system('arecord -r 16000 -f S16_LE audio_files/STT_audio_test.wav -d 3')
    
    nombre = raw_input('nombre: "')
    kid = Kid(nombre)
    
    ##crear nino, lunchbox y cargar datos a app y subir a FireBase
    ##

##CARGAR ARCHIVOS###
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
##FIN CARGAR ARCHIVOS##
            
main()
