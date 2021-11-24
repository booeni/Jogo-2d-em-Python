from os import X_OK
import pygame
import time
import random

NomeUsuario = input("Digite o seu nome: ")
emailUsuario = input("Digite o seu email: ")

dadosUsuario = "nome: " + NomeUsuario + "email: " + emailUsuario

with open("dadosDoUsuario.txt", "w") as arquivo:
    for valor in dadosUsuario:
        arquivo.write(str(valor))


pygame.init()
largura = 1000
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
pygame.display.set_caption(" Superman 2d")
icone = pygame.image.load("assets/icone.jpg")
pygame.display.set_icon(icone)
superman = pygame.image.load("assets/superman2.png")
superman = pygame.transform.rotate(superman, 90)
alturaSuperman = 200
larguraSuperman = 50
fundo = pygame.image.load("assets/fundo2.jpg")
fundo = pygame.transform.scale(fundo, (1000, 600))
missile = pygame.image.load("assets/missile2.png")
missile = pygame.transform.rotate(missile, 90)
missileAltura = 200
missileLargura = 20

somDeMorte = pygame.mixer.Sound("assets/somDeMorte.wav")
somDeMorte.set_volume(0.1)


def mostraMissile(x,y):
    gameDisplay.blit(missile, (x,y))

def mostraPersonagem(x,y):
    gameDisplay.blit(superman, (x, y))
    
def text_objects(texto, font):
    textSurface = font.render(texto,True, white)
    return textSurface, textSurface.get_rect()

def escreveNaTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 100)
    TextSurf, textRect = text_objects(texto, fonte)
    textRect.center = ((largura / 2, altura / 2))
    gameDisplay.blit(TextSurf, textRect)
    pygame.display.update()
    time.sleep(2)
    jogo()



def mostraPontuacao(contador):
    fonte = pygame.font.SysFont("Verdana", 30)
    texto = fonte.render("Pontuação: " + str(contador), True, black)
    gameDisplay.blit(texto, (10,5))

def morte():
    pygame.mixer.Sound.play(somDeMorte)
    escreveNaTela("Lex luthor venceu!")


def jogo():

    pygame.mixer.music.load("assets/SupermanTheme.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    supermanPosicaoX = largura * 0.38
    supermanPosicaoY = altura * 0.68
    movimentoX = 0
    velocidade = 7

        
    missileVelocidade = 5
    missileX = random.randrange(0, largura)
    missileY = -200
    pontuacao = 0

    while True:
        # qualquer ação realizada pelo usuário
        acoes = pygame.event.get()
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = -5
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = 5
            if acao.type == pygame.KEYUP:
                movimentoX = 0

        supermanPosicaoX += movimentoX

        if supermanPosicaoX < 0:
            supermanPosicaoX = 0
        elif supermanPosicaoX > largura - alturaSuperman:
            supermanPosicaoX = largura - alturaSuperman

        #analise de colisão do missile com o personagem
        if supermanPosicaoY < missileY + missileAltura:
            if supermanPosicaoX < missileX and supermanPosicaoX + larguraSuperman > missileX or missileX + missileLargura > supermanPosicaoX and missileX + missileLargura < supermanPosicaoX + larguraSuperman:
                morte()
            else:
                print("")
        else:
            print("")
        
        gameDisplay.blit(fundo, (0, 0))
        mostraPersonagem(supermanPosicaoX, supermanPosicaoY)
        missileY = missileY + missileVelocidade

        if missileY > altura:
            missileY = -200
            missileX = random.randrange(0, largura)
            pontuacao = pontuacao + 1
            missileVelocidade += 0.5

        mostraMissile(missileX, missileY)
        mostraPontuacao(pontuacao)
        pygame.display.update()
        clock.tick(60) # atualiza a tela x vezes por segundo

jogo()