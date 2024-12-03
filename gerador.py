import random as rd
import pandas as pd


cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

class Jogo():
    fp1 = open('mentiu.csv','at',encoding='UTF-8')
    fp2 = open('duvidou.csv','at',encoding='UTF-8')

    def __init__(self):
        # JOGADOR
        self.mao_jogador = (rd.randint(1,51)+rd.randint(1,51))//2 # tamanho da mao do jogador
        self.total_jogada = rd.randint(1,4) # total de cartas que foram jogadas
        self.qtd_do_valor_na_mao = rd.randint(0,min(self.mao_jogador,4)) # quantidade de cartas de valor da pilha na mao do jogador
        self.qtd_do_valor_jogado = rd.randint(0,min(self.total_jogada,self.qtd_do_valor_na_mao)) # quantidade de cartas do valor que foram jogados
        self.mentiu = self.qtd_do_valor_jogado!=self.total_jogada # se mentiu ou nao

        # DUVIDADOR
        self.mao_duvidador=rd.randint(1,52-self.mao_jogador) # tamanho da mao do duvidador
        self.qtd_do_valor_na_mao_duvidador = rd.randint(0,min(self.mao_duvidador,4-self.qtd_do_valor_na_mao)) # quantidade de cartas de valor da pilha na mao do duvidador
        
        
        self.duvidou = (
            (self.qtd_do_valor_na_mao_duvidador==3) and (self.total_jogada >= self.qtd_do_valor_na_mao_duvidador)
            or rd.choice([False, True])
        )
        
        # PILHA
        self.descarte=mao_duvidador= self.total_jogada + rd.randint(0,52-self.mao_jogador-self.mao_duvidador) # cartas na pilha de descarte
        self.carta = rd.choice(cards) # valor que deve ser jogado

    
    def imprime(self):
        if(Jogo.fp1.tell()==0):
            Jogo.fp1.write("Carta, Descarte, Tam. mão P1, Cartas jogadas, Tam. mão P2, Qtd. valor P2, Mentiu\n")
        Jogo.fp1.write(f'{self.carta}, {self.descarte}, {self.mao_jogador}, {self.total_jogada}, {self.mao_duvidador}, '+
            f'{self.qtd_do_valor_na_mao_duvidador}, {self.mentiu}\n')
        
        if(Jogo.fp2.tell()==0):
            Jogo.fp2.write("Carta, Descarte, Tam. mão P1, Cartas jogadas, Qtd valor P1, Qtd valor jogado, Mentiu, Tam. mão P2, Duvidou\n")
        Jogo.fp2.write(f'{self.carta}, {self.descarte}, {self.mao_jogador}, {self.total_jogada}, {self.qtd_do_valor_na_mao}, {self.qtd_do_valor_jogado}, '+
            f'{self.mentiu}, {self.mao_duvidador}, {self.duvidou}\n')
        
    



if __name__=='__main__':
    
    for i in range(int(input('n?'))):
        Jogo().imprime()
        

    


    





    
    
