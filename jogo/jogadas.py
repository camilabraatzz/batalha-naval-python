from utils.texto import gera_texto


def posicao_navios(tabuleiro):
    nome_jogador = tabuleiro['jogador']['nome']
    area = tabuleiro['area']
    for i in range(1, 6):
        print(gera_texto(f'{nome_jogador}, posicione seus navios'))
        linha = int(input(f'digite o número da linha a qual deseja inserir o navio {i} '))
        coluna = int(input(f'digite a coluna da linha a qual deseja inserir o navio {i} '))
        area[linha][coluna] = gera_texto('🚢')

