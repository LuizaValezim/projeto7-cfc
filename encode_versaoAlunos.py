import numpy as np
import sounddevice as sd

dict_frequencies = {1: [697, 1209], 
                    2: [697, 1336], 
                    3: [697, 1477], 
                    4: [770, 1209], 
                    5: [770, 1336],
                    6: [770, 1477],
                    7: [852, 1209], 
                    8: [852, 1336],
                    9: [852, 1447],
                    0: [941, 1336],
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
    duration = 2    #tempo em segundos que ira emitir o sinal acustico 

    print("Gerando Tons base")

    sen1 = dict_frequencies[numero][0]
    sen2 = dict_frequencies[numero][1]
    array = sen1 + sen2

    recording = sd.playrec(array, fs, channels=2) 

    #obtenha o vetor tempo tb.
    #deixe tudo como array

    print("Gerando Tom referente ao símbolo : {}".format(numero))
    
    
    #construa o sunal a ser reproduzido. nao se esqueca de que é a soma das senoides
    
    #printe o grafico no tempo do sinal a ser reproduzido
    # reproduz o som
    sd.play(recording)
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio
    sd.wait()

if __name__ == "__main__":
    main()
