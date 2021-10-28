import numpy as np
import sounddevice as sd
from suaBibSignal import *
import time

bib = signalMeu()

dict_frequencies = {'1': [697, 1209], 
                    '2': [697, 1336], 
                    '3': [697, 1477], 
                    '4': [770, 1209], 
                    '5': [770, 1336],
                    '6': [770, 1477],
                    '7': [852, 1209], 
                    '8': [852, 1336],
                    '9': [852, 1447],
                    '0': [941, 1336],
                    'A': [697, 1633],
                    'B': [770, 1633],
                    'C': [852, 1633],
                    'D': [941, 1633],
                    'X': [941, 1209],
                    '#': [941, 1477]}


def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)


#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)


def main():
    print("Inicializando encoder")
    
    numero = input("Escolha um número de 1 à 9 ou A,B,C,D ou X,#: ")

    #relativo ao volume. Um ganho alto pode saturar sua placa... comece com .3    
    gainX  = 0.3
    gainY  = 0.3
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    fs = 44100 # Hz
    duration = 3    #tempo em segundos que ira emitir o sinal acustico 

    print("Gerando Tons base")

    f1 = dict_frequencies[numero][0]
    sen1 = bib.generateSin(f1, gainX, duration, fs)
    f2 = dict_frequencies[numero][1]
    sen2 = bib.generateSin(f2, gainY, duration, fs)

    array = sen1[1] + sen2[1]

    print("Gerando Tom referente ao símbolo : {}".format(numero))
    
    #printe o grafico no tempo do sinal a ser reproduzido
    bib.plotFFT(array, fs)
    # reproduz o som
    sd.play(array)
    sd.wait()
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio
    sd.wait()

if __name__ == "__main__":
    main()
