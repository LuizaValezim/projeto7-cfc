import numpy as np
from scipy.signal.signaltools import resample
import sounddevice as sd
from suaBibSignal import *
import time
import peakutils
from peakutils.plot import plot as pplot
from matplotlib import pyplot

#Importe todas as bibliotecas
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

#funcao para transformas intensidade acustica em dB
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)


def main():
    #declare um objeto da classe da sua biblioteca de apoio (cedida)
    bib = signalMeu()    
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    fs = 44100 # Hz
    
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    
    sd.default.samplerate = fs #taxa de amostragem
    sd.default.channels = 1  #voce pode ter que alterar isso dependendo da sua placa

    # faca um printo na tela dizendo que a captacao comecará em n segundos. e entao
    tempoEspera = 3
    print(f"Gravação começará em {tempoEspera} segundos")
    #use um time.sleep para a espera
    time.sleep(tempoEspera)
   
    #faca um print informando que a gravacao foi inicializada
    print("Gravação iniciada")
    #declare uma variavel "duracao" com a duracao em segundos da gravacao. poucos segundos ... 
    duration = 2 #tempo em segundos que ira aquisitar o sinal acustico captado pelo mic
    #calcule o numero de amostras "numAmostras" que serao feitas (numero de aquisicoes)
    numAmostras = fs*duration
    freqDeAmostragem = fs

    audio = sd.rec(int(numAmostras), samplerate=freqDeAmostragem, channels=1)
    sd.wait()
    print("...     FIM")
    audio = np.squeeze(np.array(audio))

    #Remover frequencias menores que 500
    # print(np.shape(np.array(audio)))  #Pegar shape do audio

    # lsFiltrada  = [0 if f <= 500 else f for f in audio]
    # audio = lsFiltrada
    
    #analise sua variavel "audio". pode ser um vetor com 1 ou 2 colunas, lista ...
    #grave uma variavel com apenas a parte que interessa (dados)
    
    # print(audio)

    # use a funcao linspace e crie o vetor tempo. Um instante correspondente a cada amostra!
    inicio = 0
    fim = 10
    numPontos = 5
    t = np.linspace(inicio, fim, numPontos)

    # plot do grafico  áudio vs tempo!
   
    
    ## Calcula e exibe o Fourier do sinal audio. como saida tem-se a amplitude e as frequencias
    xf, yf = bib.calcFFT(audio, fs)
    for i, x in enumerate(xf):
        if x <= 500 or x >= 1800:
            yf[i] = 0
    plt.figure("F(y)")
    plt.plot(xf,yf)
    plt.grid()
    plt.xlabel("Frequência")
    plt.ylabel("Intensidade")
    plt.title('Fourier audio')
    plt.show()
    

    #esta funcao analisa o fourier e encontra os picos
    #voce deve aprender a usa-la. ha como ajustar a sensibilidade, ou seja, o que é um pico?
    #voce deve tambem evitar que dois picos proximos sejam identificados, pois pequenas variacoes na
    #frequencia do sinal podem gerar mais de um pico, e na verdade tempos apenas 1.
   
    index = peakutils.indexes(yf,thres=0.1, min_dist=100)
    
    #printe os picos encontrados! 
    print(index)
    resFrequency = xf[index]
    if len(resFrequency) != 2:
        print("Achou mais ou menos que duas frequencias")
        print(len(resFrequency))
        return
    f1 = resFrequency[0]
    f2 = resFrequency[1]
    print(f"Frequencias: {resFrequency[0]} e {resFrequency[1]}")
    tol = 60
    for n, freq in dict_frequencies.items():
        if freq[0]+tol >= f1 >= freq[0]-tol:
            if freq[1]+tol >= f2 >= freq[1]-tol:
                print(f"Caractere digitado no encoder: {n}")
                break

    # print(t[index], yf[index])
    # pyplot.figure(figsize=(10,6))
    # pplot(t, yf, index)
    # plt.xlabel("Tempo")
    # plt.ylabel("Áudio")
    # pyplot.title('First estimate')
    
    #encontre na tabela duas frequencias proximas às frequencias de pico encontradas e descubra qual foi a tecla
    
    # print(f"Com a frequência {} e {}, a tecla pressionada foi {}")
    
  
    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()
