import random as rd
import pandas as pd


class Jogo():
    fp1 = open('csv/mentiu.csv','at',encoding='UTF-8')
    fp2 = open('csv/duvidou.csv','at',encoding='UTF-8')

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
        self.carta = rd.randint(1,13) # valor que deve ser jogado

    
    def imprime(self):
        if(Jogo.fp1.tell()==0):
            Jogo.fp1.write("carta,descarte,tam_mao_p1,cartas_jogadas,tam_mao_p2,qtd_valor_p2,mentiu\n")
        Jogo.fp1.write(f'{self.carta},{self.descarte},{self.mao_jogador},{self.total_jogada},{self.mao_duvidador},'+
            f'{self.qtd_do_valor_na_mao_duvidador},{self.mentiu}\n')
        
        if(Jogo.fp2.tell()==0):
            Jogo.fp2.write("carta,descarte,tam_mao_p1,cartas_jogadas,qtd_valor_p1,qtd_valor_jogado,mentiu,tam_mao_p2,duvidou\n")
        Jogo.fp2.write(f'{self.carta},{self.descarte},{self.mao_jogador},{self.total_jogada},{self.qtd_do_valor_na_mao},{self.qtd_do_valor_jogado}, '+
            f'{self.mentiu},{self.mao_duvidador},{self.duvidou}\n')
        
    




def remove_duplicados(fn:str):
    # Carregar o CSV
    df = pd.read_csv(fn)

    # Remover duplicados
    df_sem_duplicados = df.drop_duplicates()

    # Salvar o resultado em um novo arquivo
    df_sem_duplicados.to_csv(fn, index=False)

    # pd.DataFrame(df)
    print(df_sem_duplicados)


if __name__=='__main__':

    
    
    for i in range(0,int(input('Inserir mais quantos jogos? '))):
        Jogo().imprime()

        
    remove_duplicados('csv/mentiu.csv')
    remove_duplicados('csv/duvidou.csv')
    


    





    
    
