import pygame
from random import randint
from pygame_functions import *


class Botao:
    def __init__(self,cor,posx,posy,largura,altura,texto=""):
        self.cor=cor
        self.posx=posx
        self.posy=posy
        self.largura=largura
        self.altura=altura
        self.texto=texto

    def mouseSobre(self,pos):
        if pos[0] > self.posx and pos[0] < self.posx + self.largura:
            if pos[1] > self.posy and pos[1] < self.posy + self.altura:
                return True
        return False

    def desenhaBotao(self):
        pygame.draw.rect(tela,self.cor,(self.posx,self.posy,self.largura,self.altura))
        fonte=pygame.font.SysFont('comicsansms', 20)
        texto_menu=fonte.render(self.texto,True,(BRANCO))
        tela.blit(texto_menu,(self.posx + (self.largura/2 - texto_menu.get_width()/2), self.posy + (self.altura/2 - texto_menu.get_height()/2)))


def desenhaCarro(posx,posy):
    tela.blit(carro,(posx,posy))

def tocar_musica(nome):
    pygame.mixer.init()
    pygame.mixer.music.load(nome)
    pygame.mixer.music.play()

def desenhaColisao(posx,posy,img):
    tela.blit(img,(posx,posy))

def verificaPontuacao(nome_jogador,pontos):
    atual=pontos
    nome=nome_jogador
    arq=open('ranking.txt','r')
    lista2=[]
    for l in arq:
        lista=l.split(';')
    trocou=0
    i=0
    for pos in lista:
        i+=1
        quebra=pos.split(':')
        if trocou==0 and int(quebra[1])<atual:
            quebra[0]=nome
            quebra[1]=atual
            lista2.append(quebra[0]+":"+str(quebra[1]))
            trocou+=1
        else:
            lista2.append(quebra[0]+":"+str(quebra[1]))
    arq.close()        
    i=0
    arq=open('ranking.txt','w')
    for pos in lista2:
        if i==2:
            arq.write(pos)
        else:
            arq.write(pos+';')
        i+=1
    arq.close()

def mostraPontuacao():
    arq=open('ranking.txt','r')
    for l in arq:
        lista=l.split(';')
    exibe_rk=texto2.render("RANKING",True,(25,25,112))
    exibe_p1=texto2.render(("1º lugar----> "+lista[0]),True,(25,25,112))
    exibe_p2=texto2.render(("2º lugar----> "+lista[1]),True,(25,25,112))
    exibe_p3=texto2.render(("3º lugar----> "+lista[2]),True,(25,25,112))
    tela.blit(exibe_rk,(352.5,190))
    tela.blit(exibe_p1,(288,230))
    tela.blit(exibe_p2,(288,260))
    tela.blit(exibe_p3,(288,290))
    
pygame.init()

largura=800
altura=600
screenSize(800,600)
tela=pygame.display.set_mode((largura,altura))

# CORES
CINZA=(204,204,204)
PRETO=(0,0,0)
VERDE=(2,91,47)
VERDE_CLARO=(6,138,80)
VERDE_ESCURO=(0,100,0)
VERDE_ESCURO2=(0,140,0)
AZUL_CLARO=(123,104,238)
AZUL_ESCURO=(0,0,128)
BRANCO=(255,255,255)
pygame.display.set_caption("Corrida Matemática")

# IMAGENS
lousa=pygame.image.load("./imagens/lousa.jpg")
fundo=pygame.image.load("./imagens/fundo.jpg")
carro=pygame.image.load("./imagens/carro.png")
cone=pygame.image.load("./imagens/cone.png")
cone2=pygame.image.load("./imagens/cone.png")
fundo_menu=pygame.image.load("./imagens/bg_menu.jpg")
numeros=[pygame.image.load("./imagens/n_0.png"),pygame.image.load("./imagens/n_1.png"),pygame.image.load("./imagens/n_2.png"),
        pygame.image.load("./imagens/n_3.png"),pygame.image.load("./imagens/n_4.png"),pygame.image.load("./imagens/n_5.png"),
        pygame.image.load("./imagens/n_6.png"),pygame.image.load("./imagens/n_7.png"),pygame.image.load("./imagens/n_8.png"),
        pygame.image.load("./imagens/n_9.png")]
colide=pygame.image.load("./imagens/colide.png")
professor=[pygame.image.load("./imagens/prof.png"),pygame.image.load("./imagens/prof2.png")]
img_vidas=[pygame.image.load("./imagens/vida1.png"),pygame.image.load("./imagens/vida2.png"),pygame.image.load("./imagens/vida3.png")]
nuvem=pygame.image.load("./imagens/nuvem.png")

#OBTENDO OS RETANGULOS DAS IMAGENS - Carro e Cone
rect_carro=carro.get_rect()
rect_cone=cone.get_rect()
rect_cone2=cone2.get_rect()
rect_num0=numeros[0].get_rect()
rect_num1=numeros[1].get_rect()
rect_num2=numeros[2].get_rect()
rect_num3=numeros[3].get_rect()
rect_num4=numeros[4].get_rect()
rect_num5=numeros[5].get_rect()
rect_num6=numeros[6].get_rect()
rect_num7=numeros[7].get_rect()
rect_num8=numeros[8].get_rect()
rect_num9=numeros[9].get_rect()

texto=pygame.font.SysFont('Arial', 50)
texto2=pygame.font.SysFont('comicsans', 30)
texto3=pygame.font.SysFont('cursive', 50)
posx_numero=[205,310,445,558]
px_carro=548
py_cone=101
py_cone2=101
px_cone=[195,310,435,555]
px_cone2=[310,210,435,555]
px_c=px_cone[randint(0,3)]
px_c2=px_cone2[randint(0,3)]
py_carro=450
py_numCerto=-100
py_numErrado=-100
px_numErrado=posx_numero[randint(0,3)]
px_numCerto=posx_numero[randint(0,3)]
i=-1
som=False
dificuldade=1
n1=randint(0,9)
n2=randint(0,9)
resultado=n1+n2
texto_soma=("%i+%i = ?"%(n1,n2))
pontos=0
nome_jogador=" "
fundo_py=0
fundo2_py=-(fundo.get_height())
vidas=3
numero_errado=randint(0,19)


#BOTÕES
botao1_menu=Botao((VERDE_CLARO),300,200,200,50,"Jogar")
botao3_menu=Botao((VERDE_CLARO),300,260,200,50,"Ligar som")
botao4_menu=Botao((VERDE_CLARO),300,260,200,50,"Desligar som")
botao5_menu=Botao((VERDE_CLARO),300,320,200,50,"Dificuldade: Fácil")
botao6_menu=Botao((VERDE_CLARO),300,320,200,50,"Dificuldade: Médio")
botao7_menu=Botao((VERDE_CLARO),300,320,200,50,"Dificuldade: Difícil")
botao_apres=Botao((VERDE_CLARO),400,360,120,40,"Seguir >>")
botao_jogarNovamente=Botao((VERDE),310,360,180,40,"Jogar novamente")


loop_jogo=True
menu=True
instrucoes=False
partida=False
apresentacao=True
informa_nome=True
gameover=False


while(loop_jogo):
    while informa_nome:
        tela.blit(lousa,(0,0))
        texto_n="Por gentileza digite o seu nome:"
        solicita_nome=makeLabel(texto_n,25,200,200,"white","comicsansms")
        showLabel(solicita_nome)
        obter_nome=makeTextBox(316,250,165,2,"Informe o seu nome:",10,20)
        showTextBox(obter_nome)
        nome_jogador=textBoxInput(obter_nome)
        if(nome_jogador!=" " or nome_jogador!=""):
            informa_nome=False

    hideTextBox(obter_nome)
    hideLabel(solicita_nome)

    while(apresentacao):
        tela.blit(lousa,(0,-10))
        botao_apres.desenhaBotao()
        tela.blit(professor[randint(0,1)],(515,234))
        text=("Olá %s seja bem-vindo!<br>Eu sou o professor Sérgio e preciso da sua ajuda para resolver<br>alguns cálculos.No caminho de volta para a minha casa sempre<br>encontro alguns obstáculos no meio do caminho,portanto desta<br>vez preciso da sua ajuda para me livrar desses obstáculos e<br>acertar os números que correspondem as respostas corretas<br>dos cálculos informados.<br><br>Utilize as teclas direcionais ESQUERDA e DIREITA para<br>controlar o veículo."%(nome_jogador))
        apresentacaoLabel=makeLabel(text,21,125,130,"white","Arial")
        showLabel(apresentacaoLabel)
        pygame.time.delay(200)

        for event in pygame.event.get():
                pos_mouse=pygame.mouse.get_pos()
                hideLabel(apresentacaoLabel)
                if event.type == pygame.QUIT:
                    loop_jogo=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_apres.mouseSobre(pos_mouse):
                        apresentacao=False

                if event.type == pygame.MOUSEMOTION:
                    if botao_apres.mouseSobre(pos_mouse):
                        botao_apres.cor=(VERDE)
                    else:
                        botao_apres.cor=(VERDE_ESCURO2)
    hideLabel(apresentacaoLabel)
    while(menu):
        for event in pygame.event.get():
            pos_mouse=pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                menu = False
                loop_jogo=False

            if event.type == pygame.MOUSEMOTION:
                if botao1_menu.mouseSobre(pos_mouse):
                    botao1_menu.cor=(VERDE)
                else:
                    botao1_menu.cor=(VERDE_CLARO)

                if botao3_menu.mouseSobre(pos_mouse):
                    botao3_menu.cor=(VERDE)
                else:
                    botao3_menu.cor=(VERDE_CLARO)

                if botao4_menu.mouseSobre(pos_mouse):
                    botao4_menu.cor=(VERDE)
                else:
                    botao4_menu.cor=(VERDE_CLARO)
                if botao5_menu.mouseSobre(pos_mouse):
                    botao5_menu.cor=(VERDE)
                else:
                    botao5_menu.cor=(VERDE_CLARO)
                if botao6_menu.mouseSobre(pos_mouse):
                    botao6_menu.cor=(VERDE)
                else:
                    botao6_menu.cor=(VERDE_CLARO)
                if botao7_menu.mouseSobre(pos_mouse):
                    botao7_menu.cor=(VERDE)
                else:
                    botao7_menu.cor=(VERDE_CLARO)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao1_menu.mouseSobre(pos_mouse):
                    partida=True
                if botao3_menu.mouseSobre(pos_mouse)and som==False:
                    som=True
                    tocar_musica("start.mp3")
                elif botao4_menu.mouseSobre(pos_mouse)and som==True:
                    som=False
                if botao5_menu.mouseSobre(pos_mouse) and dificuldade==1:
                    dificuldade=2
                elif botao6_menu.mouseSobre(pos_mouse) and dificuldade==2:
                    dificuldade=3
                elif botao7_menu.mouseSobre(pos_mouse)and dificuldade==3:
                    dificuldade=1
        
    
        tela.blit(fundo_menu,(0,0))
        exibe_nomejogo=texto3.render("Corrida Matemática",True,(BRANCO))
        tela.blit(exibe_nomejogo,(237,40))
        botao1_menu.desenhaBotao()
 
        if som:
            botao4_menu.desenhaBotao()
        else:
            botao3_menu.desenhaBotao()
            pygame.mixer.music.pause()
        if dificuldade==1:
            botao5_menu.desenhaBotao()
        elif dificuldade==2:
            botao6_menu.desenhaBotao()
        elif dificuldade==3:
            botao7_menu.desenhaBotao()
        pygame.display.flip()





        while(partida):
    
            tela.fill(CINZA)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    partida=False
                    loop_jogo = False

                if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT and px_carro==310:
                            px_carro=425
                        elif event.key==pygame.K_RIGHT and px_carro==425:
                            px_carro=548

                        elif event.key==pygame.K_RIGHT and px_carro==190:
                            px_carro=310

                        elif event.key==pygame.K_LEFT and px_carro==548:
                            px_carro=425

                        elif event.key==pygame.K_LEFT and px_carro==425:
                            px_carro=310

                        elif event.key==pygame.K_LEFT and px_carro==310:
                            px_carro=190
            rect_resultado=numeros[0].get_rect()
            rect_resultado.x=px_numCerto
            rect_resultado.y=py_numCerto
            rect_numeroErrado=numeros[0].get_rect()
            rect_numeroErrado.x=px_numErrado
            rect_numeroErrado.y=py_numErrado
            if py_cone>600:
                py_cone=randint(-50,0)
                px_c=px_cone[randint(0,3)]
            if py_cone2>600:
                py_cone2=randint(-50,0)
                px_c2=px_cone2[randint(0,3)]
                
            if py_numCerto>600:
                py_numCerto=randint(-300,0)
                px_numCerto=posx_numero[randint(0,3)]
                tela.fill(CINZA)
            if py_numErrado>600:
                numero_errado=randint(0,19)
                py_numErrado=randint(-300,0)
                px_numErrado=posx_numero[randint(0,3)]
                tela.fill(CINZA)
           
            if dificuldade==1:
                py_cone+=5
                py_cone2+=5
                py_numCerto+=5
                py_numErrado+=5
                rect_carro.x=px_carro
                rect_carro.y=py_carro
                rect_cone.x=px_c
                rect_cone.y=py_cone
            
                

            elif dificuldade==2:
                py_cone+=10
                py_cone2+=10
                py_numCerto+=10
                py_numErrado+=10
                rect_carro.x=px_carro
                rect_carro.y=py_carro
                rect_cone.x=px_c
                rect_cone.y=py_cone
                
            else:
                py_cone+=10
                py_cone2+=10
                py_numCerto+=10
                py_numErrado+=10
                rect_carro.x=px_carro
                rect_carro.y=py_carro
                rect_cone.x=px_c
                rect_cone.y=py_cone
                rect_cone2.x=px_c2
                rect_cone2.y=py_cone2
                
            tela.blit(fundo,(0,fundo_py))
            tela.blit(fundo,(0,fundo2_py))
            texto_enunciado=texto.render(texto_soma,True,(233,233,233))
            pygame.draw.rect(tela,(VERDE),(0,0,110,80))
            
            fundo_py+=2
            fundo2_py+=2

            if(fundo_py>fundo.get_height()):
                fundo_py=-(fundo.get_height()-1)
            if(fundo2_py>fundo.get_height()):
                fundo2_py=-(fundo.get_height()-1)

            if(numero_errado<=9):
                tela.blit(numeros[(numero_errado)],(px_numErrado,py_numErrado))
            else:
                exibe_n2=(numero_errado%10)
                exibe_n1=(numero_errado-exibe_n2)//10
                tela.blit(numeros[exibe_n1],(px_numErrado,py_numErrado))
                tela.blit(numeros[exibe_n2],((px_numErrado+25),py_numErrado))

            if(resultado<=9):
                tela.blit(numeros[(resultado)],(px_numCerto,py_numCerto))
            else:
                exibe_n2=(resultado%10)
                exibe_n1=(resultado-exibe_n2)//10
                tela.blit(numeros[exibe_n1],(px_numCerto,py_numCerto))
                tela.blit(numeros[exibe_n2],((px_numCerto+25),py_numCerto))

            ## VERIFICANDO COLISÃO - Carro com número certo
            if rect_carro.colliderect(rect_resultado):
                py_numCerto=700
                pontos+=1
                n1=randint(0,9)
                n2=randint(0,9)
                resultado=n1+n2
                texto_soma=("%i+%i = ?"%(n1,n2))
                if som:
                    tocar_musica("acerto.wav")
                desenhaColisao(rect_resultado.x,rect_resultado.y,nuvem)

            ## VERIFICANDO COLISÃO - Carro com número errado
            if rect_carro.colliderect(rect_numeroErrado):
                py_numErrado=700
                pontos-=1
                numero_errado=randint(0,19)
                
                if som:
                    tocar_musica("Explosion.wav")
                desenhaColisao(rect_numeroErrado.x,rect_numeroErrado.y,colide)
            while(numero_errado==resultado):
                numero_errado=randint(0,19)

            ## VERIFICANDO COLISÃO - Carro com Cone
            if dificuldade==1 and rect_carro.colliderect(rect_cone):
                print("Colidiu num errado")
                py_cone=601
                vidas-=1
                if som:
                    tocar_musica("Explosion.wav")
                desenhaColisao(rect_cone.x,rect_cone.y,colide)

            elif dificuldade==2 and rect_carro.colliderect(rect_cone):
                py_cone=601
                vidas-=1
                if som:
                    tocar_musica("Explosion.wav")
                desenhaColisao(rect_cone.x,rect_cone.y,colide)
                
            elif dificuldade==3 and rect_carro.colliderect(rect_cone):
                    vidas-=1
                    py_cone=601
                    if som:
                        tocar_musica("Explosion.wav")
                    desenhaColisao(rect_cone.x,rect_cone.y,colide)
            elif dificuldade==3 and rect_carro.colliderect(rect_cone2):
                    vidas-=1
                    py_cone2=601
                    if som:
                        tocar_musica("Explosion.wav")
                    desenhaColisao(rect_cone2.x,rect_cone2.y,colide)
                
            if vidas<=0:
                partida=False
                gameover=True
                verificaPontuacao(nome_jogador,int(pontos))
                
            
            if dificuldade==1 or dificuldade==2:
                tela.blit(cone,(px_c,py_cone))
            else:
                tela.blit(cone,(px_c,py_cone))
                tela.blit(cone,(px_c2,py_cone2))
                
            exibe_pontuacao=texto.render("Pontuação:"+(str(pontos)),True,(233,233,233))
            tela.blit(texto_enunciado,(319,5))
            tela.blit(exibe_pontuacao,(540,5))
            tela.blit(img_vidas[(vidas-1)],(30,5))
            desenhaCarro(px_carro,py_carro)
            
            pygame.time.delay(10)
            pygame.display.flip()

        while(gameover):
            tela.fill(CINZA)
            for event in pygame.event.get():
                pos_mouse=pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    gameover=False
                    partida=False
                    menu=False
                    loop_jogo = False
                    

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_jogarNovamente.mouseSobre(pos_mouse):
                        gameover=False
                        menu=True
                        vidas=3
                        pontos=0
            tela.blit(fundo_menu,(0,0))
            exibe_fim1=texto.render("Fim de Jogo!",True,(233,233,233))
            exibe_fim2=texto2.render(("Jogador: "+nome_jogador+"          Pontos obtidos:"+str(pontos)),True,(233,233,233))
            tela.blit(exibe_fim1,(280,30))
            tela.blit(exibe_fim2,(196,120))
            mostraPontuacao()
            botao_jogarNovamente.desenhaBotao()
            
            pygame.display.flip()
                
pygame.quit()
