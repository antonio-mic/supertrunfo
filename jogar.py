import pygame ,os ,sys , funpygame
import pickle
import random
from datetime import*
from pygame.locals import*
pygame.init()


arq = open("cartas.txt","r") #Abre o txt para ler as
obtercartas1 = arq.read() #Lê o txt com as cartas
obtercartas1 = obtercartas1.split() #Obtem as cartas e atributos pelos espaços
arq.close() #Fecha o txt
numdecartas = int(len(obtercartas1)/8) #Pega o numero de cartas
cartasdividi = [[]]
for i in range(0,numdecartas):
    carta = i * 8
    cartasdividi[i] = [ obtercartas1[carta] , (int)(obtercartas1[carta + 1]) , (int)(obtercartas1[carta + 2]) , (int)(obtercartas1[carta + 3]) , (int)(obtercartas1[carta + 4]) , (int)(obtercartas1[carta + 5]) , obtercartas1[carta + 6] , obtercartas1[carta + 7] ] 
    cartasdividi.append(cartasdividi[i])
cartasdividi.pop(numdecartas)
superTrunfo = cartasdividi[0][0]
print(superTrunfo)

random.shuffle(cartasdividi)                                   # 
totaldecartas = int(len(cartasdividi))                         # 
n = metadecartas = int(totaldecartas / 2)                      #Dividi o total de cartas para os jogadores 
jogador1 = cartasdividi[0:metadecartas]                        # 
jogador2 = cartasdividi[metadecartas:totaldecartas]            #            



partida = random.randint(0,1) #Verifica quem vai com

tamanho = (700,500)
tela = pygame.display.set_mode(tamanho)
nome1 = ''
nome2 = ''
salvar = ''
nomedoarquivo = ''
background = pygame.image.load("imagens/fundoNome.png")
menufonte = pygame.font.SysFont('Arial.ttf',30)
nomeJogador1 = menufonte.render("Jogador1:" + nome1,True,(0,0,0))

continuar = True
digitarNome1 = True
while continuar and digitarNome1:
    tela.blit(background,(0,0))
    tela.blit(nomeJogador1,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
    
            
            teclado = pygame.key.get_pressed()
            nome1 = nome1 + event.unicode
            nomeJogador1 = menufonte.render("Jogador1:" + nome1,True,(0,0,0))
            pygame.display.flip()
            if teclado[K_BACKSPACE]:
                numeroNome1 = len(nome1)
                nomeNovo = nome1[0:numeroNome1 - 2]
                nome1= nomeNovo
                nomeJogador1 = menufonte.render("Jogador1:" + nome1,True,(0,0,0))
                pygame.display.flip()
                
            elif teclado[K_RETURN]:
                numeroNome1 = len(nome1)
                nomeNovo = nome1[0:numeroNome1 - 1]
                nome1= nomeNovo
                digitarNome1= False
    pygame.display.flip()

    pygame.display.flip()
salvar = salvar.upper()
print(salvar)


if salvar == "SIM":
    print("")
else:
    del nomedoarquivo
    import funpygamesingle
    funpygamesingle.jogar(jogador1,jogador2,partida,superTrunfo,nome1,nome2,"")
    



