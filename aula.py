import os
import time, sys
clear = lambda: os.system('clear')
loop = 1
pontuacao = 0


def Cabecalho():
    time.sleep(1)  
    clear() 
    print("____________________________________")
    print("        Perguntas Biblicas          ")
    print("____________________________________")
    


while loop < 5:
    loop =loop +1 
    Cabecalho()
    resposta = input("Qual o nome primogenito de Jacó? ")
    if resposta == 'Ruben':
        pontuacao +=1
        print("Parabéns!! Acertou Placar: ", pontuacao)              
    else:
        print("Que pena! Você Errou")        
        exit()

    Cabecalho()
    print("O que significa Rabobi? ")
    print("( 1 ) - Pai")    
    print("( 2 ) - Mestre")    
    print("( 3 ) - Cristo")    
    resposta = int(input("R = "))
    if resposta == 1:
        print("Que pena! Você Errou")
        exit()  
    elif resposta ==2 :
        pontuacao +=1
        print("Parabéns!! Resposta correta Placar: ", pontuacao)       
    elif resposta == 3:
        print("Que pena! Você Errou")
        exit()
    else:
        print('Opção invalida!')
        
    Cabecalho()
    resposta = input("Quantos eram os discipulos de Jesus? ")
    if resposta == '12':
        pontuacao +=1
        print("Parabéns!! Acertou Placar: ", pontuacao)         
    else:
        print("Que pena! Você Errou")        
        exit()  

    Cabecalho()
    print("Quais eram os irmãos de Moises? ")
    print("( 1 ) - Arão e Miriam")    
    print("( 2 ) - Cora e Josue")    
    print("( 3 ) - Calebe e Ana")  

    resposta = int(input("R= "))
    if resposta == 1:
        pontuacao +=1
        print("Parabéns!! Resposta correta Placar: ", pontuacao)
    elif resposta ==2 :
        print("Que pena! Você Errou")
        exit()                
    elif resposta == 3:
        print("Que pena! Você Errou")
        exit()
    else:
        print('Opção invalida!')

    Cabecalho()
    print("Quantos dias Jesus Jejuou no deserto? ")
    print("( 1 ) - 30 dias")    
    print("( 2 ) - 5 dias")    
    print("( 3 ) - 40 dias")  

    resposta = int(input("R= "))
    if resposta == 1:
        print("Que pena! Você Errou")
        exit()       
    elif resposta ==2 :
        print("Que pena! Você Errou")
        exit()                
    elif resposta == 3:
         pontuacao +=1
         print("Parabéns!! Resposta correta Placar: ", pontuacao)        
    else:
        print('Opção invalida!')
else:
    print("Encerrando o Game!!")
        




