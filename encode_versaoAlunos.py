import matplotlib
import numpy as np

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

def getFrequencies(n):


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
     #declare um objeto da classe da sua biblioteca de apoio (cedida)    
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    
    
    duration = 2    #tempo em segundos que ira emitir o sinal acustico 
      
#relativo ao volume. Um ganho alto pode saturar sua placa... comece com .3    
    gainX  = 0.3
    gainY  = 0.3


    print("Gerando Tons base")
    
    #gere duas senoides para cada frequencia da tabela DTMF ! Canal x e canal y 
    #use para isso sua biblioteca (cedida)
    #obtenha o vetor tempo tb.
    #deixe tudo como array

    #printe a mensagem para o usuario teclar um numero de 0 a 9. 
    #nao aceite outro valor de entrada.
    print("Gerando Tom referente ao símbolo : {}".format(NUM))
    
    
    #construa o sunal a ser reproduzido. nao se esqueca de que é a soma das senoides
    
    #printe o grafico no tempo do sinal a ser reproduzido
    # reproduz o som
    sd.play(tone, fs)
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio
    sd.wait()

if __name__ == "__main__":
    main()
