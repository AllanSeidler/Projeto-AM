import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def qcj():
    # Quantidade de cartas jogadas
    df['cartas_jogadas'].plot(kind='hist', bins=8, title='Cartas jogadas')
    plt.xlabel('Quantidade')
    plt.ylabel('Frequência')
    plt.show()

def cartas_e_valores(df): # Cartas jogadas e valor correspondente nas mãos
    # Contagem de aparições para cada valor em cada coluna
    valores_unicos = sorted(pd.concat([df[col] for col in ['cartas_jogadas','qtd_valor_p2']]).unique())  # Valores únicos (ex.: 0-11)
    contagem = {col: df[col].value_counts().reindex(valores_unicos, fill_value=0) for col in ['cartas_jogadas','qtd_valor_p2']}

    # Transformar para DataFrame
    df_contagem = pd.DataFrame(contagem)

    # Gráfico de barras agrupadas
    x = np.arange(len(valores_unicos))  # Posições para valores únicos no eixo x
    largura = 0.15  # Largura das barras

    plt.figure(figsize=(10, 6))  # Tamanho do gráfico

    # Adicionando as barras para cada coluna
    for i, coluna in enumerate(['cartas_jogadas','qtd_valor_p2']):
        plt.bar(x + i * largura, df_contagem[coluna], width=largura, label=coluna)

    # Personalização do gráfico
    plt.title('Valor das cartas do dealer', fontsize=14, fontweight='bold')
    plt.xlabel('Valor da Carta', fontsize=12)
    plt.ylabel('Quantidade', fontsize=12)
    plt.xticks(x + largura * (len(df.columns) - 1) / 2, valores_unicos)  # Centralizar os rótulos no eixo x
    plt.legend(title="Cartas", fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Exibir
    plt.tight_layout()
    plt.show()


if __name__=='__main__':
    df = pd.read_csv('csv/mentiu.csv')
    

    # Visão geral do dataset
    print("Dimensões do dataset:", df.shape)
    print("Colunas do dataset:", df.columns)
    # df.hist(bins=30, figsize=(10, 8))
    # plt.show()
    
    # cartas_e_valores(df)

    df = pd.read_csv('csv/duvidou.csv')
    m = [[0,0],[0,0]]


    for a in range(len(df)):
        
        if df['mentiu'][a]: i=0
        else: i=1
        if df['duvidou'][a]: j=0
        else: j=1

        m[i][j]+=1

    print(m[0])
    print(m[1])
    