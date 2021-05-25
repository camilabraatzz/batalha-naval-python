from telas.tabuleiro import mostrar_tabuleiro, tabuleiro_final
from utils.cores import adiciona_cor
from utils.texto import gera_texto


def valida_posicao_bombas(jogador1, jogador2, tabuleiro1, tabuleiro2):
    jogador2['vez'] = False
    while True:
        while jogador1['vez']:
            mostrar_tabuleiro(tabuleiro2)

            area = tabuleiro2['area']
            linha = int(input(f'{jogador1["nome"]}, digite o número da linha a qual deseja inserir a bomba '))
            coluna = int(input(f'{jogador1["nome"]}, digite a coluna da linha a qual deseja inserir a bomba '))

            if area[linha][coluna] == '🚢':
                print(f'{adiciona_cor("1;33m", gera_texto("Você acertou um barco, continue jogando"))}')
                jogador1['pontos'] += 1
                jogador1['vez'] = True
                area[linha][coluna] = gera_texto('💥')
                if jogador1['pontos'] == 5:
                    print(f'{jogador1["nome"]} ganhou!!!')
                    tabuleiro_final(tabuleiro1)
                    exit()
                else:
                    continue
            else:
                jogador1['vez'] = False
                print(f'{adiciona_cor("1;31m", gera_texto("Não há nada nessa posição, vez proximo jogador"))}')
                jogador2['vez'] = True
        while jogador2['vez']:
            mostrar_tabuleiro(tabuleiro1)

            area = tabuleiro1['area']
            linha = int(input(f'{jogador2["nome"]}, digite o número da linha a qual deseja inserir a bomba '))
            coluna = int(input(f'{jogador2["nome"]}, digite a coluna da linha a qual deseja inserir a bomba '))

            if area[linha][coluna] == '🚢':
                print(f'{adiciona_cor("1;33m", gera_texto("Você acertou um barco, continue jogando"))}')
                jogador2['pontos'] += 1
                jogador2['vez'] = True
                area[linha][coluna] = gera_texto('💥')
                if jogador2['pontos'] == 5:
                    print(f'{jogador2["nome"]} ganhou!!!')
                    tabuleiro_final(tabuleiro2)
                    exit()
                else:
                    continue
            else:
                jogador2['vez'] = False
                print(f'{adiciona_cor("1;31m", gera_texto("Não há nada nessa posição, vez proximo jogador"))}')
                jogador1['vez'] = True
